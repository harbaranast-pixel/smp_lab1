#1
var_start = 1
var_end = 10
total_sum = 0

for i in range(var_start, var_end + 1):
    if i % 2 == 0:
        total_sum += i

print(total_sum)            

#2
var_start = 1
var_end = 10
var_step = 3
total_mult = 1

for i in range(var_start, var_end + 1, var_step):
    if i % 2 != 0:
        total_mult *= i

print(total_mult)  

#3 
product_name = "Laptop"
price = 750
is_sale = False
is_available = True
category = "Standard"

if not is_available:
    print(f"Товар {product_name} тимчасово відсутній на складі.")

if price <=500 or is_sale:
    category = "Budget / Promotional"
elif price>=501 and price<=1000:
    category = "Standard"
else:
    category = "Premium"         

print(f"{product_name}: price - {price}, category- {category}")

#4
gpa = 3.5
is_active_in_student_council = False
has_volunteer_experience = True
scholarship_type = {'full', 'partial', 'no'}

if gpa >=4.5 and is_active_in_student_council:
    scholarship_type = 'full'
elif gpa>=4.0:
    scholarship_type = 'partial'
elif not((gpa>=4.5 and is_active_in_student_council) or (gpa>=4.0 and has_volunteer_experience)):
    scholarship_type = 'no'
    
print(f"Scholarship type: {scholarship_type}")

#5 
var_start = 1
var_end = 10
total_result=0 

for i in range(var_start, var_end+1):
    if i % 2 == 0:
        total_result += i**2
    else:
        total_result -= i

print(total_result)

#6
var_start = 1
var_end = 10

for i in range(var_start, var_end + 1):
    if i % 7 == 0:
        print(i)
        break
      
else:
     print("There is no number divisible by 7 in the range.")

#7
start_number = 1
end_number = 1000
status = "Lucky"

while start_number <= end_number:
    if start_number % 2 !=0:
        start_number += 1
        continue

    if start_number %7 == 0 and start_number % 3 !=0 and start_number % 2 == 0:
        status= "Lucky"
        print(f"Number {start_number} is lucky.")
        break

    start_number += 1
else: 
    status = "Unlucky"
    print( 'No "lucky" number was found in the range.')

#8
raw_cars = "aUdi; bmW; pOrScHe ; toYoTa;  MeRcEdEs "
car_list = raw_cars.split(";")

for i in range(len(car_list)):
    car_list[i] = car_list[i].strip().capitalize()

car_list[1] = car_list[1].upper()

print(car_list)

print(car_list[1::2]) 

separator = " // "
car_string = separator.join(car_list)
print(car_string)