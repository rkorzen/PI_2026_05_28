

x = [1, 2, 3]
type(x) == list
isinstance(x, list)



assert splaszcz([]) == []
assert splaszcz([1, 2, 3]) == [1, 2, 3]
assert splaszcz([1, [2, 3]]) == [1, 2, 3]
assert splaszcz([1, [2, [3]]]) == [1, 2, 3]
assert splaszcz([1, [2, [3], 4], 5, 6]) == [1, 2, 3, 4, 5, 6]