import json
import os
import pyalex
import glob
# https://github.com/J535D165/pyalex
# from utils import Article

query_open_alex = True

# read openalex api key
api_key = None
with open('OPENALEX_API_KEY', 'rt') as inf:
    api_key = next(inf).rstrip()
pyalex.config.api_key = api_key

# try to read cache
if not os.path.exists('cache.openalex.json'):
    init_f = open('cache.openalex.json', 'wt')
    init_f.write('{}')
    init_f.close()
with open('cache.openalex.json', 'rt') as cache_inf:
    cache = json.load(cache_inf)

# read the list of IRSD authors
auth_info = {}
with open('people.csv', 'rt') as inf:
    heads = None
    for line in inf:
        line = line.rstrip().split(',')
        if heads is None:
            heads = line
            continue
        ainfo = {}
        ainfo['team'] = line[heads.index('team')]
        ainfo['id'] = line[heads.index('id')]
        if line[heads.index('oa_id')] != '':
            auth_info[line[heads.index('oa_id')]] = ainfo

print('{} authors with a OpenAlex ID.'.format(len(auth_info)))

if query_open_alex:
    print('Querying OpenAlex...')
    # for each author, retrieve all publications
    for oa_auth in auth_info:
        pager = pyalex.Works().filter(author={"id": oa_auth}).paginate(per_page=200)
        auth_dois = []
        for page in pager:
            for ww in page:
                # is this DOI already in the cache?
                auth_dois.append(ww['doi'])
                if ww['doi'] in cache:
                    continue
                cache[ww['doi']] = ww
        print('{}: {} dois'.format(auth_info[oa_auth]['id'], len(auth_dois)))

    # update cache
    with open('cache.openalex.json', 'wt') as cache_outf:
        json.dump(cache, cache_outf)
else:
    print('Not querying OpenAlex. Using cache instead.')

# load selected DOIs
sel_dois = set()
md_files = glob.glob('../content/*md')
md_files += glob.glob('../content/people/*md')
for mdfn in md_files:
    # read and extract DOIs
    with open(mdfn, 'rt') as inf:
        for line in inf:
            line = line.rstrip().split(':')
            if len(line) != 2:
                continue
            if line[0] == 'selected_dois':
                value = ':'.join(line[1:])
                value = value.replace('"', '').lstrip()
                for doi in value.split(';'):
                    if doi == '':
                        continue
                    doi = 'https://doi.org/' + doi
                    if doi not in cache:
                        sel_dois.add(doi)

print('{} DOIs selected found in pages.'.format(len(sel_dois)))

# read DOI list for each team
team_sel_dois = {}
with open('team.dois.tsv') as inf:
    for line in inf:
        line = line.rstrip().split('\t')
        for doi in line[1].split(';'):
            sel_dois.add(doi)
            if doi not in team_sel_dois:
                team_sel_dois[doi] = set()
            team_sel_dois[doi].add(line[0])

if query_open_alex and len(sel_dois) > 0:
    print('Querying OpenAlex...')
    doi_works = pyalex.Works().filter_or(doi=list(sel_dois)).get()
    for ww in doi_works:
        cache[ww['doi']] = ww
    # update cache
    with open('cache.openalex.json', 'wt') as cache_outf:
        json.dump(cache, cache_outf)

# make simpler json
excl_types = ['dataset', 'software', 'conference-abstract']
res = []
for doi in cache:
    if doi is None:
        continue
    nb_irsd_auhtors = 0
    work = cache[doi]
    swork = {}
    doi = doi.replace('https://doi.org/', '')
    swork['doi'] = doi
    swork['title'] = work['title']
    # convert special formatting
    swork['title'] = swork['title'].replace('<i>', '*').replace('</i>', '*')
    swork['title'] = swork['title'].replace(' <sub>', '~').replace('</sub>', '~')
    swork['title'] = swork['title'].replace(' <scp>', '').replace('</scp>', '')
    # other informations
    swork['year'] = work['publication_year']
    swork['type'] = work['type']
    swork['journal'] = work['primary_location']['raw_source_name']
    # authors
    auths = []
    for oa_auth in work['authorships']:
        auth = {}
        auth['name'] = oa_auth['author']['display_name']
        oa_id = None
        if oa_auth['author']['id'] is not None:
            oa_id = oa_auth['author']['id'].split('/')[-1]
            oa_id = oa_id.lower()
        if oa_id in auth_info:
            auth['id'] = auth_info[oa_id]['id']
            auth['team'] = auth_info[oa_id]['team']
            nb_irsd_auhtors += 1
        auths.append(auth)
    swork['authors'] = auths
    # selected by a team?
    swork['sel_team'] = []
    if doi in team_sel_dois:
        for team in team_sel_dois[doi]:
            swork['sel_team'].append(team)
    # show selected DOIs, or recent publications or with high citations
    # with at least two IRSD members and after IRSD start
    if (doi in sel_dois or
        (nb_irsd_auhtors > 1 and
         swork['type'] not in excl_types and
         swork['journal'] and
         (swork['year'] > 2023 or
          (swork['year'] >= 2016 and
           work['citation_normalized_percentile'] is not None and
           work['citation_normalized_percentile']['value'] > .95)))):
        res.append(swork)

print('{} publications prepared.'.format(len(res)))

# sort by year
res_o = sorted(res, key=lambda k: -k['year'])

with open('pubs.json', 'wt') as pubs_outf:
    json.dump(res_o, pubs_outf, indent=2)


# # filter=authorships.institutions.lineage:i4210122796
# for age in range(5):
#     results = pyalex.Works().filter(authorships={"institutions": {"lineage": "i4210122796"}}).filter(publication_year=2026-age, is_oa=True).get(per_page=200)
#     for ww in results:
#         # is this DOI already in the cache?
#         if ww['doi'] in cache:
#             continue
#         cache[ww['doi']] = ww


# TODO add fuzzy matching for author names
