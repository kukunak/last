import requests
from bs4 import BeautifulSoup

def params_input(search):
    params = {'q': search}
    return params
    
def avito(search_name):
    avito_url = 'https://www.avito.ru/moskva/muzykalnye_instrumenty/gitary_i_drugie_strunnye?'
    result = requests.get(avito_url, params=params)
    return result

def find_in_soup(result):
    soup = BeautifulSoup(result.content, 'html.parser')
    title = soup.find_all(class_='item_table-header')
    return title


def parse_price(price):
    price = price.replace('₽', '').replace(' ', '').strip().lower()
    if price.isdigit():
        return int(price)
    return 0 if price == 'бесплатно' else -1


def find_price_list(title):
    socks_name = item.find(class_='title').get_text().strip()
    socks_price = parse_price(item.find(class_='price').get_text())
    return dict(title=socks_name, price=socks_price)
    

if __name__=="__main__":
    params = params_input(input('Напишите, что хотите найти на Авито: \n'))
    res = avito(params)
    title = find_in_soup(res)
    price_list = []
    for item in title:
        find_price_list(title)
        price_list.append(find_price_list(title))
    print(price_list)
    #print(title)