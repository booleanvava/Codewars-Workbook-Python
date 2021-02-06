"""
In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and always displays exactly two decimal places.
"""


# Solution: 

small_c = int(input("How many containers of less than 1L do you have? "))
large_c = int(input("How many containers of more than 1L do you have? "))

refund = float((small_c * 0.10) + (large_c * 0.25))

print ("Refund:", round(refund, 2), "$")


