from collections import OrderedDict
# 
# # inheritance 
# class Flower_information:
#   def __init__(self, name, color, country):
#     self.name = name
#     self.color= color
#     self.country = country

#   def flower_name (self):
#     return f"this {self.name} is one of the nice flower you can find here"


# class Flower_color():
#   def flowe_color(self):
#     return f"The {self.name} has {self.color} and in this season it is really nice."


# class Flower_location(Flower_information, Flower_color):
#   def flower_location(self):
#     flower_details = f"The {self.name} has {self.color} color and you can find it in {self.country}."
#     return flower_details

# rose_flower = Flower_location("Rose", "Red", "Iran")
# print(rose_flower.flower_name())
# print(rose_flower.flowe_color())
# print(rose_flower.flower_location())


# inverted_tulip = Flower_location(" inverted tulip", "Red", "Iran")
# print( inverted_tulip.flower_name())
# print( inverted_tulip.flowe_color())
# print( inverted_tulip.flower_location())

##  dictionaries
# count_fruit_number = {
#   "Banana" : 2,
#   "cherry" : 2,
#   "peach" : 4,
#   "Appricot" : 6,
#   "grap" : 2,
#   "mixed_fruits" : ["Pineapple", "peach", "nectarin"]
# }

# print(count_fruit_number["Banana"])
# print(count_fruit_number)
# print(len(count_fruit_number))
# print(type(count_fruit_number))

# for element in count_fruit_number:
#   print(type(element))


# house_information = dict(location = "Zaeferaniye", Number = 16, area = 100)
# print(house_information["location"])
# print(house_information.get("location"))

# key_information = house_information.keys()
# print(type(key_information))
# print(key_information)

# house_information["location"] = "Darabad"
# print(house_information["location"])

# values_information = house_information.values()
# print(type(values_information))
# print(values_information)

# items_information = house_information.items()
# print(type(items_information))
# print(items_information)

# if "location" in house_information:
#   print(house_information["location"])

# house_information.update({"floor": "3rd floor"})
# print(house_information)

## OOP principles / polymorphism 

class Cat_sound:
  def sound(self):
    meow_sound = f"Cats make sound like Meaw"
    return meow_sound

class Dog_sound(Cat_sound):
  def sound(self):
    bark_sound = f"Dogs are barking"
    return bark_sound
  
class Rosster_sound(Cat_sound):
  def sound(self):
    ghooghooli_sound = f"Rossters are making sound like ghooghooli ghooghoo"
    return ghooghooli_sound

animal_sound = [Cat_sound(), Dog_sound(), Rosster_sound()]

for sound in animal_sound:
  print(sound.sound())