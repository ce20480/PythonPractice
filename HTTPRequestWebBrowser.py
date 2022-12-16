# TCP(Transport control protocol) above IP(Internet protocol) layer
# Assumes IP layer loses information and thus stores data and resends if neccessary
# creates a pipe which connects processes together end of pipe is called a socket which is connected to ports 
# which are specific to applications/protocols
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()#encode turns the bytes into unicode
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')#decode converts the unicode back into a string
mysock.close()
# even easier way to make a web browser using urllib
import urllib.request, urllib.error, urllib.parse
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhand:
    print(line.decode().strip())
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1 #.get() gets value from key but if key doesnt exists gives value of 2 argument
print(counts)

from bs4 import BeautifulSoup #bs4 allows us to use BeatifulSoup which is a file that has a way to scan for url's in hmtl files

url = input('Enter - ') # example input Enter - https://dr-chuck.com/page1.htm and it will give you https://dr-chuck.com/page2.htm
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
# retrieve all anchor tags which is the beginning or end of text which represents hyper text links
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ctx.CERT_NONE

url = input('Enter - ') # example input Enter - https://dr-chuck.com/page1.htm and it will give you https://dr-chuck.com/page2.htm
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
# retrieve all anchor tags which is the beginning or end of text which represents hyper text links
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

import xml.etree.ElementTree as ET
# xml is better for rich and hiearchical documents(word)
# json is more efficient at moving data between 2 systems 
# The ''' allows for strings to go onto different lines and this is what data a network would send and we would do the methods below to understand it
data = '''<person> 
  <name>chuck</name>
  <phone type='int1'>
    +1 734 303 4456
  </phone>
  <email hide='yes'/>
<person>'''

tree = ET.fromstring(data)
print('Name: ', tree.find('name').text)
print('Attr: ', tree.find('email').get('hide'))

input = '''<stuff>
    <users>
        <user x="2"
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall("users/user")
print('User count: ', len(lst))
for item in lst:
    print('Name: ', item.find('name').text)
    print('Id: ', item.get('id').text)
    print('Attribute: ', item.get("x")) #how complicated it is to worth with xml when there is multiple layers in the data
import json 
# JSON represents data as nested lists and dictionaries and returns a python dictionary(can be a dict of lists)
data = '''{
    "name" : Chuck,
    "phone" : {
        "type" : "int1",
        "number" : +1 734 303 4456"
    }
    "email" : {
        "hide" : "yes"
    }'''

info = json.loads(data)
print("Name: ", info["name"])
print('Hide: ', info["hide"])