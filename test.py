import linecache
line = linecache.getline(r"database.txt", 1)
print(len(line))