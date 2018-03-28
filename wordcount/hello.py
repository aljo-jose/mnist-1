"""
Flask API
"""
import HTMLparser
from flask import Flask
app = Flask(__name__)

from werkzeug.contrib.cache import SimpleCache
cache = SimpleCache()

URL = 'https://en.wikipedia.org/wiki/Python_(programming_language)'

@app.route('/')
def hello_world():
    return 'Word counter. <br>/all to list all words ; <br> /range/x to list top x words.'

@app.route('/top')
def show_top(): 
    wordSummary = get_summary()
    return str(wordSummary[0])  
    
@app.route('/all')
def show_all():  
    wordSummary = get_summary()
    return str(wordSummary)

@app.route('/word/<thisWord>')
def show_word(thisWord):  
    wordSummary = get_summary()
    d = dict(wordSummary)
    return str(d[thisWord])

@app.route('/range/<val>')
def show_range(val):    
    wordSummary = get_summary()
    return str(wordSummary[0:int(val)])

def get_summary():
    summary_cache = cache.get('summary_cache')
    if summary_cache is None:
        print("calculate_summary called")
        obj = HTMLparser.ParagraphWordCounter(URL)
        summary_cache = obj.process()
        cache.set('summary_cache', summary_cache, timeout=5 * 60)
    return summary_cache