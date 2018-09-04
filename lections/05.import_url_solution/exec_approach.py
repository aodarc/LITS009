import requests
url = 'https://raw.githubusercontent.com/aodarc/LITS009/master/lections/4.recurtion_example.py'
def download(url):
    new = requests.get(url, allow_redirects=True)
    new_globals = {}
    exec(new.content, new_globals)
    globals().update(new_globals)

download(url)
print(make_flat(l))
print(make_flat([42,3,[2]]))

