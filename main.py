"""
This file contains scripts to resolve problems on turing.nymphomath.ch. Please don't use this to cheat and just for educational purpose, verification and/or help.
TheSwagMan - Thomas POTIER <theswagman@gmx.fr>
"""

####################
# FUNCTIONS        #
####################
def syracuse(n):
    r = []
    while n > 1:
        if n % 2 == 0:
            r.append(n)
            n //= 2
        else:
            n = 3 * n + 1
    r.append(1)
    return r


def rotate(n):
    return int(str(n)[-1] + str(n)[:-1])

def syracuse_len(n):
    l = 1
    while n > 1:
        if n % 2 == 0:
            l += 1
            n //= 2
        else:
            n = 3 * n + 1
    return l

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_palindrom(n):
    s = str(n)
    l = len(s)
    if l % 2 != 0:
        return int(s[:l // 2]) == mirror(s[l // 2 + 1:])
    return int(s[:l // 2]) == mirror(s[l // 2:])


def sum_of_nums(n):
    return sum([int(e) for e in str(n)])


def facto(n):
    r = 1
    for i in range(2, n):
        r *= i
    return r * n

def mirror(n):
    return int(str(n)[::-1])


def factorial_sum(n):
    s = 0
    for c in str(n):
        s += facto(int(c))
    return s


def diastern(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if n % 2 == 0:
            return diastern(int(n / 2))
        else:
            return diastern((n - 1) / 2) + diastern((n - 1) / 2 + 1)

####################
# MAIN PROG        #
####################

"""
# 1
somme=0
for i in range(2013):
    if i%5==0 or i%7==0:
        somme+=i
print(1,somme)

# 2
s=0
a=0
b=1
c=1
while c<4000000:
    if c%2==0:
        s+=c
    a=b
    b=c
    c=a+b
print(2,s)

# 3
n=20130101
for i in range(n):
    if n%((n//2)-i)==0:
        if is_prime((n//2)-i):
            break
print(3,(n//2)-i)


# 4
palindroms=[]
for i in range(10**3-1,10**2,-1):
    for j in range(10**4-1,10**3,-1):
        if is_palindrom(i*j):
            palindroms.append(i*j)
print(4,max(palindroms))

# 5
print(5,sum_of_nums(2**2222))

# 6
print(6,sum_of_nums(facto(2013)))

# 7
i=2
a=1
while a<23456:
    i+=1
    if is_prime(i):
        a+=1
print(7,i)

# 10
s=0
for i in range(2,10000000):
    if is_prime(i):
        s+=i
print(10,s)

# 11
n=10000000
for i in range(n):
    k=n-i
    if mirror(k)==4*k:
        break
print(11,k)

# 13
a = 836
while True:
    a += 1
    if is_palindrom(a ** 2) and len(str(a**2))%2==0:
        break
print(13, a ** 2)


# 14
maxi = 0
maxl = 0
for i in range(1500000):
    k = syracuse_len(i)
    if k > maxl:
        maxl = k
        maxi = i
print(14, maxi)

# 19
sum=0
for i in range(2013):
    if (i%(2*6)==1 or i%(2*6)==2*6-1) and (i%(2*7)==1 or i%(2*7)==2*7-1):
        sum+=i+1
print(19,sum)

# 25
b=0
c=1
i=1
while len(str(c))<2013:
    i+=1
    k=b+c
    b=c
    c=k
print(25,i)


# 34 ERROR !!!
s=0
c=3
while c<1000000:
    if c==factorial_sum(c):
        s+=c
    c+=1
print(34,s)

# 48
s=0
for i in range(1,2014):
    s+=i**i
print(48,str(s)[:10])

# 67
print(67,diastern(10000001))

# 70
s=0
for i in range(10**5,10**6):
    b=rotate(i)
    if i!=b and len(str(b))==6:
        if b%i==0:
            s+=i
print(70,s)
"""  # SUPER COMMENTER """
