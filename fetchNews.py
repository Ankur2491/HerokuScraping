import redis
import requests
import unidecode
from bs4 import BeautifulSoup
from lxml import etree
import sys
import json
from bson.json_util import dumps
redis_host = "redis-11422.c62.us-east-1-4.ec2.cloud.redislabs.com"
redis_port = 11422
redis_password = "AFahzbIs3wTxs0VMPnvTqkuqyoZOWXwV"
r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
newsObj = {"news":[]}
mainData = {"status": "ok","articles":[]}
'''
try:
    response = requests.get('http://feeds.bbci.co.uk/news/world/rss.xml')
    root = etree.fromstring(response.content)
    for newsItem in root.iter('item'):
        print(newsItem)
        data = {}
        data['title'] = newsItem.find('title').text+'(source:BBC)'
        data['description'] = newsItem.find('description').text
        data['url'] = newsItem.find('link').text
        data['publishedAt'] = newsItem.find('pubDate').text
        imageUrl = data['url']
        image = ""
        page = requests.get(imageUrl)
        soup = BeautifulSoup(page.content, 'lxml')
        html = list(soup.children)[1]
        l = soup.find_all('span', class_='image-and-copyright-container')
        if len(l)>0:
            content=str(l[0])
            src_index = content.index("src=")+5
            jpg_index = content.index("\"",src_index)
            image = content[src_index:jpg_index]
        data['urlToImage'] = image
        mainData['articles'].append(data)
except:
    print("Error in Int bbc",sys.exc_info())

try:
    response = requests.get('https://feeds.a.dj.com/rss/RSSWorldNews.xml')
    root = etree.fromstring(response.content)
    for newsItem in root.iter('item'):
        data = {}
        data['title'] = newsItem.find('title').text+'(source:WSJ)'
        data['description'] =  newsItem.find('description').text
        data['url'] = newsItem.find('link').text
        data['publishedAt'] = newsItem.find('pubDate').text
        data['urlToImage'] = "./img/wall-street-journal.png"
        mainData['articles'].append(data)
except:
    print("error in wsj-world")
try:
    response = requests.get('https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/world/rss.xml')
    root = etree.fromstring(response.content)
    for newsItem in root.iter('item'):
        data = {}
        data['title'] = newsItem.find('title').text+'(source:NY Times)'
        data['description'] =  newsItem.find('description').text
        data['url'] = newsItem.find('link').text
        data['publishedAt'] = newsItem.find('pubDate').text
        data['urlToImage'] = "./img/ny-times.png"
        mainData['articles'].append(data)
except:
    print("error in nytimes-world")

try:
    response = requests.get('https://www.aljazeera.com/xml/rss/all.xml')
    root = etree.fromstring(response.content)
    for newsItem in root.iter('item'):
        data = {}
        data['title'] = newsItem.find('title').text+'(source:Al Jazeera)'
        data['description'] =  newsItem.find('description').text
        data['url'] = newsItem.find('link').text
        data['publishedAt'] = newsItem.find('pubDate').text
        data['urlToImage'] = "./img/al-jazeera.png"
        mainData['articles'].append(data)
except:
    print("error in aljazeera-world")

try:
    response = requests.get('https://www.news18.com/rss/world.xml')
    root = etree.fromstring(response.content)
    for newsItem in root.iter('item'):
        data = {}
        desc = newsItem.find('description').text
        data['publishedAt'] = newsItem.find('pubDate').text
        data['title'] = newsItem.find('title').text+'(source:News18)'
        start = desc.index('=')+2
        data['urlToImage'] =  desc[start:desc.index('\'',start)]
        data['url'] = newsItem.find('guid').text
        desc_start = desc.index('>')+1
        data['description'] = desc[desc_start:]
        mainData['articles'].append(data)
except:
    print("Error in news18-world",sys.exc_info())
try:
    response = requests.get('http://rss.cnn.com/rss/edition_world.rss')
    root = etree.fromstring(response.content)
    for newsItem in root.iter('item'):
        data = {}
        data['title'] = newsItem.find('title').text+'(source:CNN)'
        data['publishedAt'] = newsItem.find('pubDate').text
        desc = newsItem.find('description').text
        if "<" in desc:
            temp_desc = desc[0:desc.index('<')]
            data['description'] = temp_desc
        else:
            data['description'] = desc
        data['url'] = newsItem.find('link').text
        img = ""
        mediaGroup = newsItem.find('media:group',newsItem.nsmap)
        if mediaGroup is not None:
            for m in mediaGroup:
                img = m.attrib['url']
                data['urlToImage'] = img
                break
        if img == "":
            data['urlToImage'] = "./img/cnnLogo.png"
        mainData['articles'].append(data)
except:
    print("Error in Int cnn",sys.exc_info()[0])
try:
    response = requests.get('http://feeds.feedburner.com/ndtvnews-world-news')
    root = etree.fromstring(response.content)
    for newsItem in root.iter('item'):
        data = {}
        data['title'] = newsItem.find('title').text+'(source:NDTV)'
        data['description'] =  newsItem.find('description').text
        data['url'] = newsItem.find('link').text
        data['publishedAt'] = newsItem.find('pubDate').text
        data['urlToImage'] = newsItem.find('fullimage').text
        mainData['articles'].append(data)
except:
    print("Error in ndtv-world")


newsObj['news'].append(mainData)
mainData = {"status": "ok","articles":[]}
print("world done!")
#India

try:
    response = requests.get('http://feeds.feedburner.com/ndtvnews-india-news')
    root = etree.fromstring(response.content)
    for newsItem in root.iter('item'):
        data = {}
        data['title'] = newsItem.find('title').text+'(source:NDTV)'
        data['publishedAt'] = newsItem.find('pubDate').text
        data['description'] =  newsItem.find('description').text
        data['url'] = newsItem.find('link').text
        data['urlToImage'] = newsItem.find('StoryImage').text
        mainData['articles'].append(data)
except:
    print("Error in ndtv-India")

try:
    response = requests.get('https://zeenews.india.com/rss/india-national-news.xml')
    root = etree.fromstring(response.content)
    for newsItem in root.iter('item'):
        data ={}
        data['title'] = newsItem.find('title').text+'(source:ZeeNews)'
        data['description'] = newsItem.find('description').text
        data['publishedAt'] = newsItem.find('pubdate').text
        data['url'] = newsItem.find('link').text
        imageUrl = data['url']
        image = './img/zeeNews.jpg'
        page = requests.get(imageUrl)
        soup = BeautifulSoup(page.content, 'lxml')
        html = list(soup.children)[1]
        l = soup.find_all('div', class_='article-image-block')
        if len(l)>0:
            content=str(l[0])
            src_index = content.index("src=")+5
            jpg_index = content.index("\"",src_index)
            image = content[src_index:jpg_index]
        data['urlToImage'] = image
        mainData['articles'].append(data)
except:
    print('Error in ZeeNews',sys.exc_info())

try:
    response = requests.get('https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms')
    root = etree.fromstring(response.content)
    for newsItem in root.iter('item'):
        data = {}
        data['title'] = newsItem.find('title').text+'(source:TOI)'
        data['publishedAt'] = newsItem.find('pubDate').text
        description = newsItem.find('description').text
        if description:
            if "</a>" in description:
                desc = newsItem.find('description').text.split("</a>")
                data['description'] = desc[1]
            else:
                data['description'] = description
        data['url'] = newsItem.find('link').text
        imageUrl = newsItem.find('link').text
        page = requests.get(imageUrl)
        soup = BeautifulSoup(page.content, 'lxml')
        html = list(soup.children)[1]
        l = soup.find_all('section', class_='_2suu5')
        if len(l)>0:
            content=str(l[0])
            src_index = content.index("src=")+5
            jpg_index = content.index("jpg",src_index)
            data['urlToImage'] = content[src_index:jpg_index] + "jpg"
            mainData['articles'].append(data)
except:
    print("Error in toi",sys.exc_info())

try:
    response = requests.get('https://www.thehindu.com/news/national/feeder/default.rss')
    root = etree.fromstring(response.content)
    for newsItem in root.iter('item'):
        data ={}
        image = './img/theHindu.jpg'
        data['title'] = newsItem.find('title').text+'(source:TheHindu)'
        data['description'] = newsItem.find('description').text
        data['publishedAt'] = newsItem.find('pubDate').text
        data['url'] = newsItem.find('link').text
        page = requests.get(data['url'])
        soup = BeautifulSoup(page.content, 'lxml')
        html = list(soup.children)[1]
        l = soup.find_all('picture')
        data['urlToImage'] = image
        mainData['articles'].append(data)
except:
    print("Error in The Hundu",sys.exc_info())

try:
    response = requests.get('https://www.dnaindia.com/feeds/india.xml')
    root = etree.fromstring(response.content)
    for newsItem in root.iter('item'):
        data = {}
        data['title'] = newsItem.find('title').text+'(source:DNA)'
        data['description'] = newsItem.find('description').text
        data['publishedAt'] = newsItem.find('pubDate').text
        data['url'] = newsItem.find('link').text
        data['urlToImage'] = newsItem.find('enclosure').attrib['url']
        mainData['articles'].append(data)

except:
    print('Error in DNA',sys.exc_info())

newsObj['news'].append(mainData)
mainData = {"status": "ok","articles":[]}
print("India done!")

try:
    response = requests.get('http://www.moneycontrol.com/rss/MCtopnews.xml')
    root = etree.fromstring(response.content)
    for newsItem in root.iter('item'):
        data = {}
        data['title'] = newsItem.find('title').text+'(source:MoneyControl)'
        data['publishedAt'] = newsItem.find('pubDate').text
        data['url'] = newsItem.find('guid').text
        descriptionText = newsItem.find('description').text
        src_index = descriptionText.index("src=")+5
        jpg_index = descriptionText.index("jpg",src_index)
        data['urlToImage'] = content[src_index:jpg_index] + "jpg"

except:
    print('Error in MoneyControl',sys.exc_info())

try:
    response = requests.get('https://www.firstpost.com/rss/business.xml')
    root = etree.fromstring(response.content)
    for newsItem in root.iter('item'):
        data = {}
        data['title'] = newsItem.find('title').text+'(source:FP)'
        data['description'] =  newsItem.find('description').text
        data['url'] = newsItem.find('link').text
        data['publishedAt'] = newsItem.find('pubDate').text
        data['urlToImage'] = newsItem.find('media:content',newsItem.nsmap).attrib['url']
        if "dummy" in data['urlToImage']:
            data['urlToImage'] = "./img/firstpostLogo.jpg"
        mainData['articles'].append(data)
except:
    print("Error in fp-business")

try:
    response = requests.get('http://feeds.feedburner.com/ndtvprofit-latest')
    root = etree.fromstring(response.content)
    for newsItem in root.iter('item'):
        data = {}
        data['title'] = newsItem.find('title').text+'(source:NDTV)'
        data['description'] =  newsItem.find('description').text
        data['url'] = newsItem.find('link').text
        data['publishedAt'] = newsItem.find('pubDate').text
        data['urlToImage'] = newsItem.find('StoryImage').text
        mainData['articles'].append(data)
except:
    print("Error in ndtv-profit",sys.exc_info())

try:
    response = requests.get('https://www.hindustantimes.com/rss/business/rssfeed.xml')
    root = etree.fromstring(response.content)
    for newsItem in root.iter('item'):
        data = {}
        data['title'] = newsItem.find('title').text+'(source:HT)'
        data['description'] =  newsItem.find('description').text
        data['url'] = newsItem.find('link').text
        data['publishedAt'] = newsItem.find('pubDate').text
        data['urlToImage'] = newsItem.find('media:content',newsItem.nsmap).attrib['url']
        mainData['articles'].append(data)
except:
    print("Error in HT-Business",sys.exc_info())
newsObj['news'].append(mainData)

mainData = {"status": "ok","articles":[]}
print("Business done!")

try:
    response = requests.get('https://www.filmfare.com/news/bollywood')
    soup = BeautifulSoup(response.content,'html.parser')
    trending = soup.find_all(class_='news-section')
    trending_html = list(trending)
    for item in trending_html:
        data = {}
        section = list(item.children)
        figureList = list(section[1].children) 
        mainContent = str(figureList[1].contents[1])
        mySoup = BeautifulSoup(mainContent,'html.parser')
        for a in mySoup.find_all('a', href=True):
            for img in mySoup.find_all('img'):
                data['urlToImage'] = img['data-original']
                data['url'] = a['href']
                data['title'] =a['title']
                mainData['articles'].append(data)
except:
    print("Error in PinkVilla",sys.exc_info())

try:
    response = requests.get('https://www.filmfare.com/news/hollywood')
    soup = BeautifulSoup(response.content,'html.parser')
    trending = soup.find_all(class_='news-section')
    trending_html = list(trending)
    for item in trending_html:
        data = {}
        section = list(item.children)
        figureList = list(section[1].children) 
        mainContent = str(figureList[1].contents[1])
        mySoup = BeautifulSoup(mainContent,'html.parser')
        for a in mySoup.find_all('a', href=True):
            for img in mySoup.find_all('img'):
                data['urlToImage'] = img['data-original']
                data['url'] = a['href']
                data['title'] =a['title']
                mainData['articles'].append(data)
except:
    print("Error in PinkVilla-HollyWood",sys.exc_info())

try:
    response = requests.get('http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml')
    root = etree.fromstring(response.content)
    for newsItem in root.iter('item'):
        data = {}
        data['title'] = newsItem.find('title').text+'(source:BBC)'
        data['description'] = newsItem.find('description').text
        data['url'] = newsItem.find('link').text
        data['publishedAt'] = newsItem.find('pubDate').text
        imageUrl = data['url']
        image = "./img/BBCLogo.jpg"
        page = requests.get(imageUrl)
        soup = BeautifulSoup(page.content, 'lxml')
        html = list(soup.children)[1]
        l = soup.find_all('span', class_='image-and-copyright-container')
        if len(l)>0:
            content=str(l[0])
            src_index = content.index("src=")+5
            jpg_index = content.index("\"",src_index)
            image = content[src_index:jpg_index]
        data['urlToImage'] = image
        mainData['articles'].append(data)
except:
    print('Error in BBC-Entertaiment',sys.exc_info())


try:
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    response = requests.get('https://www.hindustantimes.com/rss/entertainment/rssfeed.xml',headers=headers)
    root = etree.fromstring(response.content)
    for newsItem in root.iter('item'):
        data = {}
        data['title'] = newsItem.find('title').text+'(source:HT)'
        data['description'] =  newsItem.find('description').text
        data['url'] = newsItem.find('link').text
        data['publishedAt'] = newsItem.find('pubDate').text
        data['urlToImage'] = newsItem.find('media:content',newsItem.nsmap).attrib['url']
        mainData['articles'].append(data)

except:
    print("Error in HT-Entertainment")

try:
    response = requests.get('http://rss.cnn.com/rss/edition_entertainment.rss')
    root = etree.fromstring(response.content)
    for newsItem in root.iter('item'):
        data = {}
        data['title'] = newsItem.find('title').text+'(source:CNN)'
        data['url'] = newsItem.find('link').text
        data['publishedAt'] = newsItem.find('pubDate').text
        photo = list(newsItem.find('media:group',newsItem.nsmap))[0]
        data['urlToImage'] = photo.get('url')
        description = newsItem.find('description').text
        data['description'] = description[0:description.index('<')]
        mainData['articles'].append(data)
except:
    print("Error in cnn-entertainment",sys.exc_info())

newsObj['news'].append(mainData)

print('Entertainment done!!')

mainData = {"status": "ok","articles":[]}
try:
    response = requests.get('https://www.who.int/rss-feeds/news-english.xml')
    root = etree.fromstring(response.content)
    for newsItem in root.iter('item'):
        data = {}
        data['title'] = newsItem.find('title').text+'(source:WHO)'
        data['url'] = newsItem.find('link').text
        data['publishedAt'] = newsItem.find('pubDate').text
        mainData['articles'].append(data)

except:
    print('Error in WHO',sys.exc_info())

try:
    response = requests.get('https://health.economictimes.indiatimes.com/rss/topstories')
    root = etree.fromstring(response.content)
    for newsItem in root.iter('item'):
        data = {}
        data['title'] = newsItem.find('title').text+'(source:ET)'
        data['url'] = newsItem.find('link').text
        data['publishedAt'] = newsItem.find('pubDate').text
        data['description'] = newsItem.find('description').text
        data['urlToImage'] = newsItem.find('image').attrib['src']
        mainData['articles'].append(data)

except:
    print('Error in ET-Health',sys.exc_info())

try:
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    response = requests.get('https://medicalxpress.com/rss-feed/',headers=headers)
    print(response)
    root = etree.fromstring(response.content)
    for newsItem in root.iter('item'):
        data = {}
        data['title'] = newsItem.find('title').text+'(source:Medicalxpress)'
        data['url'] = newsItem.find('link').text
        data['publishedAt'] = newsItem.find('pubDate').text
        data['description'] = newsItem.find('description').text
        data['urlToImage'] = newsItem.find('media:thumbnail',newsItem.nsmap).attrib['url']
        mainData['articles'].append(data)

except:
    print('Error in ET-Health',sys.exc_info())


newsObj['news'].append(mainData)
print('Health done!!')

mainData = {"status": "ok","articles":[]}

try:
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    response = requests.get('https://www.sciencedaily.com/rss/all.xml',headers=headers)
    root = etree.fromstring(response.content)
    for newsItem in root.iter('item'):
        data = {}
        data['title'] = newsItem.find('title').text+'(source:Science Daily)'
        data['url'] = newsItem.find('link').text
        data['publishedAt'] = newsItem.find('pubDate').text
        data['description'] = newsItem.find('description').text
        mainData['articles'].append(data)

except:
    print('Error in Science Daily',sys.exc_info())

try:
    response = requests.get('https://www.wired.com/category/science/feed')
    root = etree.fromstring(response.content)
    for newsItem in root.iter('item'):
        data = {}
        data['title'] = newsItem.find('title').text+'(source:Wired)'
        data['url'] = newsItem.find('link').text
        data['publishedAt'] = newsItem.find('pubDate').text
        data['description'] = newsItem.find('description').text
        data['urlToImage'] = newsItem.find('media:thumbnail',newsItem.nsmap).attrib['url']
        mainData['articles'].append(data)

except:
    print('Error in Wired',sys.exc_info())

try:
    response = requests.get('https://www.eurekalert.org/rss.xml')
    root = etree.fromstring(response.content)
    for newsItem in root.iter('item'):
        data = {}
        data['title'] = newsItem.find('title').text+'(source:Eurekalert)'
        data['url'] = newsItem.find('link').text
        data['publishedAt'] = newsItem.find('pubDate').text
        data['description'] = newsItem.find('description').text
        mainData['articles'].append(data)

except:
    print('Error in Eurekalert',sys.exc_info())

try:
    response = requests.get('https://feeds.newscientist.com/')
    root = etree.fromstring(response.content)
    for newsItem in root.iter('item'):
        data = {}
        data['title'] = newsItem.find('title').text+'(source:New Scientist)'
        data['url'] = newsItem.find('link').text
        data['publishedAt'] = newsItem.find('pubDate').text
        data['description'] = newsItem.find('description').text
        mainData['articles'].append(data)

except:
    print('Error in New Scientist',sys.exc_info())

newsObj['news'].append(mainData)
print('Science done!!')

mainData = {"status": "ok","articles":[]}

try:
    response = requests.get('https://www.wired.com/feed/rss')
    root = etree.fromstring(response.content)
    for newsItem in root.iter('item'):
        data = {}
        data['title'] = newsItem.find('title').text+'(source:Wired)'
        data['url'] = newsItem.find('link').text
        data['publishedAt'] = newsItem.find('pubDate').text
        data['description'] = newsItem.find('description').text
        data['urlToImage'] = newsItem.find('media:thumbnail',newsItem.nsmap).attrib['url']
        mainData['articles'].append(data)

except:
    print('Error in Wired',sys.exc_info())

try:
    response = requests.get('https://www.techrepublic.com/rssfeeds/articles/')
    root = etree.fromstring(response.content)
    for newsItem in root.iter('item'):
        data = {}
        data['title'] = newsItem.find('title').text+'(source:Tech Republic)'
        data['url'] = newsItem.find('link').text
        data['publishedAt'] = newsItem.find('pubDate').text
        data['description'] = newsItem.find('description').text
        mainData['articles'].append(data)

except:
    print('Error in Tech Republic',sys.exc_info())

try:
    response = requests.get('https://www.zdnet.com/news/rss.xml')
    root = etree.fromstring(response.content)
    for newsItem in root.iter('item'):
        data = {}
        data['title'] = newsItem.find('title').text+'(source:ZDnet)'
        data['url'] = newsItem.find('link').text
        data['publishedAt'] = newsItem.find('pubDate').text
        data['description'] = newsItem.find('description').text
        mainData['articles'].append(data)

except:
    print('Error in ZDNet',sys.exc_info())

try:
    response = requests.get('https://www.buzzfeed.com/tech.xml')
    root = etree.fromstring(response.content)
    for newsItem in root.iter('item'):
        data = {}
        data['title'] = newsItem.find('title').text+'(source:BuzzFeed)'
        data['url'] = newsItem.find('link').text
        data['publishedAt'] = newsItem.find('pubDate').text
        data['description'] = newsItem.find('description').text
        data['urlToImage'] = newsItem.find('media:thumbnail',newsItem.nsmap).attrib['url']
        mainData['articles'].append(data)

except:
    print('Error in BuzzFeed',sys.exc_info())

try:
    response = requests.get('https://www.engadget.com/rss.xml')
    root = etree.fromstring(response.content)
    for newsItem in root.iter('item'):
        data = {}
        data['title'] = newsItem.find('title').text+'(source:Engadget)'
        data['url'] = newsItem.find('link').text
        data['publishedAt'] = newsItem.find('pubDate').text
        description = newsItem.find('description').text
        src_index = description.index("src=")+5
        jpg_index = description.index("\"",src_index)
        p_start_index = description.index(">")+1
        data['description'] = unidecode.unidecode(description[p_start_index:])
        data['urlToImage'] = description[src_index:jpg_index]
        mainData['articles'].append(data)

except:
    print('Error in Engadget',sys.exc_info())

newsObj['news'].append(mainData)
print('Tech done!!')
mainData = {"status": "ok","articles":[]}

try:
    response = requests.get('https://sports.ndtv.com/rss/all')
    root = etree.fromstring(response.content)
    for newsItem in root.iter('item'):
        data = {}
        data['title'] = newsItem.find('title').text+'(source:NDTV)'
        data['url'] = newsItem.find('link').text
        data['publishedAt'] = newsItem.find('a10:updated',newsItem.nsmap).text
        data['description'] = newsItem.find('description').text
        mainData['articles'].append(data)

except:
    print('Error in NDTV',sys.exc_info())

try:
    response = requests.get('https://www.espn.com/espn/rss/news')
    root = etree.fromstring(response.content)
    for newsItem in root.iter('item'):
        data = {}
        data['title'] = newsItem.find('title').text+'(source:ESPN)'
        data['url'] = newsItem.find('link').text
        data['publishedAt'] = newsItem.find('pubDate').text
        data['description'] = newsItem.find('description').text
        data['urlToImage'] = newsItem.find('image').text
        mainData['articles'].append(data)
except:
    print('Error in ESPN',sys.exc_info())

try:
    response = requests.get('https://timesofindia.indiatimes.com/rssfeeds/4719148.cms')
    root = etree.fromstring(response.content)
    for newsItem in root.iter('item'):
        data = {}
        data['title'] = newsItem.find('title').text+'(source:TOI)'
        data['url'] = newsItem.find('link').text
        data['publishedAt'] = newsItem.find('pubDate').text
        description = newsItem.find('description').text
        start_index = description.index("a>")+2
        image_start = description.index("src=")+5
        image_end = description.index("\"",image_start)
        data['description'] = description[start_index:]
        data['urlToImage'] = description[image_start:image_end]
        mainData['articles'].append(data)
except:
    print('Error in TOI',sys.exc_info())

try:
    response = requests.get('https://zeenews.india.com/rss/sports-news.xml')
    root = etree.fromstring(response.content)
    for newsItem in root.iter('item'):
        data = {}
        data['title'] = newsItem.find('title').text+'(source:ZeeNews)'
        data['url'] = newsItem.find('link').text
        data['publishedAt'] = newsItem.find('pubDate').text
        description = newsItem.find('description').text
        start_index = description.index("a>")+2
        image_start = description.index("src=")+5
        image_end = description.index("\"",image_start)
        data['description'] = description[start_index:]
        data['urlToImage'] = description[image_start:image_end]
        mainData['articles'].append(data)
except:
    print('Error in Zee-Sports',sys.exc_info())


newsObj['news'].append(mainData)
print('Sports done!!')

mainData = {"status": "ok","articles":[]}

try:
    response = requests.get('http://feeds.feedburner.com/ndtvnews-offbeat-news')
    root = etree.fromstring(response.content)
    for newsItem in root.iter('item'):
        data = {}
        data['title'] = newsItem.find('title').text+'(source:NDTV)'
        data['url'] = newsItem.find('link').text
        data['publishedAt'] = newsItem.find('pubDate').text
        description = newsItem.find('description').text
        data['description'] = unidecode.unidecode(description)
        data['urlToImage'] = newsItem.find('fullimage').text
        mainData['articles'].append(data)
except:
    print('Error in NDTV Offbeat',sys.exc_info())

try:
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    response = requests.get('https://www.sciencedaily.com/rss/strange_offbeat.xml',headers=headers)
    root = etree.fromstring(response.content)
    for newsItem in root.iter('item'):
        data = {}
        data['title'] = newsItem.find('title').text+'(source:ScienceDaily)'
        data['url'] = newsItem.find('link').text
        data['publishedAt'] = newsItem.find('pubDate').text
        description = newsItem.find('description').text
        data['description'] = unidecode.unidecode(description)
        mainData['articles'].append(data)
except:
    print('Error in Science-Daily-Offbeat',sys.exc_info())

newsObj['news'].append(mainData)
print('Offbeat done!!')
'''
# print(list(mainContent.children))
# print(newsObj)
#print(json.dumps(newsObj))
json_data = json.dumps(newsObj)
msg = r.get("msg:hello")
print(msg)
# r.set("all_news",json_data)
msg2 = r.get("all_news")
data=json.loads(msg2)
print(data)
# off = data["news"][0]["articles"]
# print(off)
# print("-------")
# print(dumps(off))