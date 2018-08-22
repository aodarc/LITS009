import requests
import os.path
url = 'https://raw.githubusercontent.com/aodarc/LITS009/master/lections/4.recurtion_example.py'
def download(url):
    __import__('ipdb').set_trace()
    new = requests.get(url, allow_redirects=True)
    filename = url.split('/')[-1][2:]
    with open(filename, 'wb') as my_file:
        my_file.write(new.content)
    modname = filename.replace('.py','')
    globals()[modname] = __import__(modname)

    a = recurtion_example.l
    recurtion_example.make_flat(a)

download(url)

