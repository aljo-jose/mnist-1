"""
Created on Tue Mar 27 13:08:51 2018
@author: S425510
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from collections import Counter

class ParagraphWordCounter:
    def __init__(self,url):
        self.url =url
        self.wordCounter = Counter()
    # Download webpage.
    def download(self):
        urlReader = urlopen(self.url)
        html = urlReader.read()
        urlReader.close()
        return html
       
    def getWordCount(self, html):
        soup = bs(html)
        all_paragraphs = soup.find_all("p")       
        for p in all_paragraphs:           
            self.wordCounter.update(p.text.strip().split(' '))
        self.wordCounter = self.wordCounter.most_common()
        return self.wordCounter
    
    def process(self):       
        html = self.download()
        return(self.getWordCount(html))        
        
 
obj = ParagraphWordCounter('https://en.wikipedia.org/wiki/Python_(programming_language)')
s = obj.process()
