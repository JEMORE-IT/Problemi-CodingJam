input = []

e=17459243613
n=66624478857659
msg = [35784176028369,
       63561241316534,
       40946911928892,
       56405696498538,
       38978109180990,
       16444276162313,
       38053979586003,
       57562671757853]

# c = e*m % n (encription)
inv = pow(e, -1, n) # e*inv = 1 % n
# print(inv)
# print(inv * e % n)

decoded_msg = ""
for c in msg: 
    m = inv * c % n
    decoded_msg += (bytearray.fromhex(hex(m)[2:]).decode())

print(decoded_msg)

    

