file = open("text_file.txt", "r")

line_ct = 0
for line in file:
    print(line)
    line_ct += 1

file.close()
