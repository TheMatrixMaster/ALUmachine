# NLTK removing stopwords
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import requests
from bs4 import BeautifulSoup
from googlesearch import search
from cleaner import Cleaner
import html2text

#nltk.download('stopwords')
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')

def extract_NN(sent):
    grammar = r"""
    NBAR:
        # Nouns and Adjectives, terminated with Nouns
        {<NN.*>*<NN.*>}

    NP:
        {<NBAR>}
        # Above, connected with in/of/etc...
        {<NBAR><IN><NBAR>}
    """
    chunker = nltk.RegexpParser(grammar)
    ne = []
    chunk = chunker.parse(nltk.pos_tag(nltk.word_tokenize(sent)))
    for tree in chunk.subtrees(filter=lambda t: t.label() == 'NP'):
        ne.append(' '.join([child[0] for child in tree.leaves()]))
    return ne


example_sent = "Computer vision can be used to accurately diagnose lung cancers."
chunks = extract_NN(example_sent)

query_word = chunks[0]
urls = search(query_word, tld='com', lang='en', num=5, stop=5, pause=2)

h = html2text.HTML2Text()
h.ignore_links = True

webscraped_text = """"""

for url in urls:
	webpage = requests.get(url)
	soup = BeautifulSoup(webpage.text, 'html.parser')
	raw_txt = h.handle(soup.prettify())
	webscraped_text += raw_txt

webscraped_text = Cleaner(webscraped_text)