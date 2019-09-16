from alurascraper import AluraScraper, AluraLogin, AluraCrawler
import parser


#############Login#############
print('Username:')
user = input()
print('Password:')
password = input()
###############################

#######Creating Objects########
l = AluraLogin(user, password)
c = AluraCrawler(l._session)
s = AluraScraper(l._session)
###############################

####################Crawler######################
formacao = c.choose_formation()#Choose formation
links = c.formation_crawler(formacao)#collect links
#################################################

################Scraper################
s.scraper(links) #Scrap all json chunks
#######################################

###########################Parser###########################
parser.decode_json('data.txt') #Parse json chunks to links
parser.get('output.txt') #Download all links from a tet file
############################################################