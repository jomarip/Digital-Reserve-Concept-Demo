
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
['Henry', 'James', 375.00, 28, 22, 800],
['Jeff', 'Madison', 250.00, 24, 16, 642],
['Marcus', 'Mills', 400.00, 3, 21, 723],
['Nate', 'Bradshaw', 120.00, 20, 19, 825],
['Amanda', 'Jefferson', 145.00, 8, 1, 714],
['Jessica', 'Jones', 75.00, 6, 17, 660],
['Alexandra', 'Harris', 1000.00, 7, 14, 764],
['Mason', 'Viri', 1250.00, 19, 25, 807],
['Jed', 'Chan', 950.00, 23, 5, 593],
['David', 'Mitts', 780.00, 12, 23, 803],
['Justin', 'Jackson', 50.00, 18, 11, 605],
['Rick', 'Stone', 1400.00, 16, 18, 755],
['Ed', 'Sanderson', 570.00, 30, 13, 711],
['Ashley', 'Willis', 375.00, 27, 7, 698],
['Kathryn', 'London', 800.00, 26, 4, 582],
['Jignesh', 'Dashi', 650.00, 5, 24, 616],
['Kendrick', 'Blicks', 330.00, 11, 15, 850],
['Molly', 'James', 195.00, 15, 3, 679],
['Issa', 'Rae', 45.00, 21, 9, 681],
['Riley', 'Banks', 30.00, 10, 20, 771],
['Iman', 'Hill', 930.00, 13, 6, 757],
['Ted', 'Williams', 870.00, 14, 8, 695],
['Will', 'Smith', 675.00, 22, 2, 601]]
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
