import numpy as np

def run():
    array = np.random.randint(0, 100, 100)
    print(array[:10])
    array[array%2 == 1] = -1 
    print(array[:10])


if __name__ == '__main__':
    run()