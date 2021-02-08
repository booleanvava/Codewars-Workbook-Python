"""
There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!

input
customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
n: a positive integer, the number of checkout tills.
output
The function should return an integer, the total time required.

"""

# Solution: 

def queue_time(customers, n): # We solve the easiest case: when the number of tills is 1. In this case, the desired output is simply the sum of the time spent per client 
    if n == 1:
        return sum(customers)
    elif n > len(customers): # In this case, the total time spent by all customers is simply the time spent by the busiest customer. 
        return max(customers)
    elif n < len(customers): # When the tills are less than the amount of customers, the desired output will be equal to the sum of the unique customer times. For this reason, we turned the list into a set (eliminating the duplicates). 
        return sum(set(customers)) 
             
