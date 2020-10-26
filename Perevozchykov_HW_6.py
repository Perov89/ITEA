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
import re

def readMass(filename):
    with open(filename) as file:
        mass = []
        N =0

        for row in file:
            z = []

            rowStr = row.strip('\n')
            rowStr  = re.split(' +', rowStr)

            for i in rowStr:
                z.append(int(i))

            mass.append(z)
            N += 1
    return mass, N

def printMass(mass, N):
    for i in range(N):
        for j in range(N):
            print("%-4d" % mass[i][j], end='')

        print()


def sumMass(mass,N):
    sum = []
    s = 0
    max = 0
    w = 1
    for j in range(N):
        for i in range(N):
            s += mass[i][j]
            i += 1
        sum.append(s)
        s = 0
    j += 1
    # return sum
    print(sum)
    # print(max)
    for x in sum:
        if x > max:
            max = x
    # print(max)
    print(sum.index(max)+1)





if __name__ == '__main__':
    mass, N = readMass(r'C:\work\python08\GIT\input.txt')

    printMass(mass,N)

    sumMass(mass,N)





