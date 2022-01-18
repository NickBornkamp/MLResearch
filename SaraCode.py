import re

match_accuracy = 90  # percentage of accuracy to consider a line as english

# reading all the words
all_words = open("words_alpha.txt").read().split('\n')
# reading all the codes
#all_codes = open("code.txt").read().split('\n')
# reading all the comments
all_comments = open("commentsAB.csv").read().split('\n')
print(all_comments[0])
counter = 0
englishWords = 0
if __name__ == "__main__":
    # indexing for parallel access to all codes
    idx = 0
    # looping over the comments
    for line in all_comments:
        # lowercasing the comment
        line_tmp = line.lower()
        # get a list of all words without any punctuation and spaces
        line_words = re.sub(r'[^\w\s]', '', line_tmp).split()
        # counting total words for percentage calculation
        total_words = len(line_words)
        # counter for word matches
        matched_words = 0
        # looping over the words
        if(line.find("E") == 0):
            englishWords+=1
        
        
        for word in line_words:
            # checking if the word is in the list of words
            if word in all_words:
                # incrementing the counter for the matched words
                matched_words += 1
        # calcualting the percentage of matched words
        if total_words == 0:
            match_percent = 0
        else:
            match_percent = matched_words / total_words * 100
        # checking if the match is greater than or equal to 80%
        if match_percent >= match_accuracy:
            print("{} - E".format(idx+2))
            counter += 1
            # saving the corresponding comment
            open("commentsAB.txt", "a+").write(line + "\n")
            # saving the corresponding code
          #  open("code_english.txt", "a+").write(all_codes[idx] + "\n")
        else:
            print("{} - N".format(idx+2))
        # incrementing the index
        idx += 1
    print("Total English Comments found: {}".format(counter))
    print("Actual English Comments: {}".format(englishWords))