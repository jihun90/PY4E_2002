def count_word(text, word) :
    count = str(text).count(word)
    return count

text = "자세히 보아야 예쁘다\n오래 보아야 사랑스럽다\n너도그렇다."
print(count_word(text,"보아야"))


