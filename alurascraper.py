from bs4 import BeautifulSoup
import mechanize, os
from http.cookiejar import CookieJar

liga = 'https://cursos.alura.com.br'
classes = ['learning-content__link', 'courseSectionList-section', 'task-menu-nav-item-link-VIDEO']

class AluraScraper():
        def __init__(self, user, password):
            cj = CookieJar()
            self.__br = mechanize.Browser()
            self.__br.set_handle_robots(False)
            self.__br.set_cookiejar(cj)
            self.__br.open("https://cursos.alura.com.br/loginForm")

            self.__br.select_form(nr=1)
            self.__br.form['username'] = user
            self.__br.form['password'] = password
            self.__br.submit()

        def course_scraper(self, lst, aux=0):
            links=[]
            for link in lst:
                req = self.__br.open(link).read()
                soup = BeautifulSoup(req, 'html.parser')
                for a in soup.find_all('a', class_=classes[aux]):
                    if a['href'].startswith('/'):
                        print(a['href'])
                        links.append(liga + a['href'])
            if aux < 2:
                print(str(aux*20) + '%')
                return self.course_scraper(lst=links, aux=aux+1)
            print('60%')
            result=[]
            for link in links:
                print(link + '/video')
                req = self.__br.open(link + '/video').read()
                result.append(req)
            try:
                os.remove('data.txt')
            except OSError:
                pass
            with open('data.txt', 'w') as f:
                for item in result:
                    f.write(f'{item}\n')
            print('Done! Saved in data.txt')