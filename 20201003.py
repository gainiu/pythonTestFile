# pizza_add='Please enter the tooping of the pizza: '
# pizza_add+='\n(Enter "quit" to end the program.)'

# message=''
# while message!='quit':
#     message=input(pizza_add)

#     if message!='quit':
#         print(message)

# age_tip='Please enter the age and we will return the price:'
# age_tip+='\n(Enter "quit" to end the program.)'

# active=True
# while active==True:
#     age=input(age_tip)

#     if age=='quit':
#         break
#     elif int(age) < 3:
#         print("It's free!")
#     elif int(age)>=3 and int(age)<=12:
#         print("It needs 10$.")
#     elif int(age) > 12:
#         print("It needs 15$.")

# sandwich_orders=['tomato','mushroom','bbq']
# finished_sandwiches=[]

# while sandwich_orders:
#     making_sandwich=sandwich_orders.pop()
#     print('I made your {} sandwich.'.format(making_sandwich))
#     finished_sandwiches.append(making_sandwich)

# print('------finished------')
# for finished_sandwich in finished_sandwiches:
#     print(finished_sandwich)

# sandwich_orders=['tomato','pastrami','mushroom','pastrami','bbq','pastrami']
# print(sandwich_orders)
# print('pastrami sold out!')

# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')

# print(sandwich_orders)

# places={}

# active=True
# while active:
#     username=input('Please input your name: ')
#     place=input('if you could visit one place in the world,where would you go?')
#     places[username]=place
#     repeat=input('Would you like to let another person respond?(yes/no)')
#     if repeat=='no':
#         active=False

# for username,place in places.items():
#     print('{} would like to go {}.'.format(username,place))
    