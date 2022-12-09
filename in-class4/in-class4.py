# number1 = float(input('Number1 :'))
# number2 = float(input('Number2 :'))
# number3 = float(input('Number3 :'))

# numbers = [number1, number2, number3]
# largest = number1
# for i in numbers:
#     if i > largest:
#         largest = i
# print("The largest number is {}".format(largest))

# age = input('please enter a number ')

# while not age.isdigit():
#     age = input('please enter a valid number')
# else:
#     print(int(age))

# sentence = input("Please enter a sentence : ")

# word_list = sentence.split()
# count1 = len(word_list)
# count2 = 0
# longest = word_list[0]

# while count1 > 0:
#     if len(word_list[count2]) > len(longest[0]):
#         longest = word_list[count2]
#     count1 -= 1
#     count2 += 1

# print('the longest word in "{}" has {} letters.'.format(sentence, len(longest)))
# print(type(len(longest)))

var = 'Clarusway'
edited = ''
for i in var:
    edited += "{}-".format(i)

print(edited.lower().rstrip("-"))

user = {
    'name' : 'daniel',
    'surname' : 'smith',
    'age' : 35
}
for attribute in user.values():
    print(attribute, end=" ")
