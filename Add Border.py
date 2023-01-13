def solution(picture):
    ast = ''.join('*' for a in range(len(picture[0])+2) )
    print(ast)
    for i, word in enumerate(picture):
        print(word)
        nword = '*' + word + '*'
        print(nword)
        picture[i] = nword
        print(picture[i])

    picture.insert(0, ast)
    picture.insert(len(picture), ast)
    
    print(picture)
    return picture


def run():
    picture = ["abc",
               "ded"]
    print(picture)
    print(solution(picture))

if __name__ == '__main__':
    run()