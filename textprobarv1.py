import math
import time

def textbar(modeNo):
    x=0.1
    str1=' x'
    str2=' x+(1-math.sin(x*math.pi*2+math.pi/2)/-8)'
    str3=' x+(1-math.sin(x*math.pi*2+math.pi/2)/8)'
    str4=' x + math.sin(x * math.pi * 5) / 20'
    str5=' x + math.sin(x * math.pi * 20) / 80'
    str6=' (x + (1 - x) * 0.03)**2'
    str7= ' 1 + (1 - x)**2'
    str8=' (x + (1 - x) / 2) ** 8'
    str9=' 1 + (1 - x)**(3)'
    wd=100
    print("Begin".center(105,'='))
    start=time.perf_counter()
    choice='str'+str(modeNo)
    for i in range(101):
        a=chr(9617)*i
        b='.'*(wd-i)
        end=time.perf_counter()
        stu=end-start
        x=eval(eval(choice))
        print("\r{0}%[{1}{2}]{3:.2f}s -{4:.2f}".format(i,a,b,stu,x),end='')
        time.sleep(x/10)
    print("\n"+"END".center(105,'='))
    print("\n")

if __name__ == '__main__':
    enter=int(input("Enter one text-proc-mod(1-9):"))
    textbar(enter)

