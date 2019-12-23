import nltk
import string

remove_punctuation = dict(
    (ord(punctuation), None) for punctuation in string.punctuation)

lemmatizer = nltk.stem.WordNetLemmatizer()


def lammatize_words(words):
    return [lemmatizer.lemmatize(word) for word in words]


def remove_punctuations(text):
    return lammatize_words(
        nltk.word_tokenize(text.lower().translate(remove_punctuation))
    )
