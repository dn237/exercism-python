def convert(number):
    """Function that converts a number into its corresponding raindrop sounds."""
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

    
#print(convert(34))


def convertDict(number):
    """Second Option of raindrop converter. Used dictionary to store rules(data) """
    rules = {
        3 : 'Pling',
        5 : 'Plang',
        7 : 'Plong'
            }

    result = ''

    for divisor, sound in rules.items():
        if number % divisor == 0:
            result += sound

    # Returns 'result' if it evaluates to True (not empty), else return the number as a string.
    return result if result else str(number)

print(convertDict(10))
    