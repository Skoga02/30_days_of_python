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

