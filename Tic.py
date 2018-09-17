import time
import random
draw = {
    -1:"X  |",
    0: "   |",
    1: "O  |"
}
class Spot:
    def __init__(self, x, y, n):
        self.x = x
        self.y = y
        self.n = n
    
    def text(self):
        return draw[self.n]

    def __str__(self):
        return text(self)
        
class Board:
    def __init__(self, l, w):
        self.l = l
        self.w = w
        self.build = []
        R = []
        for i in range(self.l):
            for j in range(self.w):
                R.append(0)
        self.build.extend(R)
    
    def change(self, x, y, n):
        self.build[3*y+x] = n
        
    def show(self):
        for i in range(20):
            print ''
        for i in range(self.l):
            print " -----+-----+-----"
            txt ='|  '
            for j in range(self.w):
                inst = Spot(i, j, self.build[i*3+j])
                txt += inst.text()
                txt += "  "
            print txt
        print " -----+-----+-----"
GB = Board(3, 3)

GB.show()

def chose(n):
    while 1>0:
        c = input('Which square would you like?')
        try:
            if GB.build[c] != 0:
                print 'pick again'
            else:
                GB.build[c] = n
                break
        except IndexError:
            pass
def rot(n,r):
    y = (n / 3)
    x = n%3 
    if r == 2:
        y,x = x, 2-y
    if r == 3:
        y,x = 2-x, 2-y
    if r == 4:
        y,x = 2-x, y
    if r == 5:
        y,x = y, x
    if r == 5:
        y,x = y, 2-x
    if r == 6:
        y,x = 2-y, 2-x
    if r == 7:
        y,x = 2-y, x
    return 3*y+x
