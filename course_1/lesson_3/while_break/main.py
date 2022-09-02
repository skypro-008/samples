
number_of_elements = 0

while True:
  user_input = input()

  if user_input != 'stop':
    number_of_elements += 1
  else:
    break

print(number_of_elements)
