def addition(*args):
    return sum(args)

def subtraktion(*args):
    result = args[0]
    for arg in args[1:]:
        result = result - arg

    return result

def multiplikation(*args):
    result = args[0]
    for arg in args[1:]:
        result = result * arg

    return result

def division(*args):
    result = args[0]
    for arg in args[1:]:
        result = result / arg

    return result    


def taschenrechner(rechenart, *args):
    result = None
    if rechenart == addition:
        result = addition(*args)
    elif rechenart == subtraktion:
        result = subtraktion(*args)
    elif rechenart == multiplikation:
        result = multiplikation(*args)
    elif rechenart == division:
        result = division(*args)
    else:
        return 0
    
    return result

print(taschenrechner(addition, 1,2,3,4,5))