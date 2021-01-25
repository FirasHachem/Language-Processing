import nltk
from collections import Counter
from nltk.probability import ConditionalFreqDist
def build_tagger(corpus):
    a = []
    taz = []
    lip = []
    for toks, tag in corpus.tagged_words():
        if toks not in lip:     #changing first occurance to unk with tag
            a.append("<UNK>")
            taz.append(("<UNK>",tag))
            lip.append(toks)
        else :                
            taz.append((toks, tag)) #if not the first time start the count
            a.append(toks)
    zip1 = nltk.ConditionalFreqDist(taz)   #zip to store tokens and tags
    ac = Counter(a)
    for toks, tag in taz:
        zip1[toks][tag] = zip1[toks][tag] + 1 
    ck = max(dict(zip1["<UNK>"]).items(), key=lambda item: item[1])[0]
    cor = dict((toks, zip1[toks].max()) for (toks) in ac.keys())
    tagger = nltk.UnigramTagger(model=cor, backoff=nltk.DefaultTagger(ck))
    return tagger