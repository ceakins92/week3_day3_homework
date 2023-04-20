# DESCRIPTION:
# Given a string, return a string that :
# Moves the first letter of each word to the end of it, then adds “ay” to the end of the word. Leave punctuation marks untouched.
# Examples
# pig_it(‘Pig latin is cool’) : ‘igPay atinlay siay oolcay’
# pig_it(‘Hello world !’)     : ‘elloHay orldway !’


def pig_it():

    english_sentence = input(
        "What sentence would you like to convert?\n").lower()
    english_words = english_sentence.split()
    latin_words = []

    vowels = ['a', 'e', 'i', 'o', 'u']

    for word in english_words:
        has_vowel = False

        for i in range(len(word)):

            if word[0] in vowels:
                latin_words.append(word + "yay")
                break
            else:

                if word[i] in vowels:
                    latin_words.append(word[i:] + word[:i] + "ay")
                    has_vowel = True
                    break

                if (has_vowel == False and i == len(word)-1):
                    latin_words.append(word + "ay")
                    break

    pig_latin_sentence = ' '.join(latin_words)
    print(pig_latin_sentence)


pig_it()
