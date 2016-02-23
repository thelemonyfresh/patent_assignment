"""Compile lists of top assignors, assignees, and top title keywords from USPTO patent assignment data.

Usage: python patent_assignment.py [FILE PATH]

USPTO patent assignment data is available every day form Reed Tech (http://trademarks.reedtech.com/assignment.php). This script accepts one of these daily XML files, and prints the top assignors, top assignees, and words that appear most frequently in the patent titles (excluding a list of patent-specific and common English stop words.
"""

import nltk
from nltk.probability import FreqDist
import xml.etree.ElementTree as ET
import sys
import re
from nltk.corpus import stopwords

# list of patent-specific stop words
patent_stopwords = ['including','includes','included','instead','made','occurs','part','relates','resulting','section','things','thus','together','way','without','may','embodiment','first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth','one','two','three','four','five','six','seven','eight','nine','ten','include','comprising', 'according','comprises','least','wherein','present','end','arranged','elements','also','provided','arrangement','addition','another','away','either','following','takes','description','furthermore','specify','typical','system','method','invention','claim','claims','accordance','according','corresponding','diagram','associated','shown','known','art','relevant','additionally','accordingly','upon','actual','alternative','alternate','depicting','depicted','described','description','example','corresponds','specific','utilize','utilizing','become','allows','configuration','configured','configures','established','explained','functionality','incorporated','incorporates','many','whether','assigned','determine','illustrating','providing','provide','provides','requiring','alternatively','describes','features','feature','hereby','provide','provides','providing','typical','typically','illustrative','illustrate','skilled','plurality','within','additional','various','still','type','variety','implemented','requires','use','desired','however','necessary','understood','detailed','moreover','therein','throughout','would','generally','using','given','might','capable','said','apparatus','methods','systems','system','process','device','devices','high','structure','low','multiple','improve','improved']

path = sys.argv[1]

# parse xml file into ElementTree
asstree = ET.parse(path)
assroot = asstree.getroot()

# initialize FreqDist of most frequent assignors, assignees, and compile string of patent titles for ASSIGNMENT actions only
assignors_freqdist = FreqDist()
assignees_freqdist = FreqDist()

# initialize dictionaries to save patent titles from each assignee/assignor
assignees_dict = {}
assignors_dict = {}

# initialize string to hold all the patent titles
titles_string = ''
record = 0

# iterate through XML tree 
for child in asstree.iterfind('patent-assignments/patent-assignment'):
    record+= 1
    for subchild in child.iterfind('assignment-record/conveyance-text'):
        if subchild.text == 'ASSIGNMENT OF ASSIGNORS INTEREST (SEE DOCUMENT FOR DETAILS).':
            for subsubchild in child.iterfind('patent-assignors/patent-assignor/name'):
                assignors_freqdist[subsubchild.text] += 1
            for subsubchild in child.iterfind('patent-assignees/patent-assignee/name'):
                assignees_freqdist[subsubchild.text] += 1
                if subsubchild.text not in assignees_dict: assignees_dict[subsubchild.text]=[]
                for subsubsubchild in child.iterfind('patent-properties/patent-property/invention-title'):
                    assignees_dict[subsubchild.text].append(subsubsubchild.text)
            for subsubchild in child.iterfind('patent-properties/patent-property/invention-title'):
                titles_string += ' ' + subsubchild.text

# count most frequent tokens in patent titles
title_text = nltk.Text(nltk.word_tokenize(titles_string))

def word_count(text, exclude_inputlist):
    frequency = FreqDist(wd.lower() for wd in text if wd.isalpha())
    excludelist = stopwords.words('english') + exclude_inputlist
    for word in frequency.keys():
        if word in excludelist or frequency[word] < 2 or not word.isalpha(): frequency.pop(word)
    return frequency

wordfreq = word_count(title_text,patent_stopwords)

# print results
print 'On '+ re.sub("[^0-9]", "", path) + ' there are a total of ' + str(record) + ' assignment records.'
print '\nTop 20 assigned patent title tokens:'
for i, word in enumerate(wordfreq.keys()[:20]):
    print str(i+1)+ ". " + word
print '\nTop 20 assignees (by number of assignment records):'
for i, word in enumerate(assignees_freqdist.keys()[:20]):
    print str(i+1)+ ". " + word
print '\nTop 20 assignors (by number of assignment records):'
for i, word in enumerate(assignors_freqdist.keys()[:20]):
    print str(i+1)+ ". " + word
