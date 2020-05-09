import os
import sys
import datetime
from selenium import webdriver
from bs4 import BeautifulSoup

from twilio.rest import Client

FB = 'https://www.facebook.com/pg/'

shelters = [
    # 'giffordcatshelter',
    # 'northeastanimalshelter',
    # 'brokentailrescue',
    # 'buddydoghs',
    # 'MelroseHumaneSociety',
    'thesterlinganimalshelter',
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

all_posts = """"""

for shelter in shelters:
    url = FB + shelter + '/posts'
    print('='*20)
    print(url)
    driver.get(url)
    page_source = driver.page_source

    soup = BeautifulSoup(page_source, 'lxml')

    post_divs = soup.find_all('div', class_='userContentWrapper', limit=10)

    for post in post_divs:
        attrs_dict = post.find('abbr')
        date_epoch = int(attrs_dict['data-utime'])
        post_text = post.find('div', class_='userContent').get_text()[:100]
        # print('{}: {}'.format(len(post_text), post_text))
        last_check = datetime.datetime.now() - datetime.timedelta(hours=12)
        if datetime.datetime.fromtimestamp(date_epoch) > last_check and len(post_text) != 0:
            all_posts += '\n{}\n'.format(url)
            date_text = attrs_dict['title']
            print('{}:\n{}'.format(date_text, post_text))
            all_posts += '{}:\n{}'.format(date_text, post_text)

print('\n\n\nmessage below')
print('{}: {}'.format(len(all_posts), all_posts))

driver.quit()

# Your Account Sid and Auth Token from twilio.com/console

account_sid = os.environ.get('ACCOUNT_SID')
auth_token = os.environ.get('AUTH_TOKEN')
# client = Client(account_sid, auth_token)
# print('sending message...')
# message = client.messages \
#                 .create(
#                      body=all_posts,
#                      from_='+17814233477',
#                      to='+16172707122'
#                  )
#
# print("Message sent...")
