#     *args
#     **kwargs

# print("Hello","Saddam","Ansari")

# def addition(a,b,c,d):
#     print(a+b+c+d)

# addition(50,56,95,36,57)


# def addition(*num):
#     sum=0
#     for i in num:
#         sum=i+sum
#         # print(i)
#     print(sum)

# addition(5,6,9,3,7)
# addition(9,3,7)
# addition(1,2,3,7)
# addition(5,6,9,3,8,7,1,3)


#    **KWARGS

def Student_Details(**data):
    for key,value in data.items():
        print(key , " - " ,value)

Student_Details(Name="Saddam",Address="Kolkata")
Student_Details(Name="Shahbaaz",Address="Delhi", Country="India")