r = random.choice([1,2,3,4])
def they(turns,n):
    Turn = True
    while Turn != False:
        if turns == 0:
            if GB.build[4] == 0:
                GB.build[4] = n
                turns += 1
                Turn = False
                break
            else:
                GB.build[rot(0,r)] = n
                turns += 1
                Turn = False
                break
        if turns > 0 and GB.build[4] == -n:
            if GB.build[0] == GB.build[2] and GB.build[1] == 0 and GB.build[0] != 0:
                GB.build[1] = n
                Turn = False
            elif GB.build[0] == GB.build[6] and GB.build[3] == 0 and GB.build[0] != 0:
                GB.build[3] = n
                Turn = False
            elif GB.build[8] == GB.build[6] and GB.build[7] == 0 and GB.build[8] != 0:
                GB.build[7] = n
                Turn = False
            elif GB.build[8] == GB.build[2] and GB.build[5] == 0 and GB.build[8] != 0:
                GB.build[5] = n
                Turn = False
            elif GB.build[5] == GB.build[4] and GB.build[3] == 0:
                GB.build[3] = n
                Turn = False
            elif GB.build[2] == GB.build[4] and GB.build[6] == 0:
                GB.build[6] = n
                Turn = False
            elif GB.build[1] == GB.build[4] and GB.build[7] == 0:
                GB.build[7] = n
                Turn = False
            elif GB.build[0] == GB.build[4] and GB.build[8] == 0:
                GB.build[8] = n
                Turn = False
            elif GB.build[3] == GB.build[4] and GB.build[5] == 0:
                GB.build[5] = n
                Turn = False
            elif GB.build[6] == GB.build[4] and GB.build[2] == 0:
                GB.build[2] = n
                Turn = False
            elif GB.build[7] == GB.build[4] and GB.build[1] == 0:
                GB.build[1] = n
                Turn = False
            elif GB.build[8] == GB.build[4] and GB.build[0] == 0:
                GB.build[0] = n
                Turn = False
            else: 
                if GB.build[0] == 0:
                    GB.build[0] = n
                    Turn = False
                elif GB.build[2] == 0:
                    GB.build[2] = n
                    Turn = False
                elif GB.build[8] == 0:
                    GB.build[8] = n
                    Turn = False
                elif GB.build[6] == 0:
                    GB.build[6] = n
                    Turn = False
                else:
                    them(n)
                    Turn = False
        if turns > 0 and GB.build[4] == n:
            if GB.build[0] == n and GB.build[8] == 0:
                GB.build[8] = n
                Turn = False
            elif GB.build[3] == n and GB.build[5] == 0:
                GB.build[5] = n
                Turn = False
            elif GB.build[6] == n and GB.build[2] == 0:
                GB.build[2] = n
                Turn = False
            elif GB.build[7] == n and GB.build[1] == 0:
                GB.build[1] = n
                Turn = False
            elif GB.build[8] == n and GB.build[0] == 0:
                GB.build[0] = n
                Turn = False
            elif GB.build[5] == n and GB.build[3] == 0:
                GB.build[3] = n
                Turn = False
            elif GB.build[2] == n and GB.build[6] == 0:
                GB.build[6] = n
                Turn = False
            elif GB.build[1] == n and GB.build[7] == 0:
                GB.build[7] = n
                Turn = False
            elif GB.build[0] == GB.build[2] and GB.build[1] == 0 and GB.build[0] != 0:
                GB.build[1] = n
                Turn = False
            elif GB.build[0] == GB.build[6] and GB.build[3] == 0 and GB.build[0] != 0:
                GB.build[3] = n
                Turn = False
            elif GB.build[8] == GB.build[6] and GB.build[7] == 0 and GB.build[8] != 0:
                GB.build[7] = n
                Turn = False
            elif GB.build[8] == GB.build[2] and GB.build[5] == 0 and GB.build[8] != 0:
                GB.build[5] = n
                Turn = False

            elif GB.build[0] == GB.build[1] and GB.build[0] != 0 and GB.build[2] == 0:
                GB.build[2] = n
                Turn = False
            elif GB.build[0] == GB.build[3] and GB.build[0] != 0 and GB.build[6] == 0:
                GB.build[6] = n
                Turn = False
            elif GB.build[6] == GB.build[3] and GB.build[6] != 0 and GB.build[0] == 0:
                GB.build[0] = n
                Turn = False
            elif GB.build[6] == GB.build[7] and GB.build[6] != 0 and GB.build[8] == 0:
                GB.build[8] = n
                Turn = False
            elif GB.build[8] == GB.build[7] and GB.build[8] != 0 and GB.build[6] == 0:
                GB.build[6] = n
                Turn = False
            elif GB.build[8] == GB.build[5] and GB.build[8] != 0 and GB.build[2] == 0:
                GB.build[2] = n
                Turn = False
            elif GB.build[2] == GB.build[5] and GB.build[2] != 0 and GB.build[8] == 0:
                GB.build[8] = n
                Turn = False
            elif GB.build[2] == GB.build[1] and GB.build[1] != 0 and GB.build[0] == 0:
                GB.build[0] = n
                Turn = False
            elif GB.build[1] == GB.build[3] and GB.build[1] != 0 and GB.build[0] == 0:
                GB.build[0] = n
                Turn = False
            elif GB.build[1] == GB.build[5] and GB.build[1] != 0 and GB.build[2] == 0:
                GB.build[2] = n
                Turn = False
            elif GB.build[5] == GB.build[7] and GB.build[5] != 0 and GB.build[8] == 0:
                GB.build[8] = n
                Turn = False
            elif GB.build[3] == GB.build[7] and GB.build[3] != 0 and GB.build[6] == 0:
                GB.build[6] = n
                Turn = False

            elif GB.build[0] == GB.build[5] and GB.build[0] != 0 and GB.build[2] == 0:
                GB.build[2] = n
                Turn = False
            elif GB.build[0] == GB.build[7] and GB.build[0] != 0 and GB.build[6] == 0:
                GB.build[6] = n
                Turn = False
            elif GB.build[2] == GB.build[3] and GB.build[2] != 0 and GB.build[0] == 0:
                GB.build[0] = n
                Turn = False
            elif GB.build[6] == GB.build[1] and GB.build[6] != 0 and GB.build[0] == 0:
                GB.build[0] = n
                Turn = False
            elif GB.build[6] == GB.build[5] and GB.build[6] != 0 and GB.build[8] == 0:
                GB.build[8] = n
                Turn = False
            elif GB.build[8] == GB.build[1] and GB.build[8] != 0 and GB.build[2] == 0:
                GB.build[2] = n
                Turn = False
            elif GB.build[8] == GB.build[3] and GB.build[8] != 0 and GB.build[6] == 0:
                GB.build[6] = n
                Turn = False
            elif GB.build[0] == GB.build[8] and GB.build[0] != 0 and GB.build[1] == 0:
                GB.build[1] = n
                Turn = False
            elif GB.build[2] == GB.build[6] and GB.build[2] != 0 and GB.build[1] == 0:
                GB.build[1] = n
                Turn = False

            else: 
                if GB.build[0] == 0:
                    GB.build[0] = n
                    Turn = False
                elif GB.build[2] == 0:
                    GB.build[2] = n
                    Turn = False
                elif GB.build[8] == 0:
                    GB.build[8] = n
                    Turn = False
                elif GB.build[6] == 0:
                    GB.build[6] = n
                    Turn = False
                else:
                    them(n)
                    Turn = False

def them(n):
    while 1>0:
        c = random.randint(0,8)
        if GB.build[c] != 0:
            pass
        else:
            GB.build[c] = n
            break

