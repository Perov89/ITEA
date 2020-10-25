def func(text):
    letters = 0
    words = 0
    for symbol in text:
        letters += 1
    for word in text.split(' '):
        words += 1
    print(line, letters, "симв.", words, 'сл.', "\n")



with open('MyParsing',encoding='UTF-8') as pars:
    stroka = 0
    for line in pars.readlines():
        func(line)
        stroka +=1
    print(stroka,'строки')
# ______________________________________________________________________________________________________________________










