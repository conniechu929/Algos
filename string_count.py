def count_string(word):
    count = 1
    result = ''

    for i in range(len(word)):
        if i < len(word) - 1 and word[i] != word[i+1]:
            result = result + str(count) + word[i]
            count = 1
        elif word[i] == word[len(word)-1]:
            result = result + str(count) + word[i]
        else:
            count += 1
    return result

print count_string("aaaabbbcccd")
