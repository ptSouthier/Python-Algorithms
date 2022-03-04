def is_palindrome_iterative(word):
    splitted_word = word.split()

    return splitted_word.reverse() == splitted_word
