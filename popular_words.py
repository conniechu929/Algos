# Return the most the top ten most popular words

text = "dictionary which a a a a is decreasing hello hello order sorted by value"

def popularWords(string):
    my_dict = {}
    result = []

    for word in string.split():
      if word not in my_dict:
        my_dict[word] = 1
      else:
        my_dict[word] += 1

    for word in sorted(my_dict, key=my_dict.get, reverse=True)[:10]:
        result.append((word, my_dict[word]))
    return result

print popularWords(text)
