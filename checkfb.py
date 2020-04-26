import sys
import os
import requests
import notifiers
import requests
from pprint import pprint as pp
import time
import datetime
from selenium import webdriver
from bs4 import BeautifulSoup

from twilio.rest import Client

FB = 'https://www.facebook.com/pg/'


shelters = [
    'giffordcatshelter',
    'northeastanimalshelter',
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

    post_divs = soup.find_all('div', class_='userContentWrapper', limit=10)

    for post in post_divs:
        attrs_dict = post.find('abbr')
        date_epoch = int(attrs_dict['data-utime'])
        post_text = post.find('div', class_='userContent').get_text()
        last_check = datetime.datetime.now() - datetime.timedelta(hours=4)
        if datetime.datetime.fromtimestamp(date_epoch) > last_check:
            date_text = attrs_dict['title']
            print('{}: {}'.format(date_text, post_text))


driver.quit()

