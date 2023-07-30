import math
print("""SIMPLE CALCULATOR
SELECT ANY OPERATORS FROM THE LIST GIVEN BELOW:
1. ADDITION
2. SUBTRACTION
3. MULTIPLICATION
4. DIVISION
5. TO FIND SQUARE ROOT OF THE NUMBER
6. TO FIND CUBE ROOT OF THE NUMBER
7. TO FIND SQUARE OF THE NUMBER
8. TO FIND CUBE OF THE NUMBER
9. TO FIND RAISED TO THE POWER OF
10.TO FIND THE TABLES
11.TRIGONOMETRY
12.SOLVING PROBLEM USING BODMAS

JUST FOR FUN
13.TO FIND HOW MANY MINUTES FROM BIRTH?
14.TO FIND THE VALUE OF PI(round of)
15.TO FIND ONLY QUOTIENT AFTER DIVIDING TWO NUMBERS
16.TO FIND ONLY REMAINDER OF TWO NUMBERS


CALCULATION OF THE SHAPES
17.SQUARE   18.RECTANGLE 19.CIRCLE
20.CUBE     21.CUBOID    22.CONE
23.CYLINDER 24.SPHERE    25.RIGHT TRIANGLE
                                          """)
i=1
while i==1:
    a=int(input("ENTER THE INDEX OF THE OPERATOR YOU WANT TO PERFORM:  "))
    if a==1:
        b=int(input("How many numbers do you want to add up?  "))
        c=float(input("Enter a number:"))
        for i in range(1,b):
            d=float(input("Plus:"))
            c+=d
        print("THE SUM IS",c)
    elif a==2:
        b=int(input("How many numbers do you want to use in subtraction?  "))
        c=float(input("Enter a number:"))
        for i in range(1,b):
            d=float(input("minus:"))
            c-=d
        print("THE DIFFERENCE IS",c)
    elif a==3:
        b=int(input("How many numbers do you want to use in multiplication? "))
        c=float(input("Enter a number:"))
        for i in range(1,b):
            d=float(input("multiply by:"))
            c*=d
        print("THE PRODUCT IS",c)
    elif a==4:
        b=float(input("Enter a number:  "))
        c=float(input("divided by:  "))
        print("THE ANSWER IS",b/c)
    elif a==5:
        c=int(input("How many times do you want to find the square root of individual numbers?"))
        for i in range(1,c+1):
            b=int(input("Enter a number:  "))
            print("THE SQUARE ROOT OF THE NUMBER IS",math.sqrt(b))
    elif a==6:
        c=int(input("How many times do you want to find the cube root of individual numbers?"))
        for i in range(1,c+1):
            b=int(input("Enter a number:  "))
            print("THE CUBE ROOT OF THE NUMBER IS",math.cbrt(b))
    elif a==7:
        c=int(input("How many times do you want to find the square of individual numbers?"))
        for i in range(1,c+1):
            b=int(input("Enter a number:  "))
            print("THE SQUARE OF THE NUMBER IS",pow(b,2))
    elif a==8:
        c=int(input("How many times do you want to find the cube of individual numbers?"))
        for i in range(1,c+1):
            b=int(input("Enter a number:  "))
            print("THE CUBE OF THE NUMBER IS",pow(b,3))
    elif a==9:
        c=int(input("How many times do you to repeat this process?"))
        for i in range(1,c+1):
            b=int(input("Enter a number:  "))
            c=int(input("raised to the power of   "))
            print(b,"RAISED TO THE POWER OF",c,"IS",pow(b,c))
    elif a==10:
        e=int(input("How many times do you want to repeat this process?"))
        for i in range(1,e+1):
            b=float(input("Table of the number:  "))
            c=int(input("With bottom: "))
            for i in range(1,c+1):
                d=b*i
                print(b,"x",i,"=",round(d,2))
    elif a==11:
        print("1.sin  2.cos  3.tan")
        b=int(input("INDEX OF WHICH YOU WANT TO FIND(1/2/3):"))
        if b==1:
            print("1.sine inverse  2.sine")
            c=int(input("Index of which you want to find(1/2):"))
            if c==1:
                d=float(input("Enter the number in decimal for which you want to find the sin inverse:"))
                e=math.asin(d)
                print("THE SINE INVERSE OF",d,"IS",e)
            elif c==2:
                d=int(input("Enter the number in decimal which divides pi to find sine:"))
                e=math.pi*d
                print(e,"after multiplying with pi")
                f=math.sin(e)
                print("THE SINE OF",e,"IS",f)
        elif b==2:
            print("1.cosine inverse  2.cosine")
            c=int(input("Index of which you want to find(1/2):"))
            if c==1:
                d=float(input("Enter the number in decimal for which you want to find the cosine inverse:"))
                e=math.acos(d)
                print("THE COSINE INVERSE OF",d,"IS",e)
            elif c==2:
                d=int(input("Enter the number in decimal which divides pi to find cosine:"))
                e=math.pi/d
                print(e,"after pi divided by",d)
                f=math.cos(e)
                print("THE COSINE OF",e,"IS",f)
        elif b==3:
            print("1.tan inverse  2.tan")
            c=int(input("Index of which you want to find(1/2):"))
            if c==1:
                d=float(input("Enter the number in decimal for which you want to find the tan inverse:"))
                e=math.atan(d)
                print("THE TAN INVERSE OF",d,"IS",e)
            elif c==2:
                d=int(input("Enter the number in decimal which divides pi to find tan:"))
                e=math.pi/d
                print(e,"after multiplying with pi")
                f=math.tan(e)
                print("THE TAN OF",e,"IS",f)
    elif a==12:
        b=eval(input("Enter a problem using(+,-,*,/):"))
        print("THE ANSWER IS",b)
    elif a==13:
        b=int(input("How many times do you want to repeat this process?"))
        for i in range(1,b+1):
            print("SINCE BIRTH")
            a=float(input("Enter the age:"))
            b=a*365
            c=b*24
            d=c*60
            print("YOU CAME TO THE WORLD BEFORE",d,"MINUTES(approx)")
    elif a==14:
        c=int(input("How many times do you want to repeat this process?"))
        for i in range(1,c+1):
            b=math.pi
            c=int(input("How many numbers wants to be displayed after decimal point?"))
            print(round(b,c))
    elif a==15:
        e=int(input("How many times do you want to repeat this process?"))
        for i in range(1,e+1):
            b=int(input("Enter a number:"))
            c=int(input("divided by:"))
            d=b//c
            print("THE QUOTIENT OF THE DIVISION IS",d)
    elif a==16:
        e=int(input("How many times do you want to repeat this process?"))
        for i in range(1,e+1):
            b=int(input("Enter a number:"))
            c=int(input("divided by:"))
            d=b%c
            print("THE REMAINDER IS:",d)
    elif a==17:
        print("1.Diagonal  2.Area")
        b=int(input("INDEX OF WHICH YOU WANT TO FIND:"))
        if b==1:
            c=float(input("Enter the length of one of its side:"))
            d=math.sqrt(2)
            print("THE DIAGONAL OF THE SQUARE IS",c*d)
        elif b==2:
            c=float(input("Enter length of the any one of the side:"))
            d=c**2
            print("THE AREA OF THE SQUARE IS",d)
    elif a==18:
        print("1.Diagonal  2.Area")
        b=int(input("Index of which you want to find:"))
        if b==1:
            c=float(input("Enter the length:"))
            d=float(input("Enter the width:"))
            e=c**2
            f=d**2
            g=math.sqrt(e+f)
            print("THE DIAGONAL OF THE RECTANGLE IS",g)
        elif b==2:
            c=float(input("Enter the length:"))
            d=float(input("Enter the width :"))
            print("THE AREA OF THE RECTANGLE IS",c*d)
    elif a==19:
        print("1.Perimeter  2.Area")
        b=int(input("INDEX OF WHICH YOU WANT TO FIND(1/2):"))
        if b==1:
            c=float(input("Enter the radius of the circle:"))
            d=math.pi
            print("THE PERIMETER OF CIRCLE IS",2*d*c)
        elif b==2:
            c=float(input("Enter the radius of the circle:"))
            d=math.pi
            print("THE AREA OF THE CIRCLE IS",d*c**2)
    elif a==20:
        print("1.CURVED SURFACE AREA  2.TOTAL SURFACE AREA  3.VOLUME")
        b=int(input("INDEX OF WHICH YOU WANT TO FIND(1/2/3):"))
        if b==1:
            c=float(input("Enter the length of one of its side:"))
            d=4*c**2
            print("THE CURVED SURFACE AREA OF THE CUBE IS",d)
        elif b==2:
            c=float(input("Enter the length of one of its side:"))
            d=6*c**2
            print("THE TOTAL SURFACE AREA OF THE CUBE IS",d)
        elif b==3:
            c=float(input("Enter the length of one of its side:"))
            d=c**3
            print("THE VOLUME OF THE CUBE IS",d)
    elif a==21:
        print("1.CURVED SURFACE AREA  2.TOTAL SURFACE AREA  3.VOLUME")
        b=int(input("INDEX OF WHICH YOU WANT TO FIND(1/2/3):"))
        if b==1:
            c=float(input("Enter the length of the cuboid:"))
            d=float(input("Enter the width of the cuboid :"))
            e=float(input("Enter the height of the cuboid:"))
            f=2*e*(c+d)
            print("THE CURVED SURFACE AREA OF THE CUBOID IS",f)
        elif b==2:
            c=float(input("Enter the length of the cuboid:"))
            d=float(input("Enter the width of the cuboid:"))
            e=float(input("Enter the height of the cuboid:"))
            f=2*((c*d)+(c*e)+(d*e))
            print("THE TOTAL SURFACE AREA OF THE CUBOID IS",f)
        elif b==3:
            c=float(input("Enter the length of the cuboid:"))
            d=float(input("Enter the width of the cuboid:"))
            e=float(input("Enter the height of the cuboid:"))
            f=c*d*e
            print("THE VOLUME OF THE CUBOID IS",f)
    elif a==22:
         print("1.CURVED SURFACE AREA  2.TOTAL SURFACE AREA  3.VOLUME")
         b=int(input("INDEX OF WHICH YOU WANT TO FIND(1/2/3):"))
         if b==1:
             c=float(input("Enter the radius of the cone:"))
             d=float(input("Enter the slant height(L) of the cone:"))
             e=math.pi
             f=e*c*d
             print("THE CURVED SURFACE AREA OF THE CONE IS",f)
         elif b==2:
             c=float(input("Enter the radius of the cone:"))
             d=float(input("Enter the slant height(L) of the cone:"))
             e=math.pi
             f=e*c*(d+c)
             print("THE TOTAL SURFACE AREA OF THE CONE IS",f)
         elif b==3:
            c=float(input("Enter the radius of the cone:"))
            d=float(input("Enter the height(H) of the cone:"))
            e=math.pi/3
            f=e*c**2*d
            print("THE VOLUME OF THE CONE IS",f)
    elif a==23:
        print("1.CURVED SURFACE AREA  2.TOTAL SURFACE AREA  3.VOLUME")
        b=int(input("INDEX OF WHICH YOU WANT TO FIND(1/2/3):"))
        if b==1:
            c=float(input("Enter the radius of the cylinder:"))
            d=float(input("Enter the height of the cylinder:"))
            e=math.pi
            f=2*e*c*d
            print("THE CURVED SURFACE AREA OF THE CYLINDER IS",f)
        elif b==2:
            c=float(input("Enter the radius of the cylinder:"))
            d=float(input("Enter the height of the cylinder:"))
            e=math.pi
            f=2*e*c*(d+c)
            print("THE TOTAL SURFACE AREA OF THE CYLINDER IS",f)
        elif b==3:
            c=float(input("Enter the radius of the cylinder:"))
            d=float(input("Enter the height of the cylinder:"))
            e=math.pi
            f=e*c**2*d
            print("THE VOLUME OF THE CYLINDER IS",f)
    elif a==24:
         print("1.SURFACE AREA  2.VOLUME")
         b=int(input("THE INDEX OF WHICH YOU WANT TO FIND(1/2):"))
         if b==1:
             c=float(input("Enter the radius of the sphere:"))
             d=math.pi
             e=4*d*c**2
             print("THE SURFACE AREA OF THE SPHERE IS:",e)
         elif b==2:
             c=float(input("Enter the radius of the sphere:"))
             d=math.pi
             e=(4/3)*d*c**3
             print("THE VOLUME OF THE CONE IS",e)
    elif a==25:
        print("1.HYPOTENUSE  2.AREA ")
        b=int(input("INDEX OF WHICH YOU WANT TO FIND(1/2):"))
        if b==1:
            c=float(input("Enter the height of triangle:"))
            d=float(input("Enter the base of triangle:"))
            e=c**2
            f=d**2
            g=math.sqrt(e+f)
            print("THE HYPOTENUSE OF THE RIGHT TRIANGLE IS",g)
        elif b==2:
            c=float(input("Enter the height of triangle:"))
            d=float(input("Enter the base of triangle:"))
            e=0.5*c*d
            print("THE AREA OF THE RIGHT TRIANGLE IS",e)
    d=input("Do you want to continue(c/q)?")
    if d=="q":
        i=0
    else:
        i=1
        
 
            


    



