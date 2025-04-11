#Recursion is the process of defining something in terms of itself.

# def police(name):
#     print("Hello")
#     police(name)

# police("Saddam")



# def printnum(n):
#     if n>=10:
#         return
#     print(n)
#     printnum(n+1) #Recursive Call

# printnum(100)




# def printnum(n):
#     i=1
#     num=n
#     if i>=n:
#         return
#     print(i)
#     printnum(i+1)

# printnum(100)


# factorial:

# 5! : 5 * 4 * 3 * 2 * 1 = 120


def fact(n):
    if n==1:
        return 1
    else:
        return (n*fact(n-1))
print(fact(5))