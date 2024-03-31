x = 3338
y = 2866
w = 1825
z = 3816
M = 9566707
d = 36506556778
e = 17459243613
n = 66624478857659

c = [35784176028369,
63561241316534,
40946911928892,
56405696498538,
38978109180990,
16444276162313,
38053979586003,
57562671757853]

decoded_msg = ""
for number in c:
    decoded_line = (number*d)%n
    byte_string = decoded_line.to_bytes((decoded_line.bit_length() + 7) // 8, byteorder='big')
    line = byte_string.decode('utf-8')
    line_without_null = ''.join(char for char in line if char != '\x00')
    decoded_msg += line_without_null
print(decoded_msg)