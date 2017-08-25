from random import choice
from sys import exit
num_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
blank_points = [
    [0, 0], [0, 1], [0, 2], [0, 3],
    [1, 0], [1, 1], [1, 2], [1, 3],
    [2, 0], [2, 1], [2, 2], [2, 3],
    [3, 0], [3, 1], [3, 2], [3, 3]
]
win = False


def output():
    if win or (not blank_points):
        if win:
            print("you win!")
        else:
            print("you fail!")
        a = input("what do you want to do? -(r for reset, q for quit)")
        assert a == "q" or a == "r"
        if a == "q":
            q()
        if a == "r":
            reset()
        return
    print("=" * 20)
    for i in num_map:
        a = ""
        for j in i:
            a = a + str(j) + " | "
        print(a[:-3])
        print("--|---|---|--")
    print("=" * 20)


def craft(array):
    checking = 0
    checked = []
    for i, j in enumerate(array):
        if j == 0:
            continue
        else:
            if checking > 0 and array[checking - 1] == j and (not checking - 1 in checked):
                array[checking - 1] = j * 2
                array[i] = 0
                checked.append(checking - 1)
                continue
            array[checking] = j
            if not i == checking:
                array[i] = 0
            checking = checking + 1


def spawn():
    global num_map, blank_points
    if not blank_points:
        output()
    else:
        position = choice(blank_points)
        num_map[position[0]][position[1]] = choice([2, 4])


def reset():
    global num_map, blank_points, win
    num_map = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    blank_points = [
        [0, 0], [0, 1], [0, 2], [0, 3],
        [1, 0], [1, 1], [1, 2], [1, 3],
        [2, 0], [2, 1], [2, 2], [2, 3],
        [3, 0], [3, 1], [3, 2], [3, 3]
    ]
    win = False
    for i in range(2):
        refresh()
        spawn()
    refresh()
    output()


def q():
    exit(0)


def refresh():
    global blank_points, win
    del blank_points
    # for i in blank_points:
    #    blank_points.remove(i)
    blank_points = []
    for i, j in enumerate(num_map):
        for a, b in enumerate(j):
            if b == 2048:
                win = True
            if b == 0:
                blank_points.append([i, a])


def move(direction):
    global num_map
    array = []
    if direction == "w":
        for j in range(4):
            for i in range(4):
                array.append(num_map[i][j])
            craft(array)
            for i in range(4):
                num_map[i][j] = array[i]
            array = []
    elif direction == "a":
        for j in range(4):
            for i in range(4):
                array.append(num_map[j][i])
            craft(array)
            for i in range(4):
                num_map[j][i] = array[i]
            array = []
    elif direction == "s":
        for j in range(4):
            for i in range(4):
                array.append(num_map[3-i][j])
            craft(array)
            for i in range(4):
                num_map[3-i][j] = array[i]
            array = []
    elif direction == "d":
        for j in range(4):
            for i in range(4):
                array.append(num_map[j][3-i])
            craft(array)
            for i in range(4):
                num_map[j][3-i] = array[i]
            array = []
    refresh()
    spawn()
    output()


def main():
    reset()
    while True:
        action = input("what do you want to do? -(wasd for up, right, down, left move\n,r for restart, q for quit)")
        assert action == "w" or action == "a" or action == "s" or action == "d" or action == "r" or action == "q"
        if action == "q":
            q()
        elif action == "r":
            reset()
        else:
            move(action)
if __name__ == "__main__":
    main()
