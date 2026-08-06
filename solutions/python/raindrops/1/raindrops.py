def convert(number):
    result = ''
    divide = (3, 5, 7)
    for num in divide:
        if number % num == 0:
            match num:
                case 3:
                    result +='Pling'
                case 5:
                    result +='Plang'
                case 7:
                    result +='Plong'
    if result == '':
        return str(number)
    
    return result

    
print(convert(34))
