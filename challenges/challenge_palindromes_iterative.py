def is_palindrome_iterative(word):
    splitted_word = word.split()

    if splitted_word.reverse() == splitted_word:
        return True

    else:
        return False
