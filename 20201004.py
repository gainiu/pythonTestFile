# def city_country(city_name,country):
#     print(city_name.title()+','+country.title())

# city_country('beijing','china')
# city_country('tokyo','japan')
# city_country('newyork','USa')

# def make_album(singer,title,song_numbers=''):
#     if song_numbers:
#         album={'singer':singer,'title':title,'song_numbers':song_numbers}
#     else:
#         album={'singer':singer,'title':title}
#     return album


# alibum=make_album('cxk','one','1')
# # alibum=make_album('hebe','to hebe')
# # alibum=make_album('blackpink','how you like that')
# print(alibum)

# def make_album(singer,title,song_numbers=''):
#     if song_numbers:
#         album={'singer':singer,'title':title,'song_numbers':song_numbers}
#     else:
#         album={'singer':singer,'title':title}
#     return album

# while True:
#     print('Input singer and album title :'+'\n(enter "q" to end the program.)')
#     singer=input('Please enter the singer: ')
#     if singer=='q':
#         break
#     title=input('Please enter the title of the album: ')
#     if title=='q':
#         break

#     album=make_album(singer,title)
#     print(album)
#     print('\n')

# def show_magicians(magicians):
#     for magician in magicians:
#         print(magician)

# def make_great(magicians):
#     for magician in range(len(magicians)):
#         magicians[magician]='the great '+magicians[magician]
#     return magicians

# mag=['one','two','three']
# new=make_great(mag[:])
# show_magicians(new)
# show_magicians(mag)

# def make_sandwich(*toppings):
#     print('\nMaking a sandwich with the following topping: ')
#     for topping in toppings:
#         print('-'+topping)

# make_sandwich('mushrooms')
# make_sandwich('peppers','cheese','fruits')
# make_sandwich('mushrooms','green peppers')

# def build_profile(first, last, **user_info):
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile

# my_profile = build_profile('xiao', 'min', age=18,
#                            location='china', weight='45kg', adult=True)
# print(my_profile)

# class Restaurant():
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name=restaurant_name
#         self.cuisine_type=cuisine_type

#     def describe_restaurant(self):
#         print('Restaurant name: '+self.restaurant_name)
#         print('Cuisine type: '+self.cuisine_type)
    
#     def open_restaurant(self):
#         print('The restaurant is in business.')

# restaurant=Restaurant('Mcdonload','fastfood')
# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# restaurant1=Restaurant('DC','icecream')
# restaurant2=Restaurant('Haidilao','huoguo')
# restaurant1.describe_restaurant()
# restaurant2.describe_restaurant()

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0

    def describe_restaurant(self):
        print('Restaurant name: '+self.restaurant_name)
        print('Cuisine type: '+self.cuisine_type)
    
    def open_restaurant(self):
        print('The restaurant is in business.')

    def set_number_served(self,numbers):
        self.number_served=numbers

    def increment_number_served(self,numbers):
        self.number_served+=numbers


restaurant=Restaurant('Mcd','fastfood')
print(restaurant.number_served)
restaurant.number_served=10
print(restaurant.number_served)
restaurant.set_number_served(100)
print(restaurant.number_served)
restaurant.increment_number_served(150)
print(restaurant.number_served)
restaurant.increment_number_served(150)
print(restaurant.number_served)
restaurant.set_number_served(10)
print(restaurant.number_served)
