def solution(matrix):
    sum = 0
    for j in range(len (matrix[0])):
        for i in range(len(matrix)):
            if matrix[i][j] == 0:
                break
            else:
                sum += matrix[i][j]
                
    return(sum)


def run():
    matrix = [[0, 1, 1, 2], 
            [0, 5, 0, 0], 
            [2, 0, 3, 3]]

    print(matrix)
    print(solution(matrix))


if __name__ == '__main__':
    run()