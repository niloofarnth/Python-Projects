from time import sleep
import urllib
import requests
from bs4 import BeautifulSoup

#function for finding the first link in each wikipedia page
def find_first_link(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html,'html.parser' )
    #finding the body paragraph in the wikipedia page with two div tags
    content_div = soup.find(id='mw-content-text').find(class_="mw-parser-output")
    # put the first link to None in case there is no link in the page
    first_link = None
    #recursive = False only gives the direct children of the content_div paragraph
    for element in content_div.find_all("p", recursive=False):
        if element.find("a", recursive=False):
            first_link = element.find("a", recursive=False).get('href')
        break
        if not first_link:
            print ("there is no link in the last article")
            
    first_link_complete = urllib.parse.urljoin('https://en.wikipedia.org/',first_link)
    return first_link_complete


#function for a set of rules to continue crawling    
def continue_crawl(article_chain, target_url, max_steps = 25):
    if article_chain[-1] == target_url:
        answer =  False
        print ("your search has reached to the philosophy page")
    elif len(article_chain)>max_steps :
        print ("the length of the search is more than {} urls".format(max_steps))
        answer =  False
    elif article_chain[-1] in article_chain[:-1]:
        print("Your search has entered a cycle")
        answer =  False
    else:
        answer =  True
    return answer
    

#main function
def web_crawl(article_chain, target_url, max_steps = 25):
    #set the rule for continuing the web_crawl function with the continue_crawl function
    while continue_crawl(article_chain, target_url, max_steps):
    # find the first link in that html from the find_first_link function
        first_link = find_first_link(article_chain[-1])
    # add the first link to article_chain
        article_chain.append(first_link)
        print (article_chain[-1])
    # delay for two seconds
        sleep(2)


start_url = 'https://en.wikipedia.org/wiki/Męcikał'
end_url = 'https://en.wikipedia.org/wiki/Philosophy'
web_crawl([start_url],end_url,20)
