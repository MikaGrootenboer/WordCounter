import sys
import textract
given_input = textract.process("word_document.docx").decode()
test_input = "test test dit is een test om de test file te testen"
main_list = []

class List_creater:
    def list_maker(self,main_list, word):
        #if there are no words in the list yet place the given word in the list with 1 as times happened
        if (len(main_list)==0):
            main_list.append([word,1])
        else:   
            #looping through the list to check all the words.
            for i in range(len(main_list)):
                #when a given word is already in the list add the current counter(the second attribute) +1
                if(main_list[i][0]==word):
                    #print("'",word,"'","already in list adding a +1 to the counter")
                    #print("oldlist ==",main_list)
                    main_list[i][1] = main_list[i][1]+1
                    #print("newlist ==",main_list)
                    return main_list
                #if the word is not in the list add it to the list with a 1 as times happened
                elif((main_list[i]!=word and i+1 == len(main_list))):
                    #print("new word found, adding:..",word)
                    #print("oldlist ==",main_list)
                    main_list.append([word,1])
                    #print("newlist ==",main_list)
                    return main_list
    
    def list_sorter(self,main_list): 
        length = len(main_list) 
        for i in range(length): 
            for j in range(0, length-i-1): 
                if (main_list[j][1] < main_list[j + 1][1]): 
                    tempo = main_list[j] 
                    main_list[j]= main_list[j + 1] 
                    main_list[j + 1]= tempo 
        return main_list 

class Splitter:
    def __init__(self):
        self.word_counter = 0
    #function that splits a sentence.
    def split(self,sentence):
        splitted_sentence = sentence.split()
        for i in range(len(splitted_sentence)):
            List_creater().list_maker(main_list,splitted_sentence[i])
            self.word_counter = self.word_counter + 1

#create all the class instances.
Mainloop = Splitter()
MainList = List_creater()

#split,add and sort the words of the given variable to the head_list
print(Mainloop.split(given_input))
MainList.list_sorter(main_list)
print(main_list)