# bincon_loop.py | iml cwc
# convert a base 10 number to binary
# use 191 base 10 equal to 1011 1111 base
# q(quotient) d(divisor) r(remainder) n(integer input)

n = int(input("Input an integer less than 256: "))
n_og = n
d = 128
binString = ""            #create a stirng called binString

for i in range(0, 8):
    q = int(n / d)
    r = int(n % d)
    #print(d, q, r)        #debug line
    n = r
    d = int(d / 2)
    binString = binString + str(q)
    
    if i == 3:
        binString = binString + " "

print(binString)
