import nltk
def get_homographs_one_word(corpus, the_word):
    a = corpus.tagged_words()
    pos_tags = set()
    for i in range(len(a)):
        if a[i][0] == the_word:
            pos_tags.add(a[i][1])
    return pos_tags