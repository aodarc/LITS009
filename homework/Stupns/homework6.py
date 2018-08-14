import requests
import os.path


url = 'https://raw.githubusercontent.com/aodarc/LITS009/master/lections/4.recurtion_example.py'


def download(url):
    new = requests.get(url, allow_redirects=True)
    if new.status_code == 404:
        print('No such file found at %s' % url)
        return
    if not url.rfind('.py'):
        a = print('File extension with .py not found')
        return a
    filename = url.split('/')[-1][2:]
    with open(filename, 'wb') as my_file:
        my_file.write(new.content)
    if os.path.exists(filename):
        realpath = filename.replace('.py', '')
        globals()[realpath] = __import__(realpath)
        a = recurtion_example.l
        recurtion_example.make_flat(a)

if __name__ == '__main__':
    download(url)


