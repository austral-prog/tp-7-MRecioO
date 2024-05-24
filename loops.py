def index_of_by_index(word, list, index):
    i = -1
    nlist = []
    for elem in list[index:]:
        if elem != word:
            nlist.append(elem)
        else:
            i = len(nlist) + len(list[:index])
            break
    return i

def index_of_empty(list):
    i = -1
    nlist = []
    for elem in list:
        if elem != '':
            nlist.append(elem)
        else:
            i = len(nlist)
            break
    return i

def index_of(word, list):
    i = -1
    nlist = []
    for elem in list:
        if elem != word:
            nlist.append(elem)
        else:
            i = len(nlist)
            break
    return i

def put(word, list):
    i = 0
    if '' in list:
        for elem in list:
            i += 1
            if elem == '':
                list.insert(i, word)
                del list[i - 1]
                i = i - 1
                break
        return i 
    else:
        return -1

def remove(word, list):
    i = 0
    for item in list:
        if item == word: 
            list[index_of(word,list)] = ''
            i += 1
    return i
