import sys
import os
import requests
import notifiers
import requests
from pprint import pprint as pp
from selenium import webdriver
from bs4 import BeautifulSoup

from twilio.rest import Client

FB = 'https://www.facebook.com/pg/'


shelters = [
    'giffordcatshelter',
    # 'northeastanimalshelter',
    # 'brokentailrescue',
    # 'buddydoghs',
    # 'MelroseHumaneSociety',
    # 'thesterlinganimalshelter',
    # 'tccwaltham',
    # 'NAShelter',
    # 'tenlivescatrescue',
    # 'blackcatrescue',
]

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", chrome_options=options)

for shelter in shelters:
    url = FB + shelter + '/posts'
    print('='*20)
    print(url)
    driver.get(url)
    page_source = driver.page_source

    soup = BeautifulSoup(page_source, 'lxml')
    posts = []

    post_divs = soup.find_all('div', class_='userContentWrapper')

    for post in post_divs:
        # post_div = post.find('div', class_='userContent').text
        # date_div = post.find('span', class_='timestampContent')
        # post_div = post.find('div', class_='text_exposed_root')
        date_text = post.find('span', class_='timestampContent').get_text()
        date_text = post.find('span', class_='timestampContent').get_text()
        post_text = post.find('div', class_='userContent').get_text()

        print('{}: {}'.format(date_text, post_text))


driver.quit()
# for post in driver.find_elements_by_class_name('userContent'):
#     print('-'*10)
#     # print(post.find_element('timestampContent'))
#     print(post.text)

