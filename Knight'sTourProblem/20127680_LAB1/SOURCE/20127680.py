from os import access
import sys
import random
import time

move_x = [2, 1, -1, -2, -2, -1, 1, 2]
move_y = [1, 2, 2, 1, -1, -2, -2, -1]


class moveCount:
    count = 2

    def __init__(self, numCount):
        self.count = numCount


def printBoard(n, board):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()
    print(moveCount.count)


def write_board(filename, list, n, time):
    file = open(filename, 'w')
    file.write("X: " + str(init_x) + " " + "Y: " +
               str(init_y) + " " + "Size: " + str(n) + '\n')
    file.write("Moves: " + str(moveCount.count - 1) + '\n')
    file.write("Time: " + str(time) + " ms" '\n')
    for i in range(n):
        for j in range(n):
            file.write(str(list[i][j]) + " ")
        file.write('\n')
    file.close()


def isValidCoordinate(x, y, n):
    if(x >= 0 and y >= 0 and x < n and y < n):
        return True
    return False


def solve_backtrack(count, x, y, n, board, start_time):
    if(count == n*n + 1):
        return True

    end_time = time.time()
    if((end_time - start_time)*1000 >= 3600*1000):
        return True

    for i in range(8):
        next_x = x + move_x[i]
        next_y = y + move_y[i]
        if (isValidCoordinate(next_x, next_y, n) and board[next_x][next_y] == -1):
            board[next_x][next_y] = count
            moveCount.count = moveCount.count + 1
            if(solve_backtrack(count + 1, next_x, next_y, n, board, start_time)):
                return True
            board[next_x][next_y] = -1
    return False


def solveKnightTour_backtrack(init_x, init_y, board, n, start_time):
    board[init_x][init_y] = 1
    solve_backtrack(moveCount.count, init_x, init_y, n, board, start_time)


def getAccess(x, y, board, n):
    allAccess = []
    s = random.randint(1, n)
    for c in range(8):
        i = (s + c) % 8
        next_x = x + move_x[i]
        next_y = y + move_y[i]
        moveCount.count = moveCount.count + 1
        if(isValidCoordinate(next_x, next_y, n) and board[next_x][next_y] == -1):
            allAccess.append((next_x, next_y))
    return allAccess


def solveKnightTour_Warnsdorff(init_x, init_y, board, n):
    board[init_x][init_y] = 1
    count = 2
    next_x = init_x
    next_y = init_y
    for k in range(n * n - 1):
        access = getAccess(next_x, next_y, board, n)
        if (len(access) != 0):
            min = access[0]
            for i in access:
                if(len(getAccess(i[0], i[1], board, n)) <= len(getAccess(min[0], min[1], board, n))):
                    min = i
            next_x = min[0]
            next_y = min[1]
            board[next_x][next_y] = count
            count += 1
    moveCount.count = count - 1

# <executable filename> -px <x> -py <y> -s <m>


if __name__ == "__main__":
    if (len(sys.argv) == 7):
        size = int(sys.argv[6])
        init_x = int(sys.argv[2])
        init_y = int(sys.argv[4])
        if(size < 5 or init_x < 1 or init_y < 1 or init_x > size or init_y > size):
            print("Invalid input!!\n")
        else:
            board = [-1] * size
            for j in range(size):
                board[j] = [-1] * size

            start_time = time.time()
            # solveKnightTour_Warnsdorff(init_y - 1, init_x - 1, board, size)
            solveKnightTour_backtrack(init_y - 1,init_x - 1, board, size, start_time)
            end_time = time.time()
            time = (end_time - start_time)*1000
            # write_board("20127680_heuristic.txt", board, size, "%0.2f" % time)
            write_board("20127680_backtrack.txt", board, size, "%0.2f" % time)
    else:
        print("Invalid input!!! \n")
