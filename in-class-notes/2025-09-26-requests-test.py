import requests

url = 'https://www.loc.gov'

search_endpoint = '/search'

parameters = {
  'fo':'json',
  'q' :'yarn'
  }

r = requests.get(url + search_endpoint, params = parameters)

print('You requested:', r.url)
print('Response code:', r.status_code)


