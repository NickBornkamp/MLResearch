'''
Created on Nov 4, 2021

@author: nickr
'''

import os
import pathlib

"""

XXXXX_code_res.ast -> train.token.ast
XXXXX_code_res.sbt -> train.token.sbt
XXXXX_code.txt -> train.token.code
XXXXX_comments.txt -> train.token.nl

"""

def changeName(directory):    
    for file in os.listdir(directory):
        oldFile = directory + '/' + file
        newFile =  directory + '/'
        
        if(oldFile.find('.txt') != -1):
            if(oldFile.find('code') != -1):
                newFile += 'train.token.code'
            else:
                newFile += 'train.token.nl'
                
        elif(oldFile.find('.ast') != -1):
            newFile += 'train.token.ast'
        elif(oldFile.find('.sbt') != -1):
            newFile += 'train.token.sbt'
        else:
            newFile = oldFile.clone()
            
            
        os.renames(oldFile, newFile)

if __name__ == '__main__':
    directory =  'Da Filez'
    
    
    changeName(directory)
    
    
    
    
    pass





