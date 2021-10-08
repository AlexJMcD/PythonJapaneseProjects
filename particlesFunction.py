#Japanese particles function
import random
from japaneseParticlesVocab import particles1, particles2

def particles(a):
    if a<5:
        for i in range(5):
            print(random.choice(particles1))
    else:
        for i in range(a):
            print(random.choice(particles1))

particles(3)