print('number',"\t",'square',"\t",'cube')
number = 0
square = 0
cube = 0
for row in range(6):
    for column in range(1):
        number += 1
        square = number * number
        cube = number * square
        print(number,'\t',square,'\t',cube)
    print()