a = "This is is a test test senctence"


class Splitter:
    def __init__(self):
        self.word_counter = 0
        self.wordlist = []

    
    def split(self,sentence):
        for i in range(len(sentence)):
            if(sentence[i] == " " and self.word_counter > 0):
                current_word = a[prev+1:i]
                #print(current_word)
                self.wordlist.append([current_word,1])
                prev = i
                self.word_counter = self.word_counter + 1
            if(sentence[i] == " " and self.word_counter == 0):
                prev = i
                first_word = sentence[:prev]
                #print(first_word)
                self.wordlist.append([first_word,2])
                self.word_counter = self.word_counter + 1
            if(i+1 == len(sentence)):
                #print(sentence[prev+1:])
                self.wordlist.append([sentence[prev+1:],1])
                self.word_counter = self.word_counter + 1
    
    def word_count_printer(self):
        return self.word_counter

    def word_list_return(self):
        return self.wordlist

test = Splitter()
test.split(a)

newlist = test.word_list_return()

final_list = []

for i in range(test.word_count_printer()):
    word_count_adder  = 1
    j = 1
    if (newlist[i][0] == newlist[j][0]):
        print(newlist[i][0])
        j = j + 1
        final_list.append([newlist[i][0], (1 + word_count_adder)])
    else:
        j = j + 1
        final_list.append([newlist[i][0],1])


print(final_list)


