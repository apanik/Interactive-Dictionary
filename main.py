import requests

app_id = '5c77b0a4'
app_key = '7647b13cb131b250c4f7fc87e2788a20'

language = 'en-gb'
word = input("Please Enter a word:  ")
word_id = word
fields = 'definitions'
strictMatch = 'false'
url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + word_id.lower() + '?fields=' + fields + '&strictMatch=' + strictMatch
r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
data_string = r.json()
if r.status_code != 404:
    definitions = data_string['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions']
    print(definitions[0])
else:
    print("The text you entered is not a valid word...Try Again")


