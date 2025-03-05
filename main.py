from random import randint as rand

nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
special = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', ';', ':', '[', '{', '}', ']', '\'', '\"', '|', '.', ',', '<', '>', '?']

# by_user example: ['a-b', '0-4', '9']
def gen_password(numbers = True,
                 lowercase_letters = True,
                 uppercase_letters = True,
                 special_symbols = True,
                 by_user = '',
                 min_len = 12,
                 max_len = 15):
  all = set()
  if numbers:
    for num in nums:
      all.add(num)
  if lowercase_letters:
    for letter in lowercase:
      all.add(letter)
  if uppercase_letters:
    for letter in uppercase:
      all.add(letter)
  if special_symbols:
    for symbol in special:
      all.add(symbol)
  for cur in by_user:
    if len(cur) == 1:
      all.add(cur)
    elif len(cur) == 3:
      for sym in range (ord(cur[0]), ord(cur[2]) + 1):
        all.add(chr(sym))
  all_in_list = list(all)
  password_len = rand(min_len, max_len)
  password = ''
  for i in range(password_len):
    password += all_in_list[rand(0, len(all_in_list) - 1)]
  return password

print(gen_password(True, True, False, False, [], 8, 9))