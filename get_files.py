#!/usr/bin/env python3
from bs4 import BeautifulSoup
from requests import get

# Open the two URLS that contain the most common female/male names,
# Scrape the names and place them in respective lists:
# female.lst
# male.lst
common_female_names_url = 'http://names.mongabay.com/female_names_alpha.htm'
common_male_names_url = 'http://names.mongabay.com/' \
    'male_names_alpha.htm'
descriptor_url = 'http://www.enchantedlearning.com/wordlist/' \
    'adjectivesforpeople.shtml'


# Given a soup of the urls, extract the names and return them as a list
def extract_names(soup):
    results = []
    table = soup.find(lambda tag: tag.name == 'table' and
                      tag.has_attr('id') and
                      tag['id'] == 'myTable')
    for row in table.findAll(lambda tag: tag.name == 'tr'):
        found = row.find(lambda tag: tag.name == 'td')
        if found is not None:
            results.append(found.string)
    return results


def extract_descriptors(soup):
    results = []
    table = soup.find_all(lambda tag: tag.name == 'table')[4]
    for br in table.find_all(lambda tag: tag.name == 'br'):
        item = br.previous
        if item:
            results.append(item.strip())
    return results


# Get the web pages
html_female = get(common_female_names_url).content
html_male = get(common_male_names_url).content
html_desc = get(descriptor_url).content

# Pull out the data
females = extract_names(BeautifulSoup(html_female, 'html.parser'))
males = extract_names(BeautifulSoup(html_male, 'html.parser'))
desc = extract_descriptors(BeautifulSoup(html_desc, 'html.parser'))

with open('women.lst', 'w') as out:
    for f in females:
        out.write(f.lower() + '\n')

with open('men.lst', 'w') as out:
    for m in males:
        out.write(m.lower() + '\n')

with open('descriptors.lst', 'w') as out:
    for d in desc:
        out.write(d.lower() + '\n')
