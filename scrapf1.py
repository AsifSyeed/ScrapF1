from bs4 import BeautifulSoup
import requests, openpyxl

try:
    source = requests.get('http://ergast.com/api/f1/2022/drivers')
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'xml')

    givenNames = soup.find_all('GivenName')

    for givenName in givenNames:
        print(givenName.get_text())

except Exception as e:
    print(e)