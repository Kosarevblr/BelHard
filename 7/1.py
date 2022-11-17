# Написать функцию horse принимающая координаты (два числа в диапазоне от 1 до 8)
# расположения коня на шахматной доске, вывести все позиции куда может перейти конь за 1
# шаг

x, y = int(input('Enter coordinate x: ')), int(input('Enter coordinate y: '))

def horse(x, y):
    all_coord = []
    new_coord = []
    if x not in range(1, 9) and y not in range(1,9):
        print('Wrong coordinates')
    else:
        if 0<x+2<9 and 0<y+1<9:
            new_coord.append(x+2)
            new_coord.append(y+1)
            all_coord.append(tuple(new_coord))
        new_coord.clear()
        if 0<x+2<9 and 0<y-1<9:
            new_coord.append(x+2)
            new_coord.append(y-1)
            all_coord.append(tuple(new_coord))
        new_coord.clear()
        if 0<x-2<9 and 0<y+1<9:
            new_coord.append(x-2)
            new_coord.append(y+1)
            all_coord.append(tuple(new_coord))
        new_coord.clear()
        if 0<x-2<9 and 0<y-1<9:
            new_coord.append(x-2)
            new_coord.append(y-1)
            all_coord.append(tuple(new_coord))
        new_coord.clear()
        if 0<x+1<9 and 0<y+2<9:
            new_coord.append(x+1)
            new_coord.append(y+2)
            all_coord.append(tuple(new_coord))
        new_coord.clear()
        if 0<x-1<9 and 0<y+2<9:
            new_coord.append(x-1)
            new_coord.append(y+2)
            all_coord.append(tuple(new_coord))
        new_coord.clear()
        if 0<x+1<9 and 0<y-2<9:
            new_coord.append(x+1)
            new_coord.append(y-2)
            all_coord.append(tuple(new_coord))
        new_coord.clear()
        if 0<x-1<9 and 0<y-2<9:
            new_coord.append(x-1)
            new_coord.append(y-2)
            all_coord.append(tuple(new_coord))
        new_coord.clear()
    return print(*all_coord)

horse(x,y)


