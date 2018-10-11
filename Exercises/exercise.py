def product(num1, num2):
  return num1 * num2
print('product: ', product(2,2))

##################

def return_day(num):
  days = ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
  if num > 0 and num <= len(days):
    return days[num-1]
  return None
print('return_day: ', return_day(3))


##############################

def last_element(list):
  if list[0] != True:
    return None
  else:
    return list[-1]
print('last_element: ', last_element([1,2,3,4]))

############################

def number_compare(num1, num2):
  if num1 == num2:
    return 'Numbers are equal'
  elif num1 > num2:
    return 'First is greater'
  return 'Second is greater'
print('number_compare: ', number_compare(3,5))

#########################

def single_letter_count(str1, letter):
  return str1.lower().count(letter.lower())
print('single_letter_count: ', single_letter_count('Hellohh', 'h'))

###########################

def multiple_letter_count(str1):
  return {char: str1.count(char) for char in str1 }
print("multiple_letter_count: ", multiple_letter_count('awesomeeee'))

##########################

def list_manipulation(list, command, location, value=None):
  if command == 'remove' and location == 'end':
    return list.pop()
  elif command == 'remove' and location =='beginning':
    return list.pop(0)
  elif command == 'add' and location == 'beginning':
    list.insert(0, value)
    return  list
  elif command == 'add' and location == 'end':
    list.append(value)
    return list
print('list_manipulation: ', list_manipulation([1,2,3,4], 'add', 'end', 20))

############################

def is_palindrome(str1):
  stripped = str1.replace(" ", "")
  return stripped == stripped[::-1]
print("is_palindrome: ", is_palindrome('amanaplanacan alpanama'))

##########################

def frequency(list, search_term):
  count = [times for times in list if times == search_term]
  return len(count)
print("frequency: ", frequency([1,2,3,3,3,3], 3))

##########################

def multiply_even_number(list):
  num = 1
  for i in list:
    if i % 2 == 0:
      num *= i
  return num
print('multiply_even_number: ', multiply_even_number([1,2,3,4,5,6]))

############################

def capitalize(word):
  word2 = [ char for char in word]
  word2[0] = word2[0].upper()
  word3 = ''.join(word2)
  return word3
print('capitalize: ', capitalize('lukas'))

# OR

def capitalize2(word):
  return word[:1].upper() + word[1:]
print('capitalize2: ', capitalize2('jamaica'))

##################

def compact(list):
  list2 = []
  for i in list:
    if i:
      list2.append(i)
  return list2
print('compact: ', compact([0,1,2,"",[], False, {}, None, "All done"]))

#####################

def intersection(list1, list2):
  answer = []
  for i in list1:
    for l in list2:
      if i == l:
        answer.append(l)
  return answer
print('intersection: ', intersection([1,2,3,4,5], [4,5,6,7,8]))

# OR

def intersection2(list1,list2):
  answer = [ l for l in list1 if l in list2]
  return answer
print('intersection2: ', intersection2([1,2,3,4,5], [4,5,6,7,8]))

##########################

def isEven(num):
  return num % 2 == 0

def partition(list, fn=isEven):
  answer = [[],[]]
  for i in list:
    if isEven(i) == True:
      answer[0].append(i)
    else:
      answer[1].append(i)
  return answer
print('partition: ', partition([1,2,3,4,5,6]))
