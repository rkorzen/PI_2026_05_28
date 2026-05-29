def splaszcz(lista):
    result = []
    for el in lista:
        if isinstance(el, list):
            result.extend(splaszcz(el))
        else:
            result.append(el)
    return result



assert splaszcz([]) == []
assert splaszcz([1, 2, 3]) == [1, 2, 3]
assert splaszcz([1, [2, 3]]) == [1, 2, 3]
assert splaszcz([1, [2, [3]]]) == [1, 2, 3]
assert splaszcz([1, [2, [3], 4], 5, 6]) == [1, 2, 3, 4, 5, 6]