#create a Python program that will calculate the student's final grade and display the grade points grade is only between 40-100
Name= (input("Please enter your name: "))
Section= (input("Please enter your section: "))
Prelim= float(input("Prelim grade: "))
Midterm = float(input("Midterm grade: "))
Finals = float(input("Finals Grade: "))
Final_grade= (Prelim + Midterm + Finals) // 3 

if Final_grade >= 40 and Final_grade <= 100: 
    
    if Final_grade >= 99:
        print ("1.00 =" , Final_grade , "= Excellent")
    elif Final_grade >= 96 and Final_grade <= 98:  
        print ("1.25 =" , Final_grade , "= Outstanding")
    elif Final_grade >= 93 and Final_grade <= 95: 
        print ("1.50 =" , Final_grade ,  "= Superior")
    elif Final_grade >= 90 and Final_grade <= 92:
        print ("1.75 =" , Final_grade , "= Very Good")
    elif Final_grade >= 87 and Final_grade <= 89:
        print("2.00=" , Final_grade , "= Good")
    elif  Final_grade >= 84 and Final_grade <= 86:
        print ("2.25=" , Final_grade , "= Satisfactory")
    elif  Final_grade >= 81 and Final_grade <= 83:
        print ("2.50=" , Final_grade , "= Fairly Satisfactory")
    elif Final_grade >= 78 and Final_grade <= 80:
        print ("2.75=" , Final_grade , "= Fair")
    elif Final_grade >= 75 and Final_grade <= 77:
        print ("3.00=" , Final_grade , "= Passed")
    elif Final_grade < 75:
        print("5.0=" , Final_grade , "= Failed")
        
else:   
    print("Error")



