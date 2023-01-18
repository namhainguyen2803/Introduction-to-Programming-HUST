def check_triangle(a,b,c):
    if a==b==c:
        return 'Equilateral'
    elif a**2+b**2==c**2 or a**2+c**2==b**2 or c**2+b**2==a**2:
        return "Scalene"
    else:
        return 'Isosceles'
print(check_triangle(int(input()),int(input()),int(input())))