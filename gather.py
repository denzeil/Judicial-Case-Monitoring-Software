#import the necessary libraries
from bs4 import BeautifulSoup
import requests

#save the link to a url
url='https://news.ycombinator.com/news'

#save the data in a response variable
response=requests.get(url)

info=response.text

soup=BeautifulSoup(info,'html.parser')

#print(soup.title)
heading=soup.find(name='span',class_='titleline' )
title_name=soup.select_one(selector='span a')

article_upvote=soup.find(name='span',class_='score')

article_link=soup.find(name='a',class_='storylink')
#print(heading.getText())
#print(article_link)

article_text=[]
article_vote=[]
print(article_link)

