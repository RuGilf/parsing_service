import requests
from bs4 import BeautifulSoup
import csv
agree = ''
headers = {'user-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}

url = 'https://misis.ru/applicants/admission/progress/baccalaureate-and-specialties/spiskipodavshihzayavleniya/list-p/?id=BVO-COMM-O-090000-NITU_MISIS-OKM-000005382'

response = requests.get(url, headers=headers)

with open('data.csv', mode='w', newline='') as file:
    fieldnames = ['id', 'уникальный номер', 'приоритет зачисления', 'сумма баллов', 'согласие на зачисление']
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')  # <- delimiter=';'
    csv_writer.writeheader()
    
    soup = BeautifulSoup(response.text, "html.parser")
    rows = soup.find('table', class_='data with-hover sortable js-fixed js-table-data').find('tbody').find_all('tr')
    
    for row in rows: 
        columns = row.find_all('td') 
		
        if columns[17].text == '' or None:
            agree = '-'
        else:
            agree = '+'

        data = {
            'id': columns[0].text.strip(), 
            'уникальный номер': columns[1].text.strip(), 
            'приоритет зачисления': columns[3].text.strip(), 
            'сумма баллов': columns[4].text.strip(), 
            'согласие на зачисление': agree
        }
        
        csv_writer.writerow(data)