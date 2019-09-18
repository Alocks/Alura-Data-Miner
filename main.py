from alurascraper import AluraLogin
from fileparser import json_decoder, get_files

# Login
print('Username:', end='')
user = input()
print('Password:', end='')
password = input()
# Creating/Manipulating Object
a = AluraLogin(user, password)
a.formation_categories()  # Scrap and select formation categories
a.choose_formation(a.formations)  # Scrap and select a formation
a.formation_crawler()  # Crawls all links which has a video
a.formation_scraper(a.links)  # Scrap all video links requests(json) and save to data.txt
# Parser
json_decoder('data.txt')  # Parse json chunks to links
get_files('output.txt')  # Download all links from a tet file
