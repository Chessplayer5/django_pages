import csv

file = open("mpg.csv")

student_name = "Matthew Ding"

mpg_reader = csv.reader(file)

sum_city = 0
num_auto = 0
sum_suv = 0
num_suv = 0
sum_hwy = 0
num_autom = 0
sum_ford = 0
num_ford = 0


next(mpg_reader)


for row in mpg_reader:

    sum_hwy += int(row[9])
    num_autom += 1
    if row[1] == "ford":
        sum_ford += int(row[9])
        num_ford += 1

    sum_city += int(row[8])
    num_auto += 1
    if row[-1] == "suv":
        sum_suv += int(row[8])
        num_suv += 1


file.close()

out_file = open("mding1_assignment4.txt", "w")

avg_city = sum_city / num_auto
# print(avg_city)
out_file.write("The avg_city is: " + str(avg_city) + "\n")


avg_hwy = sum_hwy / num_autom
# print(avg_hwy)
out_file.write("The avg_hwy is: " + str(avg_hwy) + "\n")

ford_hwy = sum_ford / num_ford
# print(avg_ford)
out_file.write("The ford_hwy is: " + str(ford_hwy) + "\n")


suv_city = sum_suv / num_suv
# print(avg_suv)
out_file.write("The suv_city is: " + str(suv_city))

out_file.close()
