import requests as r
import re
import clipboard
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

html = r.get(clipboard.paste(), headers=headers)
bs = BeautifulSoup(html.text, 'html.parser')
src_list = bs.findAll('a', {'class': 'fileThumb'})
for i in src_list:
    file_url = 'https:' + i['href']
    print(file_url)
    file_name_reg = re.search('^.*\/(.*$)', i['href'])
    try:
        file_name = file_name_reg.group(1)[1:]
        print(file_name)
        image_bytes = r.get(file_url)
        file = open(file_name, "wb")
        file.write(image_bytes.content)
        file.close()
    except Exception as e:
        print(e)
