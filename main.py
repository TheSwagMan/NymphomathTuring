####################
# FUNCTIONS        #
####################
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

"""  # SUPER COMMENTER """
# 14
