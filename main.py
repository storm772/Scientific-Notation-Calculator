def calc(n):
    parts = n.replace('*','x').split('x10^')
    number = parts[0]
    # Scientific Notation Fixer
    if len(parts) == 2:
        exponent = int(parts[1])
        # Decimal
        if number[0] == '0':
            zeroCount = 0
            for i in number:
                if i == '0': zeroCount -= 1
                if i != '0': break 
            
            found = number.lstrip('0')
            if int(found) > 10:     found = f'{found[:1]}.{found[1:]}'
            
            print(f'{found}x10^{zeroCount + exponent}')
        # Integer   
        else:
            found = number.rstrip('0')
            if int(found) > 10:     
                found = f'{number[:1]}.{number[1:]}'
                print(f'{found.rstrip("0")}x10^{len(found.split(".")[1]) + exponent}')
            else:
                print('hi')

    elif len(parts) == 1:
        # Decimal
        if number[0] == '0':
            zeroCount = 0
            value = number.lstrip('0')

            if int(value) > 10:
                value = f'{value[:1]}.{value[1:]}'

            for i in number:
                if i == '0': zeroCount -= 1
                if i != '0': break 
            
            print(f'{value}x10^{zeroCount}')
        # Integer
        else:
           
            if int(number) > 10:
                number = number[:1] + '.' + number[1:]
                temp = number.rstrip('0')
            print(f'{temp}x10^{len(number.split(".")[1])}')

calc('720000')
