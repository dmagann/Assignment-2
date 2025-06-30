change = int(input("Please enter an amount in cents less than a dollar."))
# This value needs to be an integer to perform mathematical operations #

# The algorithm breaks down an amount of change sequentially by using remainders and started with the largest value #
Quarters = change // 25
Quarterremainder = change % 25

Dimes = Quarterremainder // 10
Dimeremainder = Quarterremainder % 10

Nickels = Dimeremainder // 5
Nickelremainder = Dimeremainder % 5
# I could have substituted Pennies for Nickelremainder, but this way aids in readability #
Pennies = Nickelremainder

# This is the format taken directly from the assignment #
print("Your change will be:")
print("Q:", Quarters)
print("D:", Dimes)
print("N:", Nickels)
print("P:", Pennies)
