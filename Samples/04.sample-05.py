# 환율

from currency_converter import CurrencyConverter


cc = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')

print(cc.convert(1,'USD','KRW'))

import requests
from bs4 import BeautifulSoup    # 크롤링을 하는 것이다. 특정 사이트에서 환율에 관한 정보만 크롤링 해서 가져오는 것이다.

def get_exchange_rate(target1, target2):
    headers = {
        'User-Agent': 'Mozilla/5.0',  # 웹브라우저 처음이 Mosilla라서 먼처 써준다. 왜냐하면 처음부터 있기 때문에 모든 웹브라우저에 다 있다.
        'Content-Type': 'text/html; charest=utf-8' # 정보를 헤더 정보에 담아준다.
    }

    response = requests.get('https://kr.investing.com/currencies/{}-{}'.format(target1, target2), headers=headers)
    
    content = BeautifulSoup(response.content, 'html.parser')
    
    containers = content.find('span', {'data-test': 'instrument-price-last'})
    print(containers.text)

get_exchange_rate('usd','krw')