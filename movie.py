from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import URLError
from urllib.error import HTTPError
import time
import re


def get_web_esource(url):
    try:
        return urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    except URLError as e:
        print('The server could not be found!')
        return None


def main():
    transformer_url = 'http://www.transformer.co.jp/products/index.html'
    try:
        f = open('transformer.csv', mode='a', encoding='utf8')

        resource = get_web_esource(transformer_url)
        read_resource = resource.read()
        bs_obj = BeautifulSoup(read_resource, 'lxml')

        img_tags = bs_obj.findAll('img', class_='ph')

        for img_tag in img_tags:
            f.write(str(img_tag['alt']) + ',' + str(img_tag['src']) + '\n')
            # print(img_tag['src'])

    except AttributeError as e:
        print(e)
    except IOError as e:
        print(e)

    f.close()


if __name__ == '__main__':
    main()

