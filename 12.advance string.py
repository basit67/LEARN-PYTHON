my_name = "bloodyh"
print(my_name[0])
print(my_name[-1])

sentence = "this is sentence"
print(sentence[:4])

print(sentence.split())

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

quote = "he said ,'give me your money'"
print(quote)

too_much_space = "              hellow"
print(too_much_space.strip)

print("a" in "apple") #case sensitive

letter = 'A'
word = "Apple"
print(letter.lower() in word.lower())

movie = "hangover"
print("my favrite movie is {}".format(movie))