# def appendDatabase(linenum , time):
#     with open("database.txt") as file:
#         lines = file.readlines()

#     if (linenum <= len(lines)):
#         lines[linenum - 1] = time + "\n"
#         with open('database.txt', "w") as f:
#             f.writelines(lines)
#     else:
#         with open("database.txt",'a') as file:
#             file.write(str(time)+"\n")

# appendDatabase(15,"69")

def appendDatabase(linenum , time):
    with open("database.txt") as file:
        data = file.readlines()
    try:
        data[linenum -1] = str(time) + "\n"
        with open("database.txt", 'w') as file:
            file.writelines(data)
    except IndexError:
        with open("database.txt",'a') as file:
            file.write(str(time)+"\n")
    print('appended the time:',time)

appendDatabase(6,6969)