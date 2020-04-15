#!/usr/bin/env python
# coding: utf-8

# In[57]:


#A part-of-speech tagger, or POS-tagger, processes a sequence of words, and attaches a part of speech tag to each word

from nltk.tokenize import word_tokenize
import nltk


# In[98]:


text = word_tokenize("I want to read a book. I want to book a flight")


# In[99]:


text


# In[100]:


nltk.pos_tag(text)


# In[94]:


a[1][1]


# In[ ]:


'''
'and' is CC, a coordinating conjunction;
'now' and 'completely' are RB, or adverbs; 
'for' is IN, a preposition; 
'something' is NN, a noun;
'different' is JJ, an adjective
'''


'''
POS tag list:

CC coordinating conjunction
CD cardinal digit
DT determiner
EX existential there (like: "there is" ... think of it like "there exists")
FW foreign word
IN preposition/subordinating conjunction
JJ adjective 'big'
JJR adjective, comparative 'bigger'
JJS adjective, superlative 'biggest'
LS list marker 1)
MD modal could, will
NN noun, singular 'desk'
NNS noun plural 'desks'
NNP proper noun, singular 'Harrison'
NNPS proper noun, plural 'Americans'
PDT predeterminer 'all the kids'
POS possessive ending parent's
PRP personal pronoun I, he, she
PRP$ possessive pronoun my, his, hers
RB adverb very, silently,
RBR adverb, comparative better
RBS adverb, superlative best
RP particle give up
TO to go 'to' the store.
UH interjection errrrrrrrm
VB verb, base form take
VBD verb, past tense took
VBG verb, gerund/present participle taking
VBN verb, past participle taken
VBP verb, sing. present, non-3d take
VBZ verb, 3rd person sing. present takes
WDT wh-determiner which
WP wh-pronoun who, what
WP$ possessive wh-pronoun whose
WRB wh-abverb where, when
'''


# In[97]:


#NLTK provides documentation for each tag, which can be queried using the tag. execute below code:
nltk.help.upenn_tagset('JJ')


# In[16]:


text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())


# In[17]:


text.similar('woman')


# In[43]:


'''
2.Tagged Corpora
    2.1   Representing Tagged Tokens
By convention in NLTK, a tagged token is represented using a tuple consisting of the token and the tag. 
We can create one of these special tuples from the standard string representation of a tagged token, 
using the function str2tuple():
'''


# In[44]:


tagged_token = nltk.tag.str2tuple('fly/NN')


# In[45]:


tagged_token


# In[41]:


sent = '''The/DT grand/JJ jury/NN commented/VBD on/IN a/AT number/NN of/IN
other/AP topics/NNS ,/, AMONG/IN them/PPO the/AT Atlanta/NP and/CC
Fulton/NP-tl County/NN-tl purchasing/VBG departments/NNS which/WDT it/PPS
said/VBD ``/`` ARE/BER well/QL operated/VBN and/CC follow/VB generally/RB
accepted/VBN practices/NNS which/WDT inure/VB to/IN the/AT best/JJT
interest/NN'''
[nltk.tag.str2tuple(t) for t in sent.split()]


# In[47]:


#2.2   Reading Tagged Corpora
    #Several of the corpora included with NLTK have been tagged for their part-of-speech. 
    #the Brown Corpus represents the data as shown below:


# In[55]:


#Whenever a corpus contains tagged text, the NLTK corpus interface will have a tagged_words() method
nltk.corpus.brown.tagged_words()


# In[53]:


nltk.corpus.nps_chat.tagged_words()


# In[54]:


nltk.corpus.brown.tagged_words(tagset='universal')


# In[56]:


nltk.corpus.indian.tagged_words()


# In[85]:


#2.3   A Universal Part-of-Speech Tagset


# In[75]:


#nltk.probability.FreqDist()--A frequency distribution records the number of times each outcome of an experiment has occurred
#nltk.probability.FreqDist().most_common()--Return a list of the n most common elements and their counts from the most common to the least

from nltk.corpus import brown
brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
tag_fd = nltk.FreqDist(tag for (word, tag) in brown_news_tagged)
tag_fd.most_common()

('The','DET')


# In[86]:


#ConditionalFreqDist()--Conditional frequency distributions are used to record the number of times each sample occurred, 
                        #given the condition under which the experiment was run.
#nltk.probability.ConditionalFreqDist.Conditions()-Return a list of the conditions that have been accessed for this ConditionalFreqDist. 
               #Use the indexing operator to access the frequency distribution for a given condition.


# In[ ]:





# In[ ]:





# In[ ]:




