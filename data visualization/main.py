from typing import final
from unittest.mock import sentinel
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    stop_words = (stopwords.words('english'))
    stop_words.extend(['yo','got','oh','na','from', 'subject', 're', 'edu', 'use', 'not', 'would', 'say', 'could', '_', 'be', 'know', 'good', 'go', 'get',
         'do', 'done', 'try', 'many', 'some', 'nice', 'thank', 'think', 'see', 'rather', 'easy', 'easily', 'lot',
         'lack', 'make', 'want', 'seem', 'run', 'need', 'even', 'right', 'line', 'even', 'also', 'may', 'take', 'come'])
    columns = ["ARTIST_NAME", "LYRICS"]
    my_file = pd.read_csv("data/preprocessed/Lyrics.csv", usecols=columns)

    lyrics = my_file["LYRICS"].to_string()
    sentences = sent_tokenize(lyrics)
    #print(sentences)
    final_list = []
    for sentence in sentences:
        word_list = word_tokenize(sentence)
        filtered_word_list = [w for w in word_list if not w in stop_words and w.isalpha()]
        for word in filtered_word_list:
            final_list.append(word)
    with open("data/processed/words.txt", "w") as f:
        f.write(str(final_list))


    sns.set_style('darkgrid')
    #nlp_words = nltk.FreqDist(final_list).most_common(20)
    #nlp_words.plot(20, kind='bar')

    ## Creating FreqDist for whole BoW, keeping the 20 most common tokens
    all_fdist = nltk.FreqDist(final_list).most_common(20)

    ## Conversion to Pandas series via Python Dictionary for easier plotting
    all_fdist = pd.Series(dict(all_fdist))

    ## Setting figure, ax into variables
    fig, ax = plt.subplots(figsize=(10, 10))

    all_fdist.plot(kind='bar', ax=ax)
    plt.tight_layout()
    plt.show()
    #plt.savefig('some file name.png')

if __name__ == '__main__':
    main()
