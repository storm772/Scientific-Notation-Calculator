# Main function
def calc(n):

    # Scientific Notation Fixer
    if '10^' in n:
        target = n.split('x')[0].replace(',','')
        exponent = int(n.split('^')[1])
        
        # Decimal System
        if target[0] == '0': 
            zeroCount = 0
            for i in target:
                if i == '0': zeroCount -= 1
                if i != '0': break

            found = target.lstrip('0')

            if int(found) > 10:
                found = found[:1] + '.' + found[1:]
            print(f'{found}x10^{zeroCount + exponent}')
            
        else: 
        # Integer System
            found = target.rstrip('0')
            if int(found) > 10:
                number = found[:1] + '.' + found[1:]
                found = target[:1] + '.' + target[1:]

                print(f'{number}x10^{len(found.split(".")[1]) + exponent}')
            else:
                zeroCount = 0
                for i in target:
                    if i == '0': zeroCount += 1
                    if i != '0': break
                
                print(f'{target.split("0")[0]}x10^{zeroCount}')
    
    # Scientific Notation Converter
    if '10^' not in n: 
        n = n.replace(' ','').replace(',','').replace('.','')
        
        # Decimal System
        if n[0] == '0':
            zeroCount = 0
            number = n.lstrip('0')
            if int(number) > 10:
                number = number[:1] + '.' + number[1:]
            for i in n:
                if i == '0': zeroCount -= 1
                if i != '0': break

            print(f'{number}x10^{zeroCount}')
            
        # Integer System
        elif n[0] != '0':
            if int(n) > 10:
                n = n[:1] + '.' + n[1:]
            print(f'{n.rstrip("0")}x10^{len(n.split(".")[1])}')
        else:
            print('Invalid Operation')

calc('0.000003367')
