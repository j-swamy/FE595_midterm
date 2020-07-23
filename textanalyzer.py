import nltk
from textblob import TextBlob

nltk.download('brown')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')


def get_sentiment(text):
    blob = TextBlob(text)
    return {'polarity': blob.sentiment.polarity, 'subjectivity': blob.sentiment.subjectivity}


def get_tags(text):
    blob = TextBlob(text)
    return blob.tags


if __name__ == '__main__':
    text = """This course deals with networking and machine
    learning technologies underlying activities of markets,
    institutions and participants. The overall purpose is to give
    students a working under-standing of a wide variety of the
    technological tools that permeate modern life. The successful
    student will be able to extend this knowledge, understand systems
    currently in place and use new developments in the field as they
    are created.
    Meetings will be in person/streamed on Canvas, once per week.
    Recordings of these lectures will also be available online
    through Canvas. Lectures will focus on either understanding or
    implementing some element of technology.As this course is being
    given as both an in person and an online class, use of the
    discussion boards on Canvas for questions and answers is highly
    encouraged."""
    print(get_sentiment(text))
