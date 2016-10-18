#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import requests
response = requests.get('https://en.wikipedia.org/wiki/Neighborhoods_in_New_York_City')
html_doc = response.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
table = soup.table
#for td in table:
print (table.tr)

#print(table.prettify())