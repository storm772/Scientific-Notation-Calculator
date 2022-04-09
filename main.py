# Main function
def calc(n):
    isAlready = False

    if '10^' in n:
        isAlready = True
    # Scientific Notation Fixer
    if isAlready:
        target = n.split('x')[0].replace(',','')
        exponent = int(n.split('^')[1])
        
        found = 0
        decimal = False
        
        if target[0] == '0': decimal = True
        else: decimal = False

        if decimal == True:
            zeroCount = 0
            found = target.lstrip('0')
            if int(found) > 10:
                number = found[:1] + '.' + found[1:]
                found = target[:1] + '.' + target[1:]
                
            for i in target:
                if i == '0':
                    zeroCount -=1

            print(f'Zeros: {zeroCount}')
            print(f'Target: {target}')
            print(f'Number: {number}')
            print(f'{number}x10^{exponent + zeroCount}')
            
        if decimal == False:
            found = target.rstrip('0')
            if int(found) > 10:
                number = found[:1] + '.' + found[1:]
                found = target[:1] + '.' + target[1:]

                print(f'{number}x10^{len(found.split(".")[1]) + exponent}')
            else:
                zeroCount = 0
                for i in target:
                    if i == '0':
                        zeroCount +=1
                else:
                    print(f'{target.split("0")[0]}x10^{zeroCount}')
    else:
        if ',' in n:
            n = n.replace(',','')
        if '.' in n:
            n = n.replace('.','')
        if ' ' in n:
            n = n.replace(' ','')
            
        # Convert To Scientific Notation
        if n[0] == '0':
            zeroCount = 0
            number = n.lstrip('0')
            if int(number) > 10:
                number = number[:1] + '.' + number[1:]
            for i in n:
                if i == '0':
                    zeroCount += 1
                if i != '0':
                    break
            print(f'{number}x10^{zeroCount}')
            
        elif n[0] != '0':
            number = n#.rstrip('0')
            if int(number) > 10:
                number = number[:1] + '.' + number[1:]
            zeroCount = len(number.split('.')[1])
            print(f'{number.rstrip("0")}x10^{zeroCount}')
            #   check = input('Do you want to check if its correct?\n~> ')
            #   if check == 'yes':
            #       checkValue = float(number.rstrip("0"))*10**int(zeroCount)
            #       print(f'Requested: {n}\nResult: {str(checkValue).replace(".0", "")}\nIdentical: {int(n) == checkValue}')
            
calc('545550000')
