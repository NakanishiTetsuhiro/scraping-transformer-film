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


def get_movie_title_and_img(tag_movie_li, f):
    movie_list = []
    for movieDetail in tag_movie_li:

        try:
            # titleを取得
            unnormalize_title = str(movieDetail.getText()).strip()
            replace_title = re.sub('(【.+|\\n).+', '', unnormalize_title)
            title = replace_title.strip()

            # imgを取得
            img = movieDetail.find('div', {'class': 'pict'}).a.img
            img_src = img['src']
            big_img_url = re.sub('\.jpg$', '1.jpg', img_src)
            movie_list.append({
                'title': title,
                'url': big_img_url
            })
            f.write(str(title) + ',' + str(big_img_url) + '\n')
        except AttributeError as e:
            print(e)

def main():
    albatross_url = 'http://www.albatros-film.com/archives/category/dvd/page/'
    page = 1
    try:
        f = open('albatross.csv', mode='a', encoding='utf8')

        while(page < 10):
            resource = get_web_esource(albatross_url + str(page))
            read_resource = resource.read()
            bs_obj = BeautifulSoup(read_resource, 'lxml')
            tag_movie_li = bs_obj.find('div', {'class': 'bg'}).ul.findAll('li')
            get_movie_title_and_img(tag_movie_li, f)
            time.sleep(1)
            page = page + 1
    except AttributeError as e:
        print(e)
    except IOError as e:
        print(e)

    f.close()

if __name__ == '__main__':
    main()

