def word_search(string, word_list):
    string_list = list(list(letter) for letter in string)
    if sorted(string_list) == sorted(word_list):
        return string
