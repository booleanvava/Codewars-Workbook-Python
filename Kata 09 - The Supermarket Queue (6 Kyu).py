"""
There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!

input
customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
n: a positive integer, the number of checkout tills.
output
The function should return an integer, the total time required.

"""

# Solution: 

def queue_time(customers, n): # We solve for the easiest case where there is only one till. Naturally, this means that each customer's time will be added to output the total time.
    if n == 1:
        return sum(customers)
    elif n > len(customers): # When the number of tills is higher than the number of customers, the total time will simply be equal to the time spent by the "busiest" customer. 
        return max(customers)
    elif n < len(customers): 
        totaltime = [0] * n  # We initiate a list which contains a number of elements equal to the number of tills. This is to iterate through the "customers" list accordingly.
        for customertime in customers: 
            totaltime[totaltime.index(min(totaltime))] += customertime 
        return max(totaltime)
             
