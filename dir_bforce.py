import requests

wordlist = open('/usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-small.txt')
lines = wordlist.readlines()

url = raw_input('Set URL widout protocol (example: example.com/): ')

for line in lines:
    stcod = 404
    if line[0] != "#":        
        result = requests.get('http://'+url+line)
        stcod = result.status_code

    if stcod != 404:
        print url+line, stcod
