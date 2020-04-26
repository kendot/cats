import sys
import os
import requests
import notifiers
import requests
from pprint import pprint as pp
from selenium import webdriver

from twilio.rest import Client

FB = 'https://www.facebook.com/pg/'


shelters = [
    'giffordcatshelter',
    'northeastanimalshelter',
    'brokentailrescue',
    'buddydoghs',
    'MelroseHumaneSociety',
    'thesterlinganimalshelter',
    'tccwaltham',
    'NAShelter',
    'tenlivescatrescue',
    'blackcatrescue',
]

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", chrome_options=options)

print(dir(driver))

for shelter in shelters:
    url = FB + shelter + '/posts'
    print('='*20)
    print(url)
    driver.get(url)
    for post in driver.find_elements_by_class_name('userContent'):
        print('-'*10)
        # print(post.find_element('timestampContent'))
        print(post.text)

driver.quit()

