def pig_it(str):
    words = str.split()
    pig_words = []

    for word in words:
        if word.isalpha():
            pig_words.append(word[1:] + word[0] + 'ay')
        else:
            pig_words.append(word)
        print(pig_words)
        print(' '.join(pig_words))


pig_it("Hello World !")
