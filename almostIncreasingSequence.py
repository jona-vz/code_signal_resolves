def solution(sequence):
    for i in range (1, len(sequence)):
        if sequence[i-1] < sequence[i]:
            continue
        else:
            print('primer caso')
            #hacemos un copia
            seq2 = sequence.copy()
            seq2.pop(i-1)
            
            #determinamos la lista 
            #ordenados
            seq_orden = sorted(seq2)
            print(seq_orden)
            #unicos
            seq_orden = list(dict.fromkeys(seq_orden))
            print(seq_orden)
            
            if seq2 == seq_orden:
                return True
            else:
                print('segundo caso')
                seq2 = sequence.copy()
                print(seq2)
                seq2.pop(i)
                print(seq2)

                #ordenados
                seq_orden = sorted(seq2)
                print(seq_orden)
                #unicos
                seq_orden = list(dict.fromkeys(seq_orden))
                print(seq_orden)

                if (seq2 == seq_orden):
                    return True
                else:
                    return False

    return True


def run():
    #a = [1, 3, 2, 1]
    #a = [1, 3, 2]
    #a = [1, 2, 1, 2]
    #a = [0, -2, 5, 6]
    #a = [123, -17, -5, 1, 2, 3, 12, 43, 45]
    a = [3, 6, 5, 8, 10, 20, 15]
    print(a)
    # b = sorted(a)
    # print(b)
    print(solution(a))


if __name__ == '__main__':
    run()