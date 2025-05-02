car_model = "BMW '12358KJ'"
print(car_model)

for element in car_model:
  print(element)


# Break lines example
scadual_class = """We have programming class \n from Monday to Friday everyday except \n weekend days"""
print(scadual_class)
print(scadual_class.find("d"))

# Boolean example 
programming_language_classes = "We have C++ and JavaScript class in this semester"

if "Python" in programming_language_classes:
  print("Python")
elif "JavaScript" in programming_language_classes:
 print("I can select JavaScript")

#  Split string
car_information = "Volvo c14564"
splited_information = car_information.split(" ")
print(splited_information)

if 'Benze' in splited_information:
  print("What is the model of Benz")
else: print("this Car is not Benz")
