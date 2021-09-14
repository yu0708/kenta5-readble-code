f = open('dictionary.txt', 'r', encoding='UTF-8')
word_list = f.readlines()

for i,word in enumerate(word_list):
    id=i+1
    print(id,':',word[:-1])

f.close()