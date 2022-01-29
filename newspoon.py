from colorama import Fore, Back, Style
import requests
from bs4 import BeautifulSoup
from os import get_terminal_size, system
from pyautogui import keyDown, keyUp, press
from time import sleep

def nytimes():
    pages = {
        "HomePage": "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
        "World": "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
        "Business": "https://rss.nytimes.com/services/xml/rss/nyt/Business.xml"
    }
    allNews = {}
    try:
        for page in pages:
            articleList = []
            req = requests.get(pages[page])
            soup = BeautifulSoup(req.content, features='xml')
            articles = soup.findAll('item')

            for a in articles:
                article = {
                    'title': a.find('title').text,
                    'link': a.find('link').text,
                    'description': a.find('description').text,
                }
                articleList.append(article)
            allNews[page] = articleList
    except Exception as e:
        print('NYTimes scraping job failed. Exception: ' + e)
    finally:
        return ['NYTimes' ,allNews]

def pcmag():
    pages = {
        "Editor's Choice": "http://feeds.pcmag.com/Rss.aspx/SectionArticles?sectionId=1475",
        "News & Analysis": "http://feeds.pcmag.com/Rss.aspx/SectionArticles?sectionId=1489"
    }
    allNews = {}
    try:
        for page in pages:
            articleList = []
            req = requests.get(pages[page])
            soup = BeautifulSoup(req.content, features='xml')
            articles = soup.findAll('item')

            for a in articles:
                article = {
                    'title': a.find('title').text,
                    'link': a.find('link').text,
                    'description': a.find('description').text,
                }
                articleList.append(article)
            allNews[page] = articleList
    except Exception as e:
        print('PCMag scraping job failed. Exception: ' + e)
    finally:
        return ['PCMag' ,allNews]

def macworld():
    allNews = {}
    try:
        articleList = []
        req = requests.get("https://www.macworld.co.uk/latest/rss")
        soup = BeautifulSoup(req.content, features='xml')
        articles = soup.findAll('item')

        for a in articles:
            article = {
                'title': a.find('title').text,
                'link': a.find('link').text,
                'description': a.find('description').text,
            }
            articleList.append(article)
        allNews['Latest'] = articleList
    except Exception as e:
        print('MacWorld scraping job failed. Exception: ' + e)
    finally:
        return ['MacWorld' ,allNews]

def techadvisor():
    allNews = {}
    try:
        articleList = []
        req = requests.get("https://www.techadvisor.com/latest/rss")
        soup = BeautifulSoup(req.content, features='xml')
        articles = soup.findAll('item')

        for a in articles:
            article = {
                'title': a.find('title').text,
                'link': a.find('link').text,
                'description': a.find('description').text,
            }
            articleList.append(article)
        allNews['Latest'] = articleList
    except Exception as e:
        print('TechAdvisor scraping job failed. Exception: ' + e)
    finally:
        return ['TechAdvisor' ,allNews]

def sozcu():
    pages = {
        "Breaking": "https://www.sozcu.com.tr/rss",
        "Agenda": "https://www.sozcu.com.tr/kategori/gundem/rss",
        "World": "https://www.sozcu.com.tr/kategori/dunya/rss"
    }
    allNews = {}
    try:
        for page in pages:
            articleList = []
            req = requests.get(pages[page])
            soup = BeautifulSoup(req.content, features='xml')
            articles = soup.findAll('item')

            for a in articles:
                article = {
                    'title': a.find('title').text,
                    'link': a.find('link').text,
                    'description': a.find('description').text,
                }
                articleList.append(article)
            allNews[page] = articleList
    except Exception as e:
        print('Sozcu scraping job failed. Exception: ' + e)
    finally:
        return ['Sozcu' ,allNews]

