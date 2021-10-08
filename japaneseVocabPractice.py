#Japanese practice generatorimport random
from japaneseVocabList import nounsEng, nounsNihongo, adjectivesEng, adjectivesNihongo, hiraganaConsonantStandard, hiraganaVowel, hiraganaConsonantAlt, particlesAndPrepositionsEng, particlesAndPrepositionsNihongo, adverbsEng, adverbsNihongo, posNeg, verbsEng, verbsNihongo
import random

def hiraganaAndKatakana(a):
    if a<5:
        for i in range(5):
            print((random.choice(hiraganaVowel)) + ", " + (random.choice(hiraganaConsonantStandard)) + ", " + (random.choice(hiraganaConsonantAlt)))
    else:
        for i in range(a):
            print((random.choice(hiraganaVowel)) + ", " + (random.choice(hiraganaConsonantStandard)) + ", " + (random.choice(hiraganaConsonantAlt)))

def verbs(b):
    if b<5:
        for i in range(5):
            print((random.choice(posNeg)) + " " + (random.choice(verbsEng)))
            print(random.choice(verbsNihongo))
    else:
        for i in range(b):
            print((random.choice(posNeg)) + " " + (random.choice(verbsEng)))
            print(random.choice(verbsNihongo))

def nouns(c):
    if c<5:
        for i in range(5):
            print((random.choice(nounsEng)) + ", " + (random.choice(nounsNihongo)))
    else:
        for i in range(c):
            print((random.choice(nounsEng)) + ", " + (random.choice(nounsNihongo)))

def auxWords(d):
    if d<5:
        for i in range(5):
            print((random.choice(auxWordsNihongo)))
    else:
        for i in range(d):
            print((random.choice(auxWordsNihongo)))

def particlesAndPrepositions(e):
    if e<5:
        for i in range(5):
            print((random.choice(particlesAndPrepositionsEng)) + ", " + (random.choice(particlesAndPrepositionsNihongo)))
    else:
        for i in range(e):
            print((random.choice(particlesAndPrepositionsEng)) + ", " + (random.choice(particlesAndPrepositionsNihongo)))

def naAdjectives(f):
    if f<5:
        for i in range(5):
            print((random.choice(naAdjectives)) + ", " + (random.choice(naAdjectivesNihongo)))
    else:
        for i in range(f):
            print((random.choice(naAdjectives)) + ", " + (random.choice(naAdjectivesNihongo)))

def interjections(g):
    if g<5:
        for i in range(5):
            print((random.choice(interjectionsEng)) + ", " + (random.choice(interjectionsNihongo)))
    else:
        for i in range(g):
            print((random.choice(interjectionsEng)) + ", " + (random.choice(interjectionsNihongo)))
def adjectives(h):

    if h<5:
        for i in range(5):
            print((random.choice(adjectivesNihongo)) + ", " + (random.choice(adjectivesEng)))
    else:
        for i in range(h):
            print((random.choice(adjectivesEng)) + ", " + (random.choice(adjectivesNihongo)))
def adverbs(j):
    if j<5:
        for i in range(5):
            print((random.choice(adverbsNihongo)) + ", " + (random.choice(adverbsEng)))
    else:
        for i in range(j):
            print((random.choice(adverbsNihongo)) + ", " + (random.choice(adverbsEng)))
def conjunctions(k):
    if k<5:
        for i in range(5):
            print((random.choice(conjunctionsEng))) + ", " + (random.choice(conjunctionsNihongo))
    else:
        for i in range(k):
            print((random.choice(conjunctionsEng))) + ", " + (random.choice(conjunctionsNihongo))

def pronouns(l):
    if l<5:
        for i in range(5):
            print(random.choice(pronounsEng)) + ", " + (random.choice(pronounsNihongo))
    else:
        for i in range(l):
            print(random.choice(pronounsEng)) + ", " + (random.choice(pronounsNihongo))

def colours(m):
    if m<5:
        for i in range(5):
            print(random.choice(coloursEng)) + ", " + (random.choice(coloursNihongo))
    else:
        for i in range(m):
            print(random.choice(coloursEng)) + ", " + (random.choice(coloursNihongo))
def japanesePractice(x):
    hiraganaAndKatakana(x)
    #verbs(x)
    #nouns(x)
    #adjectives(x)
    #adverbs(x)
    #auxWords(x)
    #particlesAndPrepositions(x)
    #naAdjectives(x)
    #interjections(x)
    #pronouns(x)
    #colours(x)
japanesePractice(5)
