from ps4a import *
import time

def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    maxScore=0
    score=0
    bestWord=None
    for i in wordList:
        if(isValidWord(i, hand, wordList)):
            score=getWordScore(i, n)
            if(score>maxScore):
                maxScore=score
                bestWord=i

    return bestWord

def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    score=0
    while(calculateHandlen(hand) > 2):
        currentHand=''
        for letter in hand.keys():
            for j in range(hand[letter]):
                currentHand += ' '
                currentHand += str(letter)
        print("Current Hand: %s" % currentHand)
        word=compChooseWord(hand, wordList, n)
        if((type(word)==None) or word ==None):
            break
        currentScore=getWordScore(word, n)
        score += currentScore
        hand=updateHand(hand, word)
        print('"%s" earned %d points. Total: %d points' %(word,currentScore,score))
        print
    if((calculateHandlen(hand)==1) or (calculateHandlen(hand)==2)):
        currentHand=''
        for letter in hand.keys():
            for j in range(hand[letter]):
                currentHand += ' '
                currentHand += str(letter)
        print("Current Hand: %s" % currentHand)        
    print("Total Score: %d points" %score)

def playGame(wordList):
    savedCurrentHand=''
    while(1):
        inp=raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game:")
        if(inp=='r'):
            if(savedCurrentHand==''):
                print("You have not played a hand yet. Please play a new hand first!")
            else:
                print
                opt=raw_input("Enter u to have yourself play, c to have the computer play:")
                while((opt!='u') and (opt!='c')):
                    print("Invalid command.")
                    print
                    opt=raw_input("Enter u to have yourself play, c to have the computer play:") 
                if(opt=='u'):
                    print
                    playHand(savedCurrentHand, wordList, HAND_SIZE)
                elif(opt=='c'):
                    print
                    compPlayHand(savedCurrentHand, wordList,HAND_SIZE)
                else:
                    print("Invalid command.")
        elif(inp=='n'):
            print
            opt=raw_input("Enter u to have yourself play, c to have the computer play:")
            while((opt!='u') and (opt!='c')):
                print("Invalid command.")
                print
                opt=raw_input("Enter u to have yourself play, c to have the computer play:") 
            if(opt=='u'):
                print
                hand=dealHand(HAND_SIZE)
                savedCurrentHand=hand
                playHand(savedCurrentHand, wordList, HAND_SIZE)
            elif(opt=='c'):
                print
                hand=dealHand(HAND_SIZE)
                savedCurrentHand=hand
                compPlayHand(hand, wordList, HAND_SIZE)
            else:
                print("Invalid command.")
        elif(inp=='e'):
            break
        else:
            print("Invalid command.")
        print
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


