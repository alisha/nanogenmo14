import sys
from random import randrange
from datetime import date, timedelta
import xml.etree.ElementTree as ET

# Get words
corpus = open("corpus.txt", "r")
wordLines = corpus.readlines()

for line in range(0, len(wordLines)-2):
    wordLines[line] = wordLines[line][:-1]

corpus.close()

# Store the start of sentences
sentenceStarters = []

# Current chapter
chapter = 1

# Characters
characters = ["Makena", "Florence"]

# Number of words in novel
numWords = 0

# Create graph of words
def createWordMap(wordLines):
    wordMap = dict()

    for line in wordLines:
        
        words = line.split()

        endOfSentence = True
        
        for index in range(0,len(words)-2):
            
            # Add to list of sentence starters
            if endOfSentence:
                sentenceStarters.append((words[index], words[index + 1]))
                endOfSentence = False

            # Check if at the end of sentence
            if words[index + 1] == "?" or words[index + 1] == "." or words[index + 1] == "!":
                endOfSentence = True

            # Add to word map
            wordMap[(words[index], words[index + 1])] = words[index + 2]

    return wordMap

# Generate one line
def genLine(wordMap):
    index = randrange(len(sentenceStarters) - 1)

    firstWord = sentenceStarters[index][0]
    secondWord = sentenceStarters[index][1]
    thirdWord = wordMap[(firstWord, secondWord)]
    
    # holds an array of words in one line of a conversation
    line = [firstWord, secondWord, thirdWord]
    words = 3

    lastElements = (line[1], line[2])

    # stop when the conversation can't go on
    while lastElements in wordMap.keys() and words < 40:
        line.append(wordMap[(lastElements[0], lastElements[1])])
        words += 1
        
        # find last words again
        end = len(line)
        lastElements = (line[end-2], line[end-1])

    return [' '.join(line), words]

def genChapter(wordMap, chapter, numWords):
    # start chapter
    currentDate = date.today() + timedelta(chapter - 1)
    book = open('novel.md', 'a')
    book.write("\n\n\n## Chapter " + `chapter` + "\n" + currentDate.strftime("%A, %B %d, %Y") + "\n\n**" + characters[0] + ":** My dear " + characters[1] + ", how are you?\n")
    words = 13

    # generate story
    characterIndex = 0

    for x in xrange(0,11):
        line = genLine(wordMap)
        book.write("**" + characters[characterIndex] + ":** " + line[0] + "\n")
        characterIndex = (characterIndex+1)%2
        words += line[1]

    # end chapter
    book.write("**" + characters[1] + ":** Until we meet again")
    words += 5
    book.close()
    
    return words


# Generate the novel
book = open('novel.md', 'w')
book.write("# The Conversations of " + characters[0] + " and " + characters[1] + "\n\nBy Alisha Ukani")
numWords += 9
book.close()

wordMap = createWordMap(wordLines)
print `numWords`

while numWords < 50000:
    numWords += genChapter(wordMap, chapter, numWords)
    print numWords
    chapter += 1

print `numWords`
