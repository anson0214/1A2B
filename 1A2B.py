#1A2B
import random
ans = set({})
while len(ans) < 4:
    ans.add(random.randint(1,9))
list(ans)
anslist = list(map(lambda x: str(x), list(ans)))
def inerror(x):
    while True:
        try:
            int(x)
            if type(int(x)) == int and len(set(x)) == 4 and len(x) == 4:
                break
            else:
                x = input("請輸入四個不同數字 = ")
        except:
            x = input("請輸入四個不同數字 = ")
    return x
guess = input("猜測的密碼 = ")
correctguess = inerror(guess)
c = list(correctguess)
a = 0
b = 0
while c != anslist:
    for i in range(4):
        if c[i] == anslist[i]:
            a += 1
        else:
            pass
        if c[i] in anslist and c[i] != anslist[i]:
            b += 1
    print(f"{a}A{b}B")
    a = 0
    b = 0
    guess = input("重新猜測的密碼 = ")
    correctguess = inerror(guess)
    c = list(correctguess)
print("恭喜答對，答案為 : ", anslist)