text = {
    1: 'you win!',
    -1: 'you lose'
}

over  = False
t = 0
f = 1
#if f == 1:
    #print 'You go first'
#if f == 2:
    #print "I'll go first"
xo = random.choice([-1,1])
diff = 1
while over == False:
    if f == 2:
        d = random.random()
        #time.sleep(.5)
        if d<=diff:
            they(t,xo)
        if d>diff:
            them(xo)
        GB.show()
    if f == 1:
        print ''
        print '   0     1     2 '
        print ''
        print '   3     4     5 '
        print ''
        print '   6     7     8 '
        print 'player 1:'
        chose(1)
        GB.show()
        for i in range(7):
            print ''
    if GB.build[0] ==  GB.build[3] and GB.build[3] == GB.build[6] and GB.build[3] != 0: 
        print text[GB.build[3]]
        over = True
        break
    if GB.build[1] ==  GB.build[4] and GB.build[4] == GB.build[7] and GB.build[4] != 0: 
        print text[GB.build[4]]
        over = True
        break
    if GB.build[2] ==  GB.build[5] and GB.build[5] == GB.build[8] and GB.build[5] != 0: 
        print text[GB.build[5]]
        over = True
        break
    if GB.build[0] ==  GB.build[1] and GB.build[1] == GB.build[2] and GB.build[1] != 0: 
        print text[GB.build[1]]
        over = True
        break
    if GB.build[3] ==  GB.build[4] and GB.build[4] == GB.build[5] and GB.build[4] != 0: 
        print text[GB.build[4]]
        over = True
        break
    if GB.build[6] ==  GB.build[7] and GB.build[7] == GB.build[8] and GB.build[7] != 0: 
        print text[GB.build[7]]
        over = True
        break
    if GB.build[0] ==  GB.build[4] and GB.build[4] == GB.build[8] and GB.build[4] != 0: 
        print text[GB.build[4]]
        over = True
        break
    if GB.build[2] ==  GB.build[4] and GB.build[4] == GB.build[6] and GB.build[4] != 0: 
        print text[GB.build[4]]
        over = True
        break
    if GB.build[0]!=0 and GB.build[1]!=0 and GB.build[2]!=0 and GB.build[3]!=0 and GB.build[4]!=0 and GB.build[5]!=0 and GB.build[6]!=0 and GB.build[7]!=0 and GB.build[8]!=0:
        print 'Tied :/'
        over = True
        break
    if f == 1:
        d = random.random()
        time.sleep(.5)
        if d <= diff:
            they(t,-1)
        if d > diff:
            them(-1)
        GB.show()
    if f == 2:
        print ''
        print '   0     1     2 '
        print ''
        print '   3     4     5 '
        print ''
        print '   6     7     8 '
        print 'player 2:'
        chose(-1)
        GB.show()
        for i in range(7):
            print ''
    if GB.build[0] ==  GB.build[3] and GB.build[3] == GB.build[6] and GB.build[3] != 0: 
        print text[GB.build[3]]
        over = True
        break
    if GB.build[1] ==  GB.build[4] and GB.build[4] == GB.build[7] and GB.build[4] != 0: 
        print text[GB.build[4]]
        over = True
        break
    if GB.build[2] ==  GB.build[5] and GB.build[5] == GB.build[8] and GB.build[5] != 0: 
        print text[GB.build[5]]
        over = True
        break
    if GB.build[0] ==  GB.build[1] and GB.build[1] == GB.build[2] and GB.build[1] != 0: 
        print text[GB.build[1]]
        over = True
        break
    if GB.build[3] ==  GB.build[4] and GB.build[4] == GB.build[5] and GB.build[4] != 0: 
        print text[GB.build[4]]
        over = True
        break
    if GB.build[6] ==  GB.build[7] and GB.build[7] == GB.build[8] and GB.build[7] != 0: 
        print text[GB.build[7]]
        over = True
        break
    if GB.build[0] ==  GB.build[4] and GB.build[4] == GB.build[8] and GB.build[4] != 0: 
        print text[GB.build[4]]
        over = True
        break
    if GB.build[2] ==  GB.build[4] and GB.build[4] == GB.build[6] and GB.build[4] != 0: 
        print text[GB.build[4]]
        over = True
        break
    if GB.build[0]!=0 and GB.build[1]!=0 and GB.build[2]!=0 and GB.build[3]!=0 and GB.build[4]!=0 and GB.build[5]!=0 and GB.build[6]!=0 and GB.build[7]!=0 and GB.build[8]!=0:
        print 'Tied :/'
        over = True
        break
    t+=1