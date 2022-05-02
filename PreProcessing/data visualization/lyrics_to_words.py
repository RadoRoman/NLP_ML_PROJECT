from typing import final
from unittest.mock import sentinel
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import pandas as pd
import seaborn as sns
from helpers import lyrics_to_words


def unique(list1):
    # intilize a null list
    unique_list = []

    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)

    return unique_list

#def main():
#stop_words = set(stopwords.words('english'))
columns = ["ARTIST_NAME", "ARTIST_URL", "SONG_NAME", "SONG_URL", "LYRICS"]
df = pd.read_csv("data/preprocessed/Lyrics.csv", usecols=columns)
df = df.dropna()
#print(df)
words = []
# iterate trought each lyric and split unique words appending the result into the words list
df = df.reset_index(drop=True)
#print(lyrics_to_words("its only one, 03, i'm from grape street, where we g-slide, sweet shay shay, would you be mine?, you know i like 'em dark skin like shay shay, got that pretty smooth skin like fay fay, i think shanini got a body like tata, she fuck with greedy 'cause he fuck her like a pornstar, freaky-deeky, heard her pussy got that voodoo, i know she gay but i done fell in love with poo poo, sex appeal like butt butt, i'm like ooh woo, go to court for a nigga like why goo, fuck around and drop some codeine in my champagne, she going in like diamond lane in the diamond lane, she going down like the motherfuckin' stock exchange, addicted like some cocaine to the campaign, i like the 'woods, kiss the motherfuckin' ashtray, one more time for poo poo, bet you i can make that ass shake, baby i can get you straight, don't act gay, fuck it, i won't interrupt you, get them stacks bae, i'm in atlanta, you know one day i'll be back bae, support my daughter may may, no back pay, if i gotta creep up on you with a masked face, or put these bitches on the blade, fuck backpage, doin' numbers like a motherfuckin' facts page, seventh letter, crooked ladder, get your facts straight, all you niggas quick to tell, it's a rat race, waste your time hating, i'ma go and rack chase, i'm from grape street, where we g-slide, sweet shay shay, would you be mine?, you know i like 'em dark skin like shay shay, got that pretty smooth skin like fay fay, i think shanini got a body like tata, she fuck with greedy 'cause he fuck her like a pornstar, freaky-deeky, heard her pussy got that voodoo, i know she gay but i done fell in love with poo poo, sex appeal like butt butt, i'm like ooh woo, go to court for a nigga like why goo, sweet lady, grape street lady, think she tryna have my baby, she know to have that sex appeal like maury, she know to always keep it trill like ba, i do her wrong but i ain't in to being sorry, my other hottie left a nigga for a flea j, he ain't rollin' with no money, he a cheapskate, oh i'm just tryna get a ticket like a sweepstakes, i love my hottie dumb thick like cheesecake, run that bitch like diddy, have you walkin' for some cheesecakes, makin' that band say i'm the man 'cause that d came, had a bitch that look like cassie workin' three blades, i got a bitch who fuck me off the syrup, booty out, smuggling something, got a porno over mookie house, she got a body on her, pockets healthy, which one look better, is it kendra, is it elthy?, i need a miracle, might ask the lord to help me, she a project bitch but look hella clean, just a couple up-and-comers that be on the scene, fuck her once under the covers like a bone meat, got her wishin' it was some way she could clone me, i'ma just pull up somewhere up the road, she's really lonely, i'm from grape street, where we g-slide, sweet shay shay, would you be mine?, you know i like 'em dark skin like shay shay, got that pretty smooth skin like fay fay, i think shanini got a body like tata, she fuck with greedy 'cause he fuck her like a pornstar, freaky-deeky, heard her pussy got that voodoo, i know she gay but i done fell in love with poo poo, sex appeal like butt butt, i'm like ooh woo, go to court for a nigga like why goo, i like all the hotties with the colors in their hair, tats on they face with the buds in they ear, p-i-m-p, come and fuck with a player, bang my whole gang and you know i won't care, at all, at all, at all, watch a young nigga, ball, ball, ball, ayy, ayy, ayy, only who i'm missin'?, oh, can't forget nae nae, she thick as a bull, gigi she had all that ass, i ain't really seen her too much after the baby, but you see what was goin' on, haha, they say pooka got it in, they don't talk about how, why, when, and where, hahaha, hey, hey, if you from the jordan downs then come over there, whoa whoa whoa, too many hotties in my section, i want 'em all, call me greedy 'cause i want 'em all, call me greedy 'cause i want 'em all, i get gigi 'cause i wanna ball, take a project bitch off"))

for word in df['LYRICS'].tolist():
    words.append(unique(lyrics_to_words(word).split()))
#print(words)
# create the new column with the information of words lists
df['words'] = words
df.to_csv("data/preprocessed/Lyrics.csv", index=False)


#print(df)
    #print(my_file["LYRICS"])

    # lyrics = my_file["LYRICS"].to_string()
    # sentences = sent_tokenize(lyrics)
    # final_list = []
    # for sentence in sentences:
    #     word_list = word_tokenize(sentence)
    #     filtered_word_list = [w for w in word_list if not w in stop_words and w.isalpha()]
    #     for word in filtered_word_list:
    #         final_list.append(word)
    # #print(len(final_list))
    #
    # sns.set_style('darkgrid')
    # nlp_words = nltk.FreqDist(final_list)
    # nlp_words.plot(10)

# if __name__ == '__main__':
#     main()
