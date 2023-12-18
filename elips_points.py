def get_points(x, a, b):
    result = (x**3+a*x+b)%7
    result = 'y^2 = {}'.format(result)
    return result

for i in range(-3, 4):
    print('x= {}; '.format(i), get_points(x=i, a=2, b=-1))