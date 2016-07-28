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

def getLink(soup):
    ret = 0
    for tag in soup.find_all('tr'):
        match = re.findall('onclick', str(tag))
        if len(match) > 0:
            ret = tag
    return str(ret).split()

def getSoup(rkuv_url):
    tmp = getLink(connect(rkuv_url))

    tmp = tmp[3].split('\'')
    link = tmp[1]

    return connect(base + link)

def getPersons(ico):
    soup = getSoup(ico)
    table = str(soup.findAll('table', {'class': 'table table-striped table-data'}))

    tmp = table.split('<td>')[1:]
    new_arr = []
    for out in tmp:
        ret = out.replace('\n', '')
        ret = ret.replace('</td>', '')
        ret = ret.replace('<br/>', ' ')
        ret = ret.replace('\r', '')
        new_arr.append(ret)

    persons = []
    for i in range(0, len(new_arr), 4):
        tmp = []
        tmp.append(new_arr[i])
        tmp.append(new_arr[i + 1])
        tmp.append(new_arr[i + 2].replace('  ', ''))
        tmp.append(new_arr[i + 3][:3])
        persons.append(tmp)
    return persons

#vrati pocet stranok na rkuv
def get_number_of_pages():
    number_of_pages = 0

    soup = connect(rkuv_url)

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
    number_of_pages = get_number_of_pages()

    #for i in range(0,number_of_pages):

    #for i in range(0,number_of_pages):
        # get_all_links_from_page
        # get_soup_for_record
        # get_data
        # insert

    return return_list


start_time = time.time() # Exec Time

output = getRKUV()

print("--- %s seconds ---" % (time.time() - start_time)) # Term Time