def printNews(source):
    dataSource = source[0]
    dataNews = source[1]
    print(consoleCol*' ')
    spaceCount = 0
    endlCount = 0
    if consoleCol >= (len(dataSource)+16):
        spaceCount = round((consoleCol-(len(dataSource)+16))/2)
        endlCount = round(consoleCol-(len(dataSource)+16)-spaceCount)
    print(Back.CYAN+Fore.WHITE+Style.BRIGHT+consoleCol*' ')
    print((spaceCount*' ')+"-=#=-=# "+dataSource+" #=-=#=-"+(endlCount*' '))
    print(consoleCol*' '+Style.RESET_ALL)
    print(consoleCol*' ')
    headerCounter = 1
    for header in dataNews:
        print(Fore.CYAN+Style.BRIGHT+"-=# "+header.upper()+" #=-"+Style.RESET_ALL)
        print(consoleCol*' ')
        counter = 1
        for i in dataNews[header]:
            print(Fore.RED+Style.BRIGHT+i['title']+Style.RESET_ALL)
            print(Fore.GREEN+i['description']+Style.RESET_ALL)
            print(Fore.LIGHTWHITE_EX+Style.DIM+i['link']+Style.RESET_ALL)
            print(consoleCol*' ')
            if counter == 10:
                if headerCounter != len(dataNews):
                    print(consoleCol*' ')
                    print(Back.LIGHTCYAN_EX+consoleCol*' '+Style.RESET_ALL)
                break
            else:
                counter += 1
        headerCounter += 1
        print(consoleCol*' ')
    print(consoleCol*' ')

def goTop():
    keyDown('shift')
    for i in range(0,59):
        press('pageup')
    sleep(0.1)
    keyUp('shift')
        

if __name__ == "__main__":
    system("clear && printf '\e[3J'")
    consoleCol = get_terminal_size()[0]
    spaceCount = 0
    endlCount = 0
    if consoleCol >= 72:
        spaceCount = round((consoleCol-72)/2)
        endlCount = round(consoleCol-72-spaceCount)
        print(Fore.WHITE+Back.CYAN+Style.BRIGHT+(consoleCol*'=')+Style.RESET_ALL+Fore.WHITE+Back.CYAN)
        print(consoleCol*' ')
        print((spaceCount*' ')+"███╗   ██╗███████╗██╗    ██╗███████╗██████╗  ██████╗  ██████╗ ███╗   ██╗"+(endlCount*' '))
        print((spaceCount*' ')+"████╗  ██║██╔════╝██║    ██║██╔════╝██╔══██╗██╔═══██╗██╔═══██╗████╗  ██║"+(endlCount*' '))
        print((spaceCount*' ')+"██╔██╗ ██║█████╗  ██║ █╗ ██║███████╗██████╔╝██║   ██║██║   ██║██╔██╗ ██║"+(endlCount*' '))
        print((spaceCount*' ')+"██║╚██╗██║██╔══╝  ██║███╗██║╚════██║██╔═══╝ ██║   ██║██║   ██║██║╚██╗██║"+(endlCount*' '))
        print((spaceCount*' ')+"██║ ╚████║███████╗╚███╔███╔╝███████║██║     ╚██████╔╝╚██████╔╝██║ ╚████║"+(endlCount*' '))
        print((spaceCount*' ')+"╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝ ╚══════╝╚═╝      ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝"+(endlCount*' '))
        print(consoleCol*' ')
        print((spaceCount*' ')+Style.BRIGHT+"               News Collector Script Made By @emiralany                 "+Style.RESET_ALL+Fore.WHITE+Back.CYAN+(endlCount*' '))
        print(consoleCol*' ')
    else:
        print(Fore.WHITE+Style.BRIGHT+'-= NEWSPOON =-')
        print("News Collector Script Made By @emiralany"+Style.RESET_ALL)
    print(Fore.WHITE+Back.CYAN+Style.BRIGHT+(consoleCol*'=')+Style.RESET_ALL)

    printNews(nytimes())
    printNews(pcmag())
    printNews(macworld())
    printNews(techadvisor())
    printNews(sozcu())
    
    goTop()