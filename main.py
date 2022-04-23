# Sorting


# 1. find max, min value in the list 
# input: [74, 50, 30, 10, 23, 112, 39, 20, 23, 42, 3]
# output: "max value is 112, min value is 3"

my_list = [74, 50, 30, 10, 23, 112, 39, 20, 23, 42, 3]
print(my_list)

my_min = 987654321

for n in my_list:
  if n < my_min:
    my_min = n

print(f'min value is {my_min}')

    