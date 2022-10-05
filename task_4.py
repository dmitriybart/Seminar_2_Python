text = input('Введите текст: ')
rub = 60*len(text)//100
kop = 60*len(text)%100
print(rub,'руб.', kop, 'коп.')