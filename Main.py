a = "This is is is a test test senctence"
head_list = []

class Splitter:
    def __init__(self):
        self.word_counter = 0

    #function that makes a list of words.
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

    #function that splits a sentence.
    def split(self,sentence):
        for i in range(len(sentence)):
            if(sentence[i] == " " and self.word_counter > 0):
                current_word = a[prev+1:i]
                self.list_maker(head_list,current_word)
                prev = i
                self.word_counter = self.word_counter + 1
            if(sentence[i] == " " and self.word_counter == 0):
                prev = i
                first_word = sentence[:prev]
                self.list_maker(head_list,first_word)
                self.word_counter = self.word_counter + 1
            if(i+1 == len(sentence)):
                last_word =sentence[prev+1:]
                self.list_maker(head_list,last_word)
                self.word_counter = self.word_counter + 1

test = Splitter()
test.split(a)

print(head_list)

def list_sorter(main_list): 
    length = len(main_list) 
    for i in range(length): 
        for j in range(0, length-i-1): 
            if (main_list[j][1] < main_list[j + 1][1]): 
                tempo = main_list[j] 
                main_list[j]= main_list[j + 1] 
                main_list[j + 1]= tempo 
    return main_list 
  
list_sorter(head_list)
print(head_list)