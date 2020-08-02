import nltk
from textblob import TextBlob, Word
import pycountry

# Returns a list of spelling mistakes the user made and suggestions to correct the word
def spellingCheck(text):
	splits = text.split()
	corrections = ""
	for s in splits:
		w = Word(s)
		lst = w.spellcheck()
		if len(lst) > 1:
			altSpellings = []
			for w in lst:
				altSpellings.append(w[0])
			joinAlt = ", ".join(altSpellings)
			corrections += "Incorrect spelling of " + s + ". Did you mean: " + joinAlt + "?\n"
	if corrections == "":
		corrections = "No spelling mistakes!"
	return corrections

# Detects the language of a phrase and translates it into English.
def translatePhrase(text):
	b = TextBlob(text)
	iso = b.detect_language()
	lang = pycountry.languages.get(alpha_2=iso)
	if iso == "en":
		return "Your phrase is already in English."
	translation = b.translate(to="en")
	result = "Your original language was " + str(lang.name) + ".\nThe translated phrase is: " + str(translation)
	return result












