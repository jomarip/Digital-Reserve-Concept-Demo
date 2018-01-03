
import sys
import operator

#customer attributes are considered favorable in the following order.
#excluding name data


#attribute 0:'First Name',
#attribute 1::'Last Name',
#attribute 2:'Loan Amount Requested',
#attribute 3:'Loan Period Requested',
#attribute 4:'Interest Rate',
#attribute 5:'Credit Score'

#List of Digital Reserve Clients
s =[['Sally', 'Henderson', 750.00, 4, 12, 738],
['Henry', 'James', 375.00, 3, 22, 800],
['Jeff', 'Madison', 250.00, 24, 16, 642],
['Marcus', 'Mills', 400.00, 3, 21, 723]]
#Sort by attributes 1 and 

#sorts for the lowest loan amount
s = sorted(s, key = operator.itemgetter(2))
print(s)

#sorts for the lowest loan period in ages
s = sorted(s, key = operator.itemgetter(3))
print(s)

#sorts for the highest interest rate
s = sorted(s, key = operator.itemgetter(4), reverse=True)
print(s)

#sorts for the highest credit score
s = sorted(s, key = operator.itemgetter(5), reverse=True)
print (s)

print ("Loan Bid Was Won By: ", s[0])
