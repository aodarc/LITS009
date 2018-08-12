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
    filename = url.split('/')[-1]
    with open(filename, 'wb') as my_file:
        my_file.write(new.content)
    print("File download.")
    # if os.path.exists(filename):
    #     print(filename)


if __name__ == '__main__':
    download(url)