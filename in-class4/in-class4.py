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

# var = 'Clarusway'
# edited = ''
# for i in var:
#     edited += "{}-".format(i)

# print(edited.lower().rstrip("-"))

# user = {
#     'name' : 'daniel',
#     'surname' : 'smith',
#     'age' : 35
# }
# for attribute in user.values():
#     print(attribute, end=" ")
# print()
# user = {
#     'name' : 'daniel',
#     'surname' : 'smith',
#     'age' : 35
# }
# for attribute in user.items():
#     print(attribute, end=" ")
# print()
# user = {
#     'name' : 'daniel',
#     'surname' : 'smith',
#     'age' : 35
# }
# for attribute in user:
#     print(attribute, end=" ")


# number = input('Enter a number between 1 and 10 :')

# for i in range(0,11):
#     print('{}x{} = {}'.format(number,i,int(number)*i))

# text = ['one', 'two', 'three', 'four', 'five']
# numbers = [1,2,3,4,5]

# for x, y in zip(text,numbers):
#     print(x, ':', y)

numbers = range(1,11)
evens = []
odds = []
for i in numbers:
    if i%2 == 0:
        evens.append(i)
    else:
        odds.append(i)
print(evens)
print(odds)


arr = ['Sunday', 'Monday', 'Tuesday', 'Wednesday']

for index, i in enumerate(arr):
    print(index, i)

arr = [55, 22, 33, 11, 66, 5, 99, 48]

# for i, ii in enumerate(arr):
#     for j, jj in enumerate(arr[i+1:]):
#         if ii > jj:
#             temp = arr[i]
#             arr[i] = arr[j+i+1]
#             arr[j+i+1] = temp
# print(arr)

# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i] > arr[j]:
#             arr[i], arr[j] = arr[j], arr[i]
#             # temp = arr[i]
#             # arr[i] = arr[j]
#             # arr[j] = temp
# print(arr)

# #long
# squares = []
# for i in range(10):
#     squares.append(i * i)
# print(squares)

# squares2 = [i * i for i in range(10)]
# print(squares2)

# evens = []
# for n in range(12):
#     if n%2 == 0:
#         evens.append(n)
# print(evens)

# evens2 = [n for n in range(12) if n%2 == 0]
# print(evens2)

# names = ['Python', 'Aisha', 'Bulend', 'Ala', 'Ahmed']

# product = 1
# arr = [1,2,3,4,5]
# for i in arr:
#     product *= i

# result = []
# for i in arr:
#     result.append(product//i)

# print(result)

arr = [1,2,3,4,5]
result = []
for i in range(len(arr)):
    product = 1
    for j in range(len(arr)):
        if i != j:
            product *= arr[j]
    result.append(product)

print(result)


lst = [1,2,3,4,5]
print([[lst[j] for j in range(len(lst)) if i !=j] for i in range(len(lst))])
