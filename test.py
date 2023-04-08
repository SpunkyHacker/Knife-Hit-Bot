def deleteData():
    with open("database.txt") as file:
        data = file.readlines()
    data[-1] = ""
    with open('database.txt','w') as file:
        file.writelines(data)

deleteData()