def principal():
    n = int(input('N: '))

    for i in range(n):
        if (i+1) % 3 == 0:
            print(i+1)


principal()
