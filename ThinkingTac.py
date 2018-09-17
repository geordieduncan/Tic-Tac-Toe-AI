import random


draw = {
    -1: "X  |",
    0: "   |",
    1: "O  |"
}


class Spot:
    def __init__(self, x, y, n):
        self.x = x
        self.y = y
        self.n = n

    def __str__(self):
        return draw[self.n]


class Board:
    def __init__(self, length, w):
        self.length = length
        self.w = w
        self.build = []
        R = []
        for i in range(self.length):
            for j in range(self.w):
                R.append(0)
        self.build.extend(R)

    def show(self):
        print "\n" * 10
        for i in range(self.length):
            print " -----+-----+-----"
            txt = '|  '
            for j in range(self.w):
                txt += draw[Spot(i, j, self.build[i * 3 + j]).n] + "  "
            print txt
        print " -----+-----+-----"


GB = Board(3, 3)
Moves = {}


def chose(n):
    print ''
    print '   0     1     2 '
    print ''
    print '   3     4     5 '
    print ''
    print '   6     7     8 '
    print 'player 1:'
    while 1 > 0:
        c = input('Which square would you like?')
        try:
            if GB.build[c] != 0:
                print 'pick again'
            else:
                GB.build[c] = n
                break
        except IndexError:
            pass


def randMove(n, board):
    choice = -1
    options = []
    for i in range(9):
        if board[i] == 0:
            options.append(i)
    if len(options) > 0:
        choice = random.choice(options)
        board[choice] = n
    else:
        return IndexError


def checkWon(bld):
    Tied = False
    over = False
    win = 0
    if bld[0] == bld[3] and bld[3] == bld[6] and bld[3] != 0:
        over = True
        win = bld[0]
    elif bld[1] == bld[4] and bld[4] == bld[7] and bld[4] != 0:
        over = True
        win = bld[1]
    elif bld[2] == bld[5] and bld[5] == bld[8] and bld[5] != 0:
        over = True
        win = bld[2]
    elif bld[0] == bld[1] and bld[1] == bld[2] and bld[1] != 0:
        over = True
        win = bld[0]
    elif bld[3] == bld[4] and bld[4] == bld[5] and bld[4] != 0:
        over = True
        win = bld[3]
    elif bld[6] == bld[7] and bld[7] == bld[8] and bld[7] != 0:
        over = True
        win = bld[6]
    elif bld[0] == bld[4] and bld[4] == bld[8] and bld[4] != 0:
        over = True
        win = bld[0]
    elif bld[2] == bld[4] and bld[4] == bld[6] and bld[4] != 0:
        over = True
        win = bld[2]
    elif 0 not in bld:
        Tied = True
        over = True
    if Tied is True:
        return 'over = True,{}'.format(win)
    if over is True:
        return 'over = True,{}'.format(win)
    else:
        return 'over = False, 0'


def simBoard(reps, board, n, first):
    WLT = [0, 0, 0]
    for i in range(reps):
        Sboard = []
        for i in board:
            Sboard.append(i)
        Sboard[first] = n
        while True:
            if checkWon(Sboard).split(',')[0] == 'over = True':
                break
            randMove(-n, Sboard)
            if checkWon(Sboard).split(',')[0] == 'over = True':
                break
            randMove(n, Sboard)
        if checkWon(Sboard).split(',')[1] == str(n):
            WLT[0] += 1
        if checkWon(Sboard).split(',')[1] == str(-n):
            WLT[1] += 1
        elif checkWon(Sboard).split(',')[1] is '0':
            WLT[2] += 1
    return WLT


tL = []


def think(n):
    global tL
    if str(GB.build) in Moves.keys():
        pass
    else:
        options = []
        for k in range(9):
            if GB.build[k] == 0:
                options.append(k)
        count = 0
        most = -701
        best = None
        for i in options:
            count = simBoard(700, GB.build, n, i)
            if count[0] - count[1] + count[2] // 10 > most:
                most = count[0] - count[1] + count[2] // 10
                best = i
            if most == 0:
                randMove(n, GB.build)
                return None
        Moves[str(GB.build)] = best
    GB.build[Moves[str(GB.build)]] = n


xo = random.choice([-1, 1])
while True:
    if xo == 1:
        GB.show()
        chose(1)
        if checkWon(GB.build).split(',')[0] == 'over = True':
            GB.show()
            if int(checkWon(GB.build).split(',')[1]) == xo:
                print 'You Won!'
            elif int(checkWon(GB.build).split(',')[1]) == -1 * xo:
                print 'You Lose'
            else:
                print 'Tie game'
            over = True
            break
        GB.show()
        think(-1)
        if checkWon(GB.build).split(',')[0] == 'over = True':
            GB.show()
            if int(checkWon(GB.build).split(',')[1]) == xo:
                print 'You Won!'
            elif int(checkWon(GB.build).split(',')[1]) == -1 * xo:
                print 'You Lose'
            else:
                print 'Tie game'
            over = True
            break
    else:
        GB.show()
        think(1)
        if checkWon(GB.build).split(',')[0] == 'over = True':
            GB.show()
            if int(checkWon(GB.build).split(',')[1]) == xo:
                print 'You Won!'
            elif int(checkWon(GB.build).split(',')[1]) == -1 * xo:
                print 'You Lose'
            else:
                print 'Tie game'
            over = True
            break
        GB.show()
        chose(-1)
        if checkWon(GB.build).split(',')[0] == 'over = True':
            GB.show()
            if int(checkWon(GB.build).split(',')[1]) == xo:
                print 'You Won!'
            elif int(checkWon(GB.build).split(',')[1]) == -1 * xo:
                print 'You Lose'
            else:
                print 'Tie game'
            over = True
            break
