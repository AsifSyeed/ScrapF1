from bs4 import BeautifulSoup
import requests, openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'F1 Drivers 2022'
sheet.append(['Given Name', 'Family Name', 'Permanent Number', 'Nationality'])

try:
    source = requests.get('http://ergast.com/api/f1/2022/drivers')
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'xml')
    print(soup)

    givenNames = soup.find_all('GivenName')
    familyNames = soup.find_all('FamilyName')
    permanentNumbers = soup.find_all('PermanentNumber')
    nationalities = soup.find_all('Nationality')

    for givenName in givenNames:
        print(givenName.get_text())
        sheet.append({'Given Name': givenName.get_text()})

except Exception as e:
    print(e)

excel.save('IMDB Movie Ratings.xlsx')