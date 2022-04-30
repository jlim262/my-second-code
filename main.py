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


my_max = -987654321

for n in my_list:
  if n > my_max:
    my_max = n

print(f'max value is {my_max}')

# 2. sort a list 
# input: [74, 50, 30, 10, 23, 112, 39, 20, 23, 42, 3]
# output: 3, x, x, x, x, x, ,x x,x, 112

# input = [74, 50, 30, 10, 23, 112, 39, 20, 23, 42, 3]
input = [74, 50, 30, 10, 23, 112, 39, 20, 42, 3]
result = []
print(len(input))
for i in input:
  my_min = 987654321
  
  for n in input:
    if n not in result:
      if n < my_min:
        my_min = n
  
  # print(f'min value is {my_min}')
  result.append(my_min)
print(result)

# -----------------------------------------------------

# input = [74, 50, 30, 112, 39, 42]
input = [74, 50, 30, 10, 23, 112, 39, 20, 23, 42, 3]

result = []
print(len(input))
# for i, v in enumerate(input):
for i in range(len(input)):
  my_min = 987654321
  
  for n in input:
    if n < my_min:
      my_min = n
  
  result.append(my_min)
  print(my_min)
  input.remove(my_min)
  print(input)
  
print(result)


# extract file name from file path
# input: 'main.py'
# output: main
# input: 'my_text.txt'
# output: my_text

def extract_filename(full_path):
  filename = ''
  for c in full_path:
    if c == '.':
      return filename
    else:
      filename = filename + c

    print(filename)

name = extract_filename('asdfasdfasdfmain.py')
print(name) # main

