import pycountry
from textblob import TextBlob, Word


# Returns a list of spelling mistakes the user made and suggestions to correct the word
def spellingCheck(text):
    splits = text.split()
    corrections = []
    for s in splits:
        w = Word(s.lower())
        lst = w.spellcheck()
        if len(lst) > 1:
            altSpellings = []
            for w in lst:
                altSpellings.append(w[0])
            joinAlt = ", ".join(altSpellings)
            corrections.append("Incorrect spelling of " + s + ". Did you mean: " + joinAlt + "?")
    if len(corrections) == 0:
        corrections.append("No spelling mistakes!")
    return corrections


# Detects the language of a phrase and translates it into English.
def translatePhrase(text):
    b = TextBlob(text)
    iso = b.detect_language()
    lang = pycountry.languages.get(alpha_2=iso)
    if iso == "en":
        return "Your phrase is already in English."
    translation = b.translate(to="en")
    result = {"Your original language was": str(lang.name),
              "The translated phrase is": str(translation)}
    return result


if __name__ == '__main__':
    text = """This course deals with networking and machine
    learning technologies underlying activities of markets,
    institutions and participants. The overall purpose is to give
    students a working under-standing of a wide variety of the
    technological tools that permeate modern life. The successful
    student will be able to extend this knowledge, understand systems
    currently in place and use new developments in the field as they
    are created.
    Meetings will be in person / streamed on Canvas, once per week.
    Recordings of these lectures will also be available online
    through Canvas. Lectures will focus on either understanding or
    implementing some element of technology. As this course is being
    given as both an in person and an online class, use of the
    discussion boards on Canvas for questions and answers is highly
    encouraged."""
    print(spellingCheck(text))

    frtext = """Ce cours traite des technologies de réseautage et 
    d'apprentissage automatique sous-jacentes aux activités des marchés, 
    des institutions et des participants. L'objectif général est de 
    donner aux étudiants une compréhension de travail d'une grande 
    variété d'outils technologiques qui imprègnent la vie moderne. 
    L'étudiant retenu sera capable d'approfondir ses connaissances, 
    de comprendre les systèmes actuellement en place et d'utiliser 
    les nouveaux développements dans le domaine au fur et à mesure 
    de leur création. 
    Les réunions seront en personne / diffusées sur Canvas, 
    une fois par semaine. Les enregistrements de ces conférences 
    seront également disponibles en ligne sur Canvas. Les conférences 
    porteront sur la compréhension ou la mise en œuvre d'un élément 
    de la technologie. Comme ce cours est donné à la fois en personne 
    et en ligne, l'utilisation des forums de discussion sur Canvas 
    pour les questions et réponses est fortement encouragée."""
    print(translatePhrase(frtext))