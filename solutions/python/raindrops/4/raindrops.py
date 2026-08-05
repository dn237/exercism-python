def Convert_dict(number):
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
    