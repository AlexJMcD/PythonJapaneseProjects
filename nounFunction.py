#Noun function
import random
from japaneseNounVocab import nounsEng1, nounsEng2, nounsEng3, nounsEng4, nounsEng5, nounsNihongo1, nounsNihongo2, nounsNihongo3, nounsNihongo4, nounsNihongo5

def nouns(a):
    if a<5:
        for i in range(5):
            print(random.choice(nounsEng3))
            print(random.choice(nounsNihongo3))
    else:
        for i in range(a):
            print(random.choice(nounsEng3))
            print(random.choice(nounsNihongo3))

nouns(5)