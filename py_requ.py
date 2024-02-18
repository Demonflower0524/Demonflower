import requests

reponse = requests.get('https://www.naver.com/')

print(reponse.status_code)
print(reponse.text)