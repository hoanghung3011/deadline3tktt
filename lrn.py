import random
import cProfile
def lrn(array,l,r):
    if l == r:
        # print(array[l])
        return
    if r == l + 1:
        # print(array[l])
        # print(array[l+1])
        return
    if l > r:
        return
    t = int((l+r)/2)
    lrn(array,l,t-1)
    lrn(array,t+1,r)
    # print(array[t])
    return

for n in range(100,10000,350):
    b = []
    for i in range(0,n):
        n = random.choice(range(0, 101))
        b.append(n)
    print(len(b))
    cProfile.run('[lrn(b,0,len(b)-1) for i in range(100)]')
    b.clear()
# for i in range(0,n):
#     n = random.choice(range(0, 101))
#     b.append(n)
# cProfile.run('[lrn(b,0,len(b)-1) for i in range(10)]')