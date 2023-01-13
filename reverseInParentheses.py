def solution(inputString):
    print('inputString: '+inputString)
    if '(' in inputString:
        print('si tiene todavia')
        inicio = inputString.find('(')
        final = inputString[::-1].find(')')
        print(inicio, final)
        subs = inputString[inicio+1:len(inputString)-final-1]
        print('.....' + subs)
        dentro = solution(subs)
        print('dentro: ' + dentro)
        dentro = dentro[::-1]        
        print('dentro reverseado: ' + dentro)
        subs = inputString[:inicio] + dentro + inputString[len(inputString)-final:]

        print ('subs:' + subs) 
        return subs
    else:
        return inputString
    

def solution2(inputString):
    inputList = list(inputString)
    openp = []
    for i, l in enumerate(inputList):
        print('i: ' + str(i) + '   l: ' + str(l))
        if l == '(':
            print('abierto')
            openp.append(i)
        elif l == ')':
            print('cerrado')
            print(openp)
            j = openp.pop()
            print(i, j)
            print(inputList[j+1:i])
            print(inputList[i-1:j:-1])

            inputList[j+1:i] = inputList[i-1:j:-1]
            print('inputList hasta ahora: ' + str(inputList))

    res = ''.join(l for l in inputList if l not in '()')
    return res

    

    
def run():
    inputString = "mur(ci(123)e)l(ag)o"
    #inputString = "foo(bar)baz"

    print(inputString)
    print(solution2(inputString))


if __name__ == '__main__':
    run()