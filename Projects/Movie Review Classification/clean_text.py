# Converted the NLTK.ipynb to .py to access the functions in another code

from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import sys

# init Objects
tokenizer = RegexpTokenizer(r'\b\w+\b')
en_stopwords = set(stopwords.words('english'))
ps = PorterStemmer()

def getStemmedReview(review):
    review = review.lower()
    review = review.replace("<br /><br>"," ")

    #tokenize
    tokens = tokenizer.tokenize(review)
    new_tokens = [token for token in tokens if token not in en_stopwords]
    stemmed_tokens = [ps.stem(token) for token in new_tokens]

    cleaned_review = ' '.join(stemmed_tokens)

    return cleaned_review

# Accepts input file and returns clean output file of moview reviews
def getStemmedDocument(inputfile,outputfile):
    out = open(outputfile,'w',encoding="utf8")

    with open(inputfile,encoding="utf8") as f:
        reviews = f.readlines()

    for review in reviews:
        cleaned_review = getStemmedReview(review)
        print((cleaned_review),file=out)

    out.close()


# inputfile = '/workspaces/Machine_Learning_in_Python/Projects/Movie Review Classification/IMDB/imdb_trainX.txt'
# outputfile = '/workspaces/Machine_Learning_in_Python/Projects/Movie Review Classification/IMDB/imdb_trainX_output.txt'
# getStemmedDocument(inputfile,outputfile)