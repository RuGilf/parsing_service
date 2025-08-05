import requests
from bs4 import BeautifulSoup
import csv
agree = ''
headers = {'user-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}

def update_script(url):
    response = requests.get(url, headers=headers)

    with open('data.csv', mode='w', newline='') as file:
        fieldnames = ['id', 'уникальный номер', 'приоритет зачисления', 'сумма баллов', 'согласие на зачисление']
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
        csv_writer.writeheader()
    
        soup = BeautifulSoup(response.text, "html.parser")
        rows = soup.find('table', class_='data with-hover sortable js-fixed js-table-data').find('tbody').find_all('tr')
    
        for row in rows: 
            columns = row.find_all('td') 
		
            if not columns[17].text.strip():
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

def places_function(SPECIALTIES):
    with open('places.csv', mode='w', newline='') as file:
        fieldnames = ['Специальность', 'Количество мест']
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
        csv_writer.writeheader()

        for specialty, url in SPECIALTIES.items(): 
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            places = soup.find('div', text=lambda t: t and 'Всего мест:' in t)
            places_count = 'Не удалось получить данные'
            if places:
                places_count = places.find_next_sibling('div').get_text(strip=True)
            
            csv_writer.writerow({
                'Специальность': specialty,
                'Количество мест': places_count
            })
