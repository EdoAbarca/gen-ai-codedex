from nltk import ngrams, word_tokenize

sample_text = 'I am learning NLP(Natural Language Processing)'
tokens = word_tokenize(sample_text)

# Unigram
unigrams = list(ngrams(tokens, 1))
print('Unigrams:', unigrams)

# Bigram
bigrams = list(ngrams(tokens, 2))
print('Bigrams:', bigrams)

# Trigram
trigrams = list(ngrams(tokens, 3))
print('Trigrams:', trigrams)