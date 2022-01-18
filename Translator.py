'''
Created on Nov 5, 2021

@author: nickr
'''


import time

class Language:
    
    def __init__(self, file, score):
        self.file = file
        self.score = score
    def formatLines(self):
        return tuple(open(self.file, 'r').readlines())

commentFile = open('commentsAB.csv', 'r')
engComment = open('English Comments.txt', 'w')
fileCode = open('code.txt', 'r')
engCode = open('English Code.txt', 'w')

fileRejects = open('rejects.txt', 'w')
engDict = Language('Dictionaries/words_alpha.txt', 1.0)
stopDict = Language('Dictionaries/stopwords.txt', 2.5)
trueStopDict = Language('Dictionaries/trueStopWords.txt', 10.0)

frenchLines = tuple(open('Dictionaries/francais.txt', 'r').readlines())
dutchLinesz = open('Dictionaries/deutsch.txt', 'r').readlines()



italianLines = tuple(open('Dictionaries/italiano.txt', 'r').readlines())
spanishLines = tuple(open('Dictionaries/espanol.txt', 'r').readlines())
polishLines = tuple(open('Dictionaries/polish.txt', 'r').readlines())
germanLinesz = open('Dictionaries/german.txt', 'r').readlines()


stopWordLines = tuple(open('Dictionaries/stopwords.txt', 'r').readlines())




dictionaries = {stopDict.formatLines(): stopDict.score, engDict.formatLines() : engDict.score, trueStopDict.formatLines() : trueStopDict.score}
#dictionaries[frenchLines] = 0.3
#dictionaries[dutchLines] = 0.2
dictionaries = dict(sorted(dictionaries.items(), key=lambda item: item[1], reverse = True))


for lang in dictionaries:
    print('50th word: ' + str(lang[51]).strip() + "; Score: " + str(dictionaries.get(lang, 0)))
    

commentLines = commentFile.readlines()



codeLines = fileCode.readlines()

count = 0
lineNum = 0


def commentEnglish(comment):
    if(len(comment) == 0):
        return False
    score = 0.0
    percentPass = 0.68
    for word in comment:
        word = word.lower() + '\n'
        for lang in dictionaries:
            if(lang.count(word) != 0):
                score += dictionaries.get(lang, 0)
                break
                
    
    
    if(percentPass <= (score/len(comment))):
        return True;
    return False
    



start = time.time()
print('lets go')
counter = 0
actualWords = 0
for line in commentLines:
    
    comment = line.replace('*', '').replace('/', '').rsplit()
    
    if(line.find("E") == 0):
        actualWords+=1
    comment = comment[1:len(comment)-1]

    if(commentEnglish(comment)):
        engComment.write(line)
        engCode.write(codeLines[lineNum])
        counter+=1
    else:
        fileRejects.write(line)
    
    lineNum+=1
    if(lineNum % 1000 == 0):
        print(str(int(lineNum/1000)) + 'K')
        print('time: ' + str(time.time()-start))
        start = time.time()
    
    if(lineNum == 1000):
        break
        

def checkCorrect():
    return 1

    
print('done!')
print('time: ' + str(time.time()-start))
print("Total English Comments found: {}".format(counter))
print("Actual English Comments: {}".format(actualWords))
print("Percentage: {}%".format(round((counter*100/actualWords), 2)))