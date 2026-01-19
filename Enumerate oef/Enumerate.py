dagen = ["mon","teus","wedns","thurs","frid","sat","sun"]
print(list(enumerate(dagen)))

def enumerateList(iterable, start):
    print(list(enumerate(iterable, start=start)))

enumerateList(dagen, 3)