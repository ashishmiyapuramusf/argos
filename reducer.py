import sys
n = 0
s = 0
#Read standard input
for i in sys.stdin:
    try:
        number = i.strip().split()[0]
        count = i.strip().split()[1]
        s_temp = int(number)
        n_temp = int(count)
        n = n + n_temp
        s = s + s_temp
    except ValueError:
        pass
print( float(summation) / float(count) )
