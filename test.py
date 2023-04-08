def checkDatabase(linenum): #OK
    with open('database.txt') as file:
        data = file.readlines()
    try:
        if len(data[linenum-1]) > 0:
            print(len(data[linenum-1]))
            return True
        else:
            return False    
    except IndexError:
        return False
    
print(checkDatabase(0))