import requests

text = requests.get('https://www.python.org/').text

print(text)