import re, json, time
from urllib.request import build_opener
from urllib.request import HTTPCookieProcessor
from http.cookiejar import CookieJar
from bs4 import BeautifulSoup


rkuv_url = 'https://www.uvo.gov.sk/register-konecnych-uzivatelov-vyhod-427.html?page=1&limit=80&sort=nazov&sort-dir=ASC&ext=0&ico=&nazov=&obec='
base = 'https://www.uvo.gov.sk'

def connect(url):
    cj = CookieJar()
    opener = build_opener(HTTPCookieProcessor(cj))
    page = opener.open(url)
    data = BeautifulSoup(page,"html.parser")
    return data

def get_end_users(soup):
    #table = soup.findAll('table', {'class': 'table table-striped table-data'})
    #trs = soup.find_all('tr')
    #trs = soup.tr
    #print(trs.contents[0])




#vrati pocet stranok na rkuv
def get_number_of_pages(soup):
    number_of_pages = 0
    #div, kde je select box + pocet_stranok
    div = soup.find('div', {"class": "pag-page"})

    #pocet_stranok v elemente span
    spans = div.find_all('span')

    for span in spans:
        #format 'z @number_of_pages' -> hladam zhodu s 'z '
        match = re.findall('z ',str(span))
        if(len(match) > 0):
            split = span.string.split(' ')
            number_of_pages = int(split[1])

    return number_of_pages

def getRKUV():
    return_list = []
    soup = connect(rkuv_url)
   #number_of_pages = get_number_of_pages(soup)
    number_of_pages = 1


    for i in range(0,number_of_pages):
        trs = soup.find_all('tr')
        links = [str(base) + str(tr.get('onclick'))[24:-2] for tr in trs]

        for link in links:
            link_soup = connect(link)
            end_users = get_end_users(link_soup)



    #for i in range(0,number_of_pages):
        # get_all_links_from_page
            # for all links
            # get_soup_for_record
            # get_data
            # insert

    return return_list


start_time = time.time() # Exec Time

output = getRKUV()

print("--- %s seconds ---" % (time.time() - start_time)) # Term Time