#(Circle Area, Diameter and Circumference) For a circle of radius 2, display the diameter,
#circumference and area. Use the value 3.14159 for π. Use the following formulas
#(r is the radius): diameter = 2r, circumference = 2πr and area = πr2. [In a later chapter, we’ll
#introduce Python’s math module which contains a higher-precision representation of π.]


pie = 3.14159
radius = 2

diameter =  2 * radius 
print ("Diameter =", diameter)
circumference = 2 * pie * radius
print('Circumference =', circumference)
area = pie * (radius ** radius)
print('Area =', area)