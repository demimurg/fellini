import nltk

nltk.download("stopwords")

en_stop = nltk.corpus.stopwords.words("english")
ru_stop = nltk.corpus.stopwords.words("russian")

for name, words in zip(("stopwords_en", "stopwords_ru"), (en_stop, ru_stop)):
    f = open(f"./datasets/{name}.txt", "w")
    f.write("\n".join(words))
    f.close()