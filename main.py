from alurascraper import AluraScraper
import parser


#############Login#############
print('Username:')
user = input()
print('Password:')
password = input()
f = AluraScraper(user, password)
###############################

####################Crawler######################
formacao = f.choose_formation()#Choose formation
links = f.formation_crawler()#collect links
#################################################

################Scraper################
f.scraper(links) #Scrap all json chunks
#######################################

###########################Parser###########################
parser.decode_json('data.txt') #Parse json chunks to links
parser.get('output.txt') #Download all links from a tet file
############################################################