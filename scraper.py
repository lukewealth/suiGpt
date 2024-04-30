import requests
from bs4 import BeautifulSoup

url = "https://github.com/MystenLabs/apps/blob/main/kiosk/docs/creating_a_rule_guide.md#rule-structure-dummy"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
print(page.text)