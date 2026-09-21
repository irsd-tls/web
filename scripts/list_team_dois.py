import json
import os
import pyalex
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', help='team')
parser.add_argument('-n', help='minimum number of authors',
                    type=int, default=1)
parser.add_argument('-c', help='minimum citation factor',
                    type=float, default=.95)
parser.add_argument('-q', action='store_true', help='query OpenAlex')
parser.add_argument('-v', action='store_true', help='verbose (titles)')
args = parser.parse_args()

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
        team = line[heads.index('team')]
        if team != args.t:
            continue
        ainfo['id'] = line[heads.index('id')]
        if line[heads.index('oa_id')] != '':
            auth_info[line[heads.index('oa_id')]] = ainfo

print('{} authors with a OpenAlex ID in this team.'.format(len(auth_info)))

if args.q:
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
    # other informations
    swork['year'] = work['publication_year']
    swork['type'] = work['type']
    swork['journal'] = work['primary_location']['raw_source_name']
    # count authors
    for oa_auth in work['authorships']:
        oa_id = None
        if oa_auth['author']['id'] is not None:
            oa_id = oa_auth['author']['id'].split('/')[-1]
            oa_id = oa_id.lower()
        if oa_id in auth_info:
            nb_irsd_auhtors += 1
    # show selected DOIs, or recent publications or with high citations
    # with at least two IRSD members and after IRSD start
    if (nb_irsd_auhtors >= args.n and
        swork['type'] not in excl_types and
        swork['journal'] and
        ((swork['year'] >= 2016 and
          work['citation_normalized_percentile'] is not None and
          work['citation_normalized_percentile']['value'] > args.c))):
        res.append(swork)

print('{} publications prepared.'.format(len(res)))

# sort by year
res_o = sorted(res, key=lambda k: -k['year'])

for work in res_o:
    print(work['doi'])
    if args.v:
        print("\t", work['title'])
