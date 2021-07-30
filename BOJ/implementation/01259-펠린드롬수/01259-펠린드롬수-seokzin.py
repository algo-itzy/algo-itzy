while True:
  num = input()

  if num == '0':
    break

  print('yes' if num == num[::-1] else 'no')