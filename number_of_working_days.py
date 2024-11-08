import requests

url = 'https://parsinger.ru/3.3/2/1.html'
s = []
a = 2

response = requests.get(url=url)
s.append(response.status_code)
print(response.status_code)

for a in range(200):
    url = url.replace(f'{a-1}.h', f'{a}.h')
    response = requests.get(url=url)
    s.append(response.status_code)
    a += a
    print({url}, {response.status_code})
print(sum(s))