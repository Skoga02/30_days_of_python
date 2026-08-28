age = 24
print(type(age))

height = 185.0
print(type(height))

complex = 1 + 1j
print(type(complex))

base = int(input("Enter base of triangle: "))
height = int(input("Enter the height of the triangle: "))

area_of_triangle = 0.5 * base * height
print(area_of_triangle)

side_a = int(input("Enter length of side a: "))
side_b = int(input("Enter length of side b: "))
side_c = int(input("Enter length of side c: "))

perimeter = side_a + side_b + side_c
print(perimeter)

radius = 4
area_of_circle = 2 * 3.14 ** radius
circumference_circle = 2 * 3.14 * radius

# Claculate the slope, x-intercept and y-intercept of y = 2x - 2
slope = 2
y_intercept = -2

# Find x-intercept 
# 0 = 2x - 2
x_intecept = 1 

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1 = 2 
y1 = 2 

x2 = 6 
y2 = 10

slope = (y2 - y1) / (x2 - x1)

distance = ((x2 - x1) ** 2 + (y2 - y1)) ** 0.5

print("Slope:", slope)
print("Distance:", distance)

# compare slope 1 and slope 2
slope_1 = 2
slope_2 = 2

print(slope_1 == slope_2)

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# y = (x + 3)**2

x = -3
y = x ** 2 + 6 * x + 9
print(y)

python_length = len("python")
dragon_length = len("dragon")

print(python_length)
print(dragon_length)

# This statement is False sins the are the same len
print(python_length != dragon_length)

# the letters on in that order can be found in both words, True
print("on" in "python" and "on" in "dragon")


sentence = "I hope this course is not full of jargon."

print("jargon" in sentence)

print("on" not in "python" and "on" not in "dragon")

python_length = len("python")

print(type(python_length))

python_length_float = float(python_length)
python_length_string = str(python_length)

print(python_length)
print(python_length_float)
print(python_length_string)


number = int(input("Enter a number: "))
print(number % 2 == 0)

print(7 // 3 == int(2.7))

print(type("10") == type(10))

# Gives error sins python can´t directly convert "9.8" to int
print(int("9.8") == (10))

# Correct way to do it
print(int(float("9.8")) == 10)

hours = int(input("Enter hours: "))
hourly_rate = int(input("Enter rate per hour: "))

weekly_earnings = hours * hourly_rate
print("Your weekly earning is", weekly_earnings)

years_lived = (int(input("Enter number of years you have lived: ")))
seconds = years_lived * 365 * 24 * 60 * 60

print("You have lived for", seconds, "seconds.")

print("1", "1", "1", "1", "1")
print("2", "1", "2", "4", "8")
print("3", "1", "3", "9", "27")
print("4", "1", "4", "16", "64")
print("5", "1", "5", "25", "125")