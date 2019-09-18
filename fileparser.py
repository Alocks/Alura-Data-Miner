import codecs
import os
import requests

#decode json chunks from a text file
def json_decoder(file):
    file = open(file, 'r')
    file = file.read().replace(chr(92) * 2, chr(92))
    file = codecs.decode(file, 'unicode_escape')
    lst = file.split('\n')
    tofile = []
    for i in lst:
        if not i:
            continue
        j = i.index(':') + 2
        k = i.index('"', 50)
        tofile.append(i[j:k])
    try:
        os.remove('output.txt')
    except OSError:
        pass
    with open('output.txt', 'w') as f:
        for item in tofile:
            print(item)
            f.write(f'{item}\n')

#Download batch of links from a .txt file
def get_files(data):
    file = open(data, 'r')
    lst = file.read().split('\n')
    for i in lst:
        if not i:
            continue
        video_name = i.split('=')[-1]
        print('Downloading ' + video_name)
        r = requests.get(i)
        if os.path.isdir("./" + video_name.split('-')[0]) is not True:
            os.mkdir(video_name[:3])
        with open(video_name[:3] + "/" + video_name, 'wb') as f:
            f.write(r.content)
