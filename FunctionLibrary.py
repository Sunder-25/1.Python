class multipleFunctions():

    def OddEven():
        num=int(input("Enter the number:"))
        if((num%2)==1):
            print("Odd Number")
            message="Odd Number"
        else:
            print("Even Number")
            message="Even Number"
        return message

    def BMI():
        BMI=int(input("Enter the BMI Index:"))
        if(BMI <18.5):
            print("Underweight")
            message="Underweight"
        elif(BMI<=24.9):
            print("Normal range")
            message="Normal range"
        elif(BMI <=29.9):
            print("Overweight")
            message="Overweight"
        else:
            print("Very Overweight")
            message="Very Overweight"
        return message    

    def subfields():
        #lists=["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        print("Sub-fields in AI are:")
        for subfield in lists:
            print(subfield)

    def Eligible():
        #request user input
        gender =input("Your gender (Male/Female): ")
        age=int(input("Your age: "))
        
        #print user details
        print("Your Gender: ", gender)
        print("Your Age: ", age)
    
        #check eligibility
        if (gender == "Male" and age>=21):
            print("ELIGIBLE")
        elif (gender == "Female" and age>=18):
            print("ELIGIBLE")
        else :
            print("NOT ELIGIBLE")

    def percentage ():
        #percentage of each subject
        subject1 = 98
        subject2 = 87
        subject3 = 95
        subject4 = 95
        subject5 = 93

        #calculate total
        total = subject1 + subject2 + subject3 + subject4 + subject5

        #calculate percentage
        percentage = (total/500) * 100 #since max marks = 500

        #print results
        print("Subject1=", subject1)
        print("Subject2=", subject2)
        print("Subject3=", subject3)
        print("Subject4=", subject4)
        print("Subject5=", subject5)
        print("Total :", total)
        print("Percentage :", percentage)

    def triangle():
    #triangle details
        Height = 32
        Breadth = 34
        AreaFormula = "(Height*Breadth)/2"
        AreaOfTriangle = 544.0
        Height1 = 2
        Height2 = 4
        Breadth = 4
        PerimeterFormula = "Height1+Height2+Breadth"
        PerimeterOfTriangle = 10

        #print output
        print("Height:", Height)
        print("Breadth:", Breadth)
        print("Area formula:", AreaFormula)
        print("Area of triangle:", AreaOfTriangle)
        print("Height1:", Height1)
        print("Height2:", Height2)
        print("Breadth:", Breadth)
        print("Perimeter formula:", PerimeterFormula)
        print("Perimeter of Triangle:", PerimeterOfTriangle)