def func(text):
    letters = 0
    for symbol in text:
        letters += 1
    print(line,letters,"симв.","\n")


with open('MyParsing',encoding='UTF-8') as pars:
    for line in pars.readlines():
        func(line)










