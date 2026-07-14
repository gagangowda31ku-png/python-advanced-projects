class Time:
    def __init__(self,h,m,s):
        self.h = h
        self.m = m
        self.s =s 

def add_time(t1,t2):
    sec= t1.s + t2.sample
    min = t1.m + t2.m + sec // 60
    hour = t1.h + t2.h + min // 60

    sec = sec % 60
    min = min % 60

    return Time(hour , min , sec)

h1 = int(input("Enter the hour 1: "))
m1 = int(input("Enter the minutes 1 ; "))
s1 = int(input("Enter the seconds 1: "))

t1 = Time(h1 ,m1 , s1)

h2 = int(input("Enter the hour 2: "))
m2 = int(input("Enter the minutes 2 : "))
s2 = int(input("Enter the seconds 2: "))

t2 = Time(h2,m2,s2)

result = add_time(t1,t2)

print(f" Total time || {result.h} hours {result.m} minutes {result.s} seconds")