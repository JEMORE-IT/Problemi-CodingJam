from textwrap import wrap

e = 17459243613 
n = 66624478857659
ciphertext = """
35784176028369
63561241316534
40946911928892
56405696498538
38978109180990
16444276162313
38053979586003
57562671757853
""".strip()

cs = [int(x.strip()) for x in ciphertext.splitlines()]

inverse = pow(e, -1, n)

message_dec = []
for c in cs:
    m = inverse*c%n
    m_hex = f'{m:02x}'
    message_dec += [int(x, 16) for x in wrap(m_hex, 2)]

print(''.join([chr(x) for x in message_dec]))
