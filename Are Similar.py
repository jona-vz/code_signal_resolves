def solution(a, b):
    aset = set(a)
    bset = set(b)
    if aset != bset:
        return False
    
    for i in range(len(a)):
        for j in range(1, len(a)):
            c = a.copy()
            c[i] = a[j]
            c[j] = a [i]
            if c == b:
                return True

    return False

def solution2(a, b):
    counter = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            counter +=1
    if counter > 2:
        return False
    a = sorted(a)
    b = sorted(b)
    if a != b :
        return False
    
    return True

def solution3(a, b):
    counter = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            counter +=1
    if counter > 2:
        return False
    if sorted(a) != sorted(b) :
        return False
    
    return True



def run():
    a = [1, 2, 3]
    b = [1, 3, 2]

    print(a, b)
    print(solution3(a, b))

if __name__ == '__main__':
    run()