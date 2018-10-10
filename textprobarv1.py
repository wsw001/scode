import math
import time
import sys
import threading

def textbar(modeNo):
    x=0.1
    str1='x'
    str2='x+(1-math.sin(x*math.pi*2+math.pi/2)/-8)'
    str3='x+(1-math.sin(x*math.pi*2+math.pi/2)/8)'
    str4='x + math.sin(x * math.pi * 5) / 20'
    str5='x + math.sin(x * math.pi * 20) / 80'
    str6='(x + (1 - x) * 0.03)**2'
    str7='1 + (1 - x)**2'
    str8='(x + (1 - x) / 2) ** 8'
    str9='1 + (1 - x)**(3)'
    wd=100
    print("\n")
    print("Begin%s".center(105,'=')%(str(modeNo)))
    start=time.perf_counter()
    choice='str'+str(modeNo)
    for i in range(101):
        a=chr(9617)*i
        b='.'*(wd-i)
        end=time.perf_counter()
        stu=end-start
        x=eval(eval(choice))
        print("\r{0}%[{1}{2}]{3:.2f}s".format(i,a,b,stu),end='')
        time.sleep(x/10)
    print("\n"+"END%s".center(105,'=')%(str(modeNo)))
    print("\n")

if __name__ == '__main__':
    time.sleep(1)
    sys.stdout.flush()
    choice1,choice2=eval(input("Enter number range,START:(1-9)"))

    for i in range(choice1,choice2):
        t=threading.Thread(target=textbar,args=(i,))
        t.start()
        #t.join()

