import turtle as t
#0->1->1+4->1+4+16->1+4+16+64
#0->3분의1->9분의1
#->2->4->16
#->2->3->4
def for_Koch(dist, depth):
    flag = 0
    flag2 = 0
    flag3 = 0
    if(depth == 0):
        t.forward(dist)
    if(depth == 1):
        max = 1
        length = dist/3**depth
        t.forward(length)
        t.left(60)
        t.forward(length)
        t.right(120)
        t.forward(length)
        t.left(60)
        t.forward(length)
    else:
        max = 4**(depth-1)+1
    for i in range(1, max):
        length = dist/3**depth
        t.forward(length)
        t.left(60)
        t.forward(length)
        t.right(120)
        t.forward(length)
        t.left(60)
        t.forward(length)
        if(i%2 == 1):
            t.left(60)
        elif(i%64 == 0 and flag3 == 0):
            t.left(60)
            flag3 = 1
            flag2 = 0
            flag = 0
        elif(i%64 == 0 and flag3 == 1):
            t.right(120)
            flag3 = 0
            flag2 = 0
            flag = 0
        elif(i%16 == 0 and flag2 == 0):
            t.left(60)
            flag2 = 1
            flag = 0
        elif(i%16 == 0 and flag2 == 1):
            t.right(120)
            flag2 = 0
            flag = 0
        elif(i%4 == 0 and flag == 0):
            t.left(60)
            flag = 1
        elif(i%4 == 0 and flag == 1):
            t.right(120)
            flag = 0
        else:
            t.right(120)
t.speed(0)
for_Koch(500,5)#5까지 동작확인
