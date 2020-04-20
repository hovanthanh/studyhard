a = [(1, 2), (4, 1), (9, 19), (13, -3)]
b = lambda i: i[1]
# a.sort(key=b)
def add(i):
    	return i[1]
print(a.sort(key=add()))
