word=input('Введите слово: ')
first=list(word)
second=list(word)
second.reverse()
if second==first:
    print('True')
else:
    print(bool(0))