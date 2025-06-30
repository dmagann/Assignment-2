# The assignment prompt calls for five inputs. That means 5 variables requiring an input. #
number1 = float(input("Please enter five numbers"))
number2 = float(input())
number3 = float(input())
number4 = float(input())
number5 = float(input())

# There is an average function, but we have not been taught it yet. I stuck with basic operations for full credit. #
numtotal = number1 + number2 + number3 +number4 + number5
numavg = numtotal / 5

#This portion is determined by the assignment prompt. #
print("The average of those numbers is:")
print(numavg)