# Made by Kartik
flag = True
try:
    import numpy as np
    import nltk
    from nltk.stem.porter import PorterStemmer

except ModuleNotFoundError:
    print("The module named 'Numpy' or 'NLTK' not installed")
    flag = False

if flag:

    try:
        Stemmer = PorterStemmer()
    except:
        Stemmer = False
    
    def tokenize(sentence):
        """ This function taken a sentence and return a tokenized sentence. """
        return nltk.word_tokenize(sentence)

    def stem(word):
        """ This return list of word (stemmed) """
        word = str(word)
        if Stemmer == False:
            print("Warning: Stemmer not working.")
            return word.lower()
        else:
            return Stemmer.stem(word.lower())

    def bag_of_words(tokenized_sentence, words):
        """ This function creates a bagt of words for us. -> Document Vector """
        sentence_words = [stem(word) for word in tokenized_sentence]
        bag = np.zeros(len(words), dtype=np.float32)

        for id_of_word, word in enumerate(words):
            if word in sentence_words:
                bag[id_of_word] = 1

        return bag


if __name__ == '__main__':
                #   For Testing   #

    # sentence = "Kartik is a programmer. "
    # new_sentence = tokenize(sentence)
    # list1 = []
    # for i in new_sentence:
    #     a = stem(i)
    #     list1.append(a)
    #     bag = bag_of_words(new_sentence, list1)
    # print(new_sentence,"\n\n")
    # print(list1,"\n\n")
    # print(bag)
    pass
