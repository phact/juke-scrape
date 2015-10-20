from lxml import html
import requests
import mechanize

import cookielib
from BeautifulSoup import BeautifulSoup
import html2text

import codecs

# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

br.addheaders = [('User-agent', 'Chrome')]

br.open('https://jukely.com/log_in')

# View available forms
for f in br.forms():
    print f

br.select_form(nr=0)

# User credentials
br.form['username'] = '***'
br.form['password'] = '***'

# Login
br.submit()

print "Here's my page!!!"


page = br.open('https://jukely.com/unlimited/shows').read()
print(page)



print "other request code"
#page = requests.get('https://www.jukely.com/unlimited/shows')
tree = html.fromstring(page)

print "tree"
print(tree)

#events = tree.xpath('//*[@id="unlimited_container"]')
events = tree.xpath('//script')


print "events"

#i=0
#for e in events:
#    print i
#    i=i+1
#    print e.text


f = open('output','w')

event_text = events[8].text



f.write(event_text.encode('utf-8'))
f.close()

