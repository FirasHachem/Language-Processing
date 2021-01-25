def count_ngrams(corpus_object, n):
    dict_ngrams = {}
    ngrams = []
    for line in corpus_object.readlines():
        for word in line.split():
            if len(ngrams) == n:
                ngrams = ngrams[1:] + [word]
                ngram = tuple(ngrams)
                if ngram in dict_ngrams:
                    dict_ngrams[ngram] += 1
                else:
                    dict_ngrams[ngram] = 1
            if len(ngrams) < n:
                ngrams.append(word)
                if len(ngrams) == n:
                    ngram = tuple(ngrams)
                    if ngram in dict_ngrams:
                        dict_ngrams[ngram] += 1
                    else:
                        dict_ngrams[ngram] = 1
    return dict_ngrams