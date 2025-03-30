lines: list[str] = []
with open("input.txt", "r") as f:
    lines = f.readlines()[1:-2]

good_bytes = [ 0x13, 0x37, 0x2a, 0xb1]
bad_bytes = [ 0x11, 0x42, 0x00 ]

for line in lines:
    data = line[line.index('TO ') + 3 : line.index(' (')].split(': ')
    hex = data[1]
    
    if hex.startswith("4445445a") and hex.endswith("4e555453") and len(hex) == 64:
        grouped = [hex[i:i+2] for i in range(0, len(hex), 2)]
        
        good_count = 0
        bad = False
        for i in range(len(grouped)): # always 32
            if i != len(grouped)-1 and grouped[i] == grouped[i+1]:
                bad = True
                break
            
            b = int(grouped[i], 16)
            if b in good_bytes:
                good_count += 1
            if b in bad_bytes:
                bad = True
                break
        
        if good_count >= 3 and not bad:
            print(line)
        
