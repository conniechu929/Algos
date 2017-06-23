def removeDup(string):
    temp_list = list(string)
    result = []
    for i in temp_list:
        if i not in result:
            result.append(i)
    return ''.join(result)
