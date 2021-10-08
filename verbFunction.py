#Random verb generator
from japaneseVerbVocab import posNeg, verbsEng1, verbsNihongo1, verbsEng2, verbsNihongo2, verbsEng3, verbsNihongo3
import random
def verbs(a):
    if a<5:
        for i in range(5):
            print((random.choice(posNeg)) + " " + (random.choice(verbsEng2)))
            print(random.choice(verbsNihongo2))
    else:
        for i in range(a):
            print((random.choice(posNeg)) + " " + (random.choice(verbsEng2)))
            print(random.choice(verbsNihongo2))

verbs(5)
