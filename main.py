import requests

text = requests.get('https://www.python.org/').text

print(text)

for num in range(50):
    print('Hello world', '[' + str(num + 1) + ']')  # This string code create sequence of 50 'Hello world'