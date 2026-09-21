import os
import shutil

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


def createPage(page_path, ainfo, lang='fr'):
    outf = open(page_path, 'wt')
    outf.write('---\n')
    outf.write('title: "{} {}"\n'.format(ainfo['first_name'],
                                         ainfo['last_name']))
    outf.write('layout: people\n')
    outf.write('team: "{}"\n'.format(ainfo['team']))
    # for the image, check if there is one, otherwise copy the generic one
    image_path = 'images/people/{}.png'.format(ainfo['id'])
    outf.write('image: "{}"\n'.format(image_path))
    if not os.path.exists('../static/' + image_path):
        shutil.copy('../static/images/people/generic.png',
                    '../static/' + image_path)
    # other optional fields
    if 'subteam' in ainfo:
        outf.write('subteam: "{}"\n'.format(ainfo['subteam']))
    if 'email' in ainfo:
        outf.write('email: "{}"\n'.format(ainfo['email']))
    if 'phone' in ainfo:
        outf.write('phone: "{}"\n'.format(ainfo['phone']))
    if 'room' in ainfo:
        outf.write('room: "{}"\n'.format(ainfo['room']))
    if 'alumni' in ainfo:
        outf.write('alumni: "{}"\n'.format(ainfo['alumni']))
    if 'position' in ainfo and lang == 'fr':
        outf.write('position: "{}"\n'.format(ainfo['position']))
    if 'position_en' in ainfo and lang == 'en':
        outf.write('position: "{}"\n'.format(ainfo['position_en']))
    if 'alumni_position' in ainfo and lang == 'fr':
        outf.write('alumni_position: "{}"\n'.format(ainfo['alumni_position']))
    if 'alumni_position_en' in ainfo and lang == 'en':
        outf.write('alumni_position: "{}"\n'.format(ainfo['alumni_position_en']))
    outf.write('---\n\n')
    # add publication section?
    outf.write('\n\n## Publications\n\n{{< people-publications >}}\n\n')
    
    outf.close()


def updatePage(page_path, ainfo, lang='fr'):
    # read and update/add fields with different values
    out_l = []
    with open(page_path, 'rt') as inf:
        header_def = 0
        header_fields = set()
        for line in inf:
            if line[:3] == '---':
                if header_def == 1:
                    # we're about to close the header, add missing/new optional fields
                    for ff in ['email', 'phone', 'room', 'alumni',
                               'subteam', 'selected_dois']:
                        if ff in ainfo and ff not in header_fields:
                            out_l.append('{}: "{}"\n'.format(ff, ainfo[ff]))
                    if 'position' not in header_fields:
                        if 'position' in ainfo and lang == 'fr':
                            out_l.append('position: "{}"\n'.format(ainfo['position']))
                        if 'position_en' in ainfo and lang == 'en':
                            out_l.append('position: "{}"\n'.format(ainfo['position_en']))
                    if 'alumni_position' not in header_fields:
                        if 'alumni_position' in ainfo and lang == 'fr':
                            out_l.append('alumni_position: "{}"\n'.format(ainfo['alumni_position']))
                        if 'alumni_position_en' in ainfo and lang == 'en':
                            out_l.append('alumni_position: "{}"\n'.format(ainfo['alumni_position_en']))
                header_def += 1
                out_l.append(line)
            elif header_def < 2:
                # header part
                line = line.rstrip().split(':')
                field = line[0]
                value = ':'.join(line[1:])
                value = value.replace('"', '').lstrip()
                if field in ainfo and ainfo[field] != value:
                    value = ainfo[field]
                if field == 'position' and lang == 'en' and 'position_en' in ainfo:
                    value = ainfo['position_en']
                if field == 'alumni_position' and lang == 'en' and 'alumni_position_en' in ainfo:
                    value = ainfo['alumni_position_en']
                header_fields.add(field)
                out_l.append('{}: {}\n'.format(field, value))
            else:
                out_l.append(line)
    # write output file
    outf = open(page_path, 'wt')
    for line in out_l:
        outf.write(line)
    outf.close()


# for each member, check/create page informations
for author in auth_info:
    # check french page
    page_path = '../content/people/{}.md'.format(author)
    if os.path.exists(page_path):
        updatePage(page_path, auth_info[author])
    else:
        createPage(page_path, auth_info[author])
    # check english page
    page_path = '../content/people/{}.en.md'.format(author)
    if os.path.exists(page_path):
        updatePage(page_path, auth_info[author], lang='en')
    else:
        createPage(page_path, auth_info[author], lang='en')
