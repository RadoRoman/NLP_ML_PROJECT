


def useless_code():


    df = pd.read_csv('')

    #from sklearn.feature_extraction.text import CountVectorizer

    # the vectorizer object will be used to transform text to vector form
    vectorizer = CountVectorizer(max_df=0.9, min_df=25, token_pattern='\w+|\$[\d\.]+|\S+')


    # apply transformation
    tf = vectorizer.fit_transform(df['clean_tweet']).toarray()

    # tf_feature_names tells us what word each column in the matric represents
    tf_feature_names = vectorizer.get_feature_names()

    #from sklearn.decomposition import LatentDirichletAllocation
    number_of_topics = 10

    model = LatentDirichletAllocation(n_components=number_of_topics, random_state=0)
    model.fit(tf)


    def display_topics(model, feature_names, no_top_words):
        topic_dict = {}
        for topic_idx, topic in enumerate(model.components_):
            topic_dict["Topic %d words" % (topic_idx)]= ['{}'.format(feature_names[i])
                            for i in topic.argsort()[:-no_top_words - 1:-1]]
            topic_dict["Topic %d weights" % (topic_idx)]= ['{:.1f}'.format(topic[i])
                            for i in topic.argsort()[:-no_top_words - 1:-1]]
        return pd.DataFrame(topic_dict)


    #display_topics(model, tf_feature_names, no_top_words)

    df = pd.read_csv('')


import regex as re
import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
import gensim
from gensim import corpora
nltk.download('wordnet')
nltk.download('omw-1.4')

def importing_Lyrics_df():
    df = pd.read_csv('azlyrics-scraper/azlyrics_lyrics_19.csv',on_bad_lines='skip')
    return df

def pre_processing(text):
    stop_list = []
    stop_list.extend(stopwords.words('english'))
    stop_list.extend(
        ['yo','dont','nigga','uh', 'got', 'oh', 'im', 'na', 'from', 'subject', 're', 'edu', 'use', 'not', 'would', 'say', 'could', '_', 'be',
         'know', 'good', 'go', 'get', 'ah', 'bout','yeah','le','ayy','u','bitch','eh','wa',
         'do', 'done', 'try', 'many', 'some', 'nice', 'thank', 'think', 'see', 'rather', 'easy', 'easily', 'lot',
         'lack', 'make', 'want', 'seem', 'run', 'need', 'even', 'right', 'line', 'even', 'also', 'may', 'take', 'come'])
    exclude = set(string.punctuation)
    lemma = WordNetLemmatizer()

    text = text.rstrip()
    normalized = " ".join(lemma.lemmatize(i) for i in text.split())
    punc_free = ''.join(i for i in normalized if i not in exclude)
    stop_free = " ".join([i for i in punc_free.lower().split() if((i not in stop_list) and (not i.isdigit()))])
    return stop_free


def modelling(clean_text):
    dictionary = corpora.Dictionary(clean_text)
    corpus = [dictionary.doc2bow(text) for text in text_clean]
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=5, id2word=dictionary, passes=5)
    topics = ldamodel.print_topics(num_words=5)
    return (dictionary, corpus, ldamodel, topics)


#Importing the CSV file
df = importing_Lyrics_df()


#Cleaning the data
text_clean=[]
for text in df['LYRICS']:
    text_clean.append(pre_processing(text).split())

#Modelling
dictionary, corpus, ldamodel, topics = modelling(text_clean)
for topic in topics:
    print(topic)

def get_topic_details(ldamodel, corpus):
    topic_details_df = pd.DataFrame()
    for i, row in enumerate(ldamodel[corpus]):
        row = sorted(row, key=lambda x: (x[1]), reverse=True)
        for j, (topic_num, prop_topic) in enumerate(row):
            if j == 0:  # => dominant topic
                wp = ldamodel.show_topic(topic_num)
                topic_details_df = topic_details_df.append(pd.Series([topic_num, prop_topic]),
                ignore_index=True)
    topic_details_df.columns = ['Dominant_Topic', '% Score']
    return topic_details_df

contents = pd.DataFrame({'Original Text': text_clean})
topic_details = pd.concat([get_topic_details(ldamodel, corpus), contents], axis=1)

# Create flag for text highest associated with topic 3
dom_tp = topic_details['Dominant_Topic']
topic_details['flag'] = np.where((dom_tp == 2.0) | (dom_tp == 3.0) | (dom_tp == 4.0), 1, 0)
print(topic_details.head())

