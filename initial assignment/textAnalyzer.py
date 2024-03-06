global_words=["is","if","are","the"]
def text_analyzer(input):
    sepWords=input.split()
    print(sepWords)
    longestWord=sepWords[0]
    for i in sepWords:
        if len(i)>len(longestWord):
            longestWord=i
            print(i)
    for word in sepWords:
         if word in global_words:
              sepWords.remove(word)
    print(sepWords)
    unique_word={}
    for word in sepWords:
            if word in unique_word:
                unique_word[word]+=1
            else:
                  unique_word[word]=1
    print (unique_word)
   

text_analyzer("how are you friend we are glad you are here")