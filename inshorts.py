import requests
from bs4 import BeautifulSoup


def getNews(category):

    newsDictionary = {

    'success': True,
        'category': category,
        'data': []

    }


    try:
        if category != 'all':
            htmlBody = requests.get(
                'https://www.inshorts.com/en/read/' + category)
        else:
            htmlBody = requests.get('https://www.inshorts.com/en/read/')

    except requests.exceptions.RequestException as e:
        newsDictionary['success'] = False
        newsDictionary['error'] = str(e.message)
        return newsDictionary
    
    soup = BeautifulSoup(htmlBody.content, 'html.parser')
    elements = soup.findAll('div', class_='news-card z-depth-1')


    for i in elements:
        
        try:
            title = i.find('div', class_='news-card-title news-right-box').find('span').text
            print(title)
        except AttributeError:
            author = None

        try:
            author = i.find('div', class_='news-card-title news-right-box').find('span',class_="author").text
            print(author)
        except AttributeError:
            author = None

        try:
            time = i.find('div', class_='news-card-title news-right-box').find('span',class_="time").text
            print(time)
        except AttributeError:
            time = None

        try:
            date = i.find('div', class_='news-card-title news-right-box').find('span',clas="date").text
            print(date)

        except AttributeError:
            date = None

        try:
            content = i.find('div' , class_="news-card-content news-right-box").find('div').text
            print(content)
        
        except AttributeError:
            content = None
        

        try:
            readMoreUrl = i.find(class_='read-more').find('a').get('href')
            print(readMoreUrl)
        except AttributeError:
            readMoreUrl = None

        
        try:
            imageUrl = i.find(class_='news-card-image')['style'].split("'")[1]
        except AttributeError:
                imageUrl = None

        print("\n")





        newsObject = {
                # 'id': uuid.uuid4().hex,
                'title': title,
                'imageUrl': imageUrl,
                'url': readMoreUrl,
                'content': content,
                'author': author,
                'date': date,
                'time': time,
                'readMoreUrl': readMoreUrl
            }
        

        newsDictionary['data'].append(newsObject)

    return(newsDictionary)

    