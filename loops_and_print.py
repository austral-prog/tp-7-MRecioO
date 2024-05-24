def enumerate_list(list):
    nlist = []
    if list != []:
        i = 0 
        for elem in list:
            if  elem != '':
                nlist.append(f'{i}. {elem}')
                i += 1
        return  nlist
    else:
        return list

def enumerate_backwards(list):
    nlist = []
    if list != []:
        i = 0 
        for elem in list:
            if elem != '':
                nlist.append(f'{i}. {elem[::-1]}')
                i += 1
        return nlist
    else:
        return list
