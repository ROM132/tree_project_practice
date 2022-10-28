def spin_words(sentence):
    sentence = sentence.split()

    new_sentence = ""
    for word in sentence:
        if len(word) >= 5:
            new_sentence += " " + word[::-1]
        else:
            new_sentence += " " + word

    print(new_sentence)

    return None


spin_words(" a that srettel tsisnoc sekat dessap sekat")

