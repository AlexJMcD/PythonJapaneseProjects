
import random
verbVocab={"aru": "there is/to have/there exists (non-sentient)", "iru": "there is/to have/there exists (sentient)"}
dictionary={"verbs": {"aru": "there is/to have/there exists (non-sentient)", "iru": "there is/to have/there exists (sentient)"}, 'other': {'hello': 'yes'}}
from japaneseVerbVocab import verbs2
def vocabTest(x):
    rightAnswers=0
    questionNumber=1
    listChoice=input("What list would you like to be tested on?")
    while True:
        try:
            listChoice==verbs2[listChoice]
        except:
            print("\nYou have not selected a valid vocab list name.")
            listChoice=input("\nPlease enter a valid vocab list name.")
        else:
            break
    user_input=verbs2[listChoice]
    for key in range(x):
        print(f"\nQuestion {questionNumber}")
        question=(random.choice(list(user_input.items())))
        testWord=(random.choice(question)) #(question[1]) - for english words only, (question[0]) for the japanese words only.
        userAnswer=input(f"\nWhat is the translation of '{testWord}'?")
        if userAnswer==(question[0]) or userAnswer==(question[1]):
            print("\ncorrect")
            rightAnswers +=1
        else:
            print("\nIncorrect")
            rightAnswers=rightAnswers
            if testWord==question[0]:
                print(f"\nThe correct answer was, '{question[1]}'")
            else:
                print(f"\nThe correct answer was '{question[0]}'")

        questionNumber+=1
    print("\nTest complete")
    print(f"\nYou scored {rightAnswers} out of {x}")

#vocabTest(5)
def makeASentence(x):
    nounList=(input("Which noun list would you like a random word from?"))
    verbList=(input("\nWhich verb list would you like a random word from?"))
    adjectiveList=(input("\nWhich adjective list would you like a random word?"))
    while True:
        try:
            nounList==verbs2[nounList]
        except:
            print("\nYou have not entered a valid noun list name, please enter the name again.")
            nounList=(input("\nWhich noun list would you like a random word from?"))
        else:
            break
        try:
            verbList==verbs2[verbList]
        except:
            print("\nYou have not entered a valid verb list name, please enter the name again.")
            verbList=(input("\nWhich verb list would you like a random word from?"))
        else:
            break
        try:
            adjectiveList==verbs2[adjectiveList]
        except:
            print("\nYou have not entered a valid adjective list name, please enter the name again.")
            adjectiveList=(input("\nWhich adjective list would you like a random word from?"))
        else:
            break
    nounSource=verbs2[nounList]
    verbSource=verbs2[verbList]
    adjectiveSource=verbs2[adjectiveList]
    for key in range(x):
        noun = random.choice(list(nounSource.items()))
        verb = random.choice(list(verbSource.items()))
        adjective = random.choice(list(adjectiveSource.items()))
        print(f"\nMake a sentence from the following words: {noun[0]}, {verb[0]}, {adjective[0]}")
        print(f"\nMake a sentence from the following words: {noun[1]}, {verb[1]}, {adjective[1]} ")


vocabTest(5)










