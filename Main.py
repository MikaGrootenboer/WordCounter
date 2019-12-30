a = "This is is a test test senctence"
head_list = []

def list_maker(main_list, word):
    if (len(main_list)==0):
        print(main_list)
        main_list.append([word,1])
        print(main_list)
    else:   
        for i in range(len(main_list)):
            if(main_list[i][0]==word):
                 print("'",word,"'","already in list adding a +1 to the counter")
                 print("oldlist ==",main_list)
                 main_list[i][1] = main_list[i][1]+1
                 print("newlist ==",main_list)
                 return main_list
            elif((main_list[i]!=word and i+1 == len(main_list))):
                print("new word found, adding:..",word)
                print("oldlist ==",main_list)
                main_list.append([word,1])
                print("newlist ==",main_list)
                return main_list

class Splitter:
    def __init__(self):
        self.word_counter = 0
        self.wordlist = []

    
    def split(self,sentence):
        for i in range(len(sentence)):
            if(sentence[i] == " " and self.word_counter > 0):
                current_word = a[prev+1:i]
                list_maker(head_list,current_word)
                prev = i
                self.word_counter = self.word_counter + 1
            if(sentence[i] == " " and self.word_counter == 0):
                prev = i
                first_word = sentence[:prev]
                list_maker(head_list,first_word)
                self.word_counter = self.word_counter + 1
            if(i+1 == len(sentence)):
                last_word =sentence[prev+1:]
                list_maker(head_list,last_word)
                self.word_counter = self.word_counter + 1

test = Splitter()
test.split(a)

print(head_list)



