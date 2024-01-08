import multiprocessing

def side1(a):
    print('lisa*', a)

def side2(b):
    print('naruto*', b)

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=side1, args=(5,))
    p2 = multiprocessing.Process(target=side2, args=(6,))
    p1.start()
    p2.start()
    p1.join()
    print("baba buii")
    p2.join()
