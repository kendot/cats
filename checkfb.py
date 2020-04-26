import datetime
from selenium import webdriver
from bs4 import BeautifulSoup

from twilio.rest import Client

FB = 'https://www.facebook.com/pg/'

shelters = [
    'giffordcatshelter',
    'northeastanimalshelter',
    'brokentailrescue',
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

all_posts = []

for shelter in shelters:
    url = FB + shelter + '/posts'
    all_posts.append('{}\n'.format(url))
    print('='*20)
    print(url)
    driver.get(url)
    page_source = driver.page_source

    soup = BeautifulSoup(page_source, 'lxml')

    post_divs = soup.find_all('div', class_='userContentWrapper', limit=10)

    for post in post_divs:
        attrs_dict = post.find('abbr')
        date_epoch = int(attrs_dict['data-utime'])
        post_text = post.find('div', class_='userContent').get_text()
        last_check = datetime.datetime.now() - datetime.timedelta(days=2)
        if datetime.datetime.fromtimestamp(date_epoch) > last_check:
            date_text = attrs_dict['title']
            print('{}:\n{}'.format(date_text, post_text))
            all_posts.append('{}:\n{}'.format(date_text, post_text))

print(all_posts)
print('\n\n\nmessage below')
print(''.join(all_posts))

driver.quit()

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC8d8fac0b3bd29d0a46e6d1c034a169c1'
auth_token = '8c2ccea453cee9ce6abb00f308704b4b'
# client = Client(account_sid, auth_token)
#
# message = client.messages \
#                 .create(
#                      body=MESSAGE,
#                      from_='+18573080080',
#                      to='+16172707122'
#                  )
#
# print("Message sent...")
