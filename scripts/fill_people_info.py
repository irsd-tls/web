import pyalex


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
        for ii, value in enumerate(line):
            ainfo[heads[ii]] = value
        auth_info[ainfo['id']] = ainfo

#
# guess inserm email
#
for auth in auth_info:
    if auth_info[auth]['email'] == '':
        auth_info[auth]['email'] = '{}@inserm.fr'.format(auth_info[auth]['id'])

#
# find OpenAlex author ID
#

# read openalex api key
api_key = None
with open('OPENALEX_API_KEY', 'rt') as inf:
    api_key = next(inf).rstrip()
pyalex.config.api_key = api_key

for auth in auth_info:
    if auth_info[auth]['oa_id'] == '':
        disp_name = '{} {}'.format(auth_info[auth]['first_name'],
                                   auth_info[auth]['last_name'])
        search_o = pyalex.Authors().search(disp_name).filter(has_orcid=True).get()
        # keep the ID with the most publications
        oa_id = None
        npubs = 0
        for res in search_o:
            if res['works_count'] > npubs:
                oa_id = res['id'].replace('https://openalex.org/', '').lower()
                npubs = res['works_count']
        if oa_id is None:
            oa_id = ''
        auth_info[auth]['oa_id'] = oa_id

#
# write new CSV file
#

cols = ['id', 'first_name', 'last_name', 'email',
        'team', 'position', 'position_en',
        'phone', 'room', 'subteam',
        'oa_id', 'selected_dois',
        'alumni', 'alumni_position', 'alumni_position_en']

out_csv = open('people.f.csv', 'wt')
out_csv.write(','.join(cols) + '\n')

for auth in auth_info:
    outl = [auth_info[auth][coln] for coln in cols]
    out_csv.write(','.join(outl) + '\n')

out_csv.close()
