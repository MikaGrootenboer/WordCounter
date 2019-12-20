a = "Hallooooo this is a second test of the word count thing program"
word_counter = 0

for i in range(len(a)):
    if(a[i] == " " and word_counter > 0):
        print(a[prev+1:i])
        prev = i
        word_counter = word_counter + 1
    if(a[i] == " " and word_counter == 0):
        prev = i
        first_word = a[:prev]
        print(first_word)
        word_counter = word_counter + 1
    if(i+1 == len(a)):
        print(a[prev+1:])
        word_counter = word_counter + 1

print(word_counter)