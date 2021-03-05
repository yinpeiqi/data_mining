from urllib.request import urlopen
from bs4 import BeautifulSoup

def query(url):
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    post_items = soup.find_all(class_="post-item")
    result_list = []
    for post_item in post_items:
        result = dict()
        result['title'] = post_item.find_all(class_="post-header")[0].a.contents[0]
        result['author'] = post_item.find_all(class_="author")[0].a.contents[0]
        result['date'] = post_item.find_all(class_="date")[0].a.contents[0]
        result_list.append(result)
    try:
        next_url = soup.find_all(class_="next-posts-link")[0]['href']
        result_list.extend(query(next_url))
    except:
        pass
    return result_list

if __name__ == '__main__':
    url = "https://blog.scrapinghub.com"
    resultSet = query(url)
    for result in resultSet:
        print(result)
    print(len(resultSet))