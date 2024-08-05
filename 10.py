def frequency_of_words(text):
    words=text.split()#kelimleri ayırdım
    word_count={} #Bu ifade Python'da boş bir sözlük (dictionary) oluşturur.
    #örn bi kelimenin kaç defa geçtiğini saklamak istiyorsam 
    for word in words:
        word=word.lower().strip(".,?:;")
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1
    return word_count
user_input=input("Enter a text: ")
word_counts= frequency_of_words(user_input)

for word in word_counts:
    print(word, ":", word_counts[word])
