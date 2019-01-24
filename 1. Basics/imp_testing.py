L = [1,2,3,4,5]

def find_index(to_search, to_find):
    for idx, item in enumerate(to_search):
        if item == to_find:
            return idx