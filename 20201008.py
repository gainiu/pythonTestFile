# with open('pythonTestFile\\txt\\pi_digits.txt') as file_object:
#     content=file_object.read()
#     print(content)

filename = 'pythonTestFile\\txt\\learning_python.txt'

# with open(filename) as file_object:
#     content = file_object.read()
#     print(content+'\n')

# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())
# print('\n')

# with open(filename) as file_object:
#     lines = file_object.readlines()

# for line in lines:
#     print(line.rstrip())

# with open(filename) as file_object:
#     lines = file_object.readlines()
# for line in lines:
#     print(line.replace('Python','C').rstrip())

# filename='pythonTestFile\\txt\\guest.txt'
# username=input('Please enter your name:')
# with open(filename,'w') as file_object:
#     file_object.write(username)

# filename='pythonTestFile\\txt\\guest_book.txt'
# while True:
#     username=input('Please enter your name:')
#     print('Welcome!'+username.title())
#     with open(filename,'a') as file_object:
#         file_object.write(username.title()+'\n')

# print('Give me two number, and I will add them.')
# print('Enter "q" to quit.')

# while True:
#     first_number=input('First number:')
#     if first_number=='q':
#         break
    
#     second_number=input('Second number:')
#     if second_number=='q':
#         break

#     try:
#         answer=int(first_number)+int(second_number)
#     except ValueError:
#         print('you are not enter a number')
#     else:
#         print(answer)

# def read_file(filename):
#     '''读取文件内容并打印出来'''
#     try:
#         with open(filename,'r') as file_object:
#             content=file_object.read()
#     except FileNotFoundError:
#         pass
#         # print('Sorry,the file {} does not exist.'.format(filename))
#     else:
#         print(content.rstrip())

# filenames=['pythonTestFile\\txt\\guest_book.txt','guest.txt']
# for filename in filenames:
#     read_file(filename)

# filename='pythonTestFile\\txt\\learning_python.txt'
# try:
#     with open(filename) as file_object:
#         content=file_object.read()
#         number=content.lower().count('in ')
# except FileNotFoundError:
#     print('Sorry,the file {} does not exist.'.format(filename))
# else:
#     print(number)

# import json

# number=input('Enter your favorite number:')
# filename='pythonTestFile\\txt\\favorite_number.json'
# with open(filename,'w') as file_object:
#     json.dump(number,file_object)

# with open(filename) as file_object:
#     content=json.load(file_object)
#     print('I known your favorite number! It is '+content)

# import json

# filename='pythonTestFile\\txt\\favorite_number.json'
# try:
#     with open(filename) as file_object:
#        content=json.load(file_object)
# except FileNotFoundError:
#     number=input('Enter your favorite number:')
#     with open(filename,'w') as file_object:
#         json.dump(number,file_object)
#         print('We will remember your favorite number!')
# else:
#     print('I known your favorite number! It is '+content)

import json

def show_number(filename):
    try:
        with open(filename) as file_object:
            content=json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return content

def get_new_number(filename):
    number=input('Enter your favorite number:')
    with open(filename,'w') as file_object:
        json.dump(number,file_object)
        print('We will remember your favorite number!')

def ask_user(filename):
    numbers=show_number(filename)
    if numbers:
        print('I known your favorite number! It is '+numbers)
    else:
        numbers=get_new_number(filename)

ask_user('pythonTestFile\\txt\\favorite_number.json')