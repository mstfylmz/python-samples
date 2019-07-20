import requests;

# birinci aşama : kaynağı websitesinden okuma..

r = requests.get('http://xn--mustafaylmaz-84b.com/tr/blog')
print(r.status_code);
print(r.text)


# ikinci aşama : kaynağı parse etme...

