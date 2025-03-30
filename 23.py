from itertools import product
k = 0
words=product('01234567', repeat=5)
for x in words:
    s=''.join(x)
    if s[0]!='0' and s.count('6')==1:
        s=s.replace('1','*').replace('3','*').replace('5','*').replace('7','*')
        if '*6' not in s and '6*' not in s:
            k+=1

print(k)
