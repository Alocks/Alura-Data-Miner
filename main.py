from alurascraper import AluraScraper
import parser
print('Username:')
u_input = input()
print('Password:')
p_input = input()
#Your login
user = u_input
password = p_input
#Login
s = AluraScraper(user, password)

print('What formation do you wanna get? (e.g.: https://cursos.alura.com.br/formacao-dotnet')
p_input = input()
#Insert the url(s) of the course you wanna get
url = [u_input]
#Scrap all json files using recursive method and save to data.txt
s.course_scraper(lst = url)
#encode and get links from json chunks written in data.txt
parser.encode_json('data.txt')
#Download files from output.txt
parser.get('output.txt')