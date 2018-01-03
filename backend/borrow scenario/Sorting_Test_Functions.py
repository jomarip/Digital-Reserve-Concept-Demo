
import sys
import operator

#

#attribute 0:'First Name',
#attribute 1::'Last Name',
#attribute 2:'Loan Amount Requested',
#attribute 3:'Loan Period Requested',
#attribute 4:'Interest Rate',
#attribute 5:'Credit Score'

#List of Digital Reserve Clients
s =[['Sally', 'Henderson', '750', '4', '12', '738'],
['Henry', 'James', '375', '28', '22', '800'],
['Jeff', 'Madison', '250', '24', '16', '642'],
['Marcus', 'Mills', '400', '3', '21', '723'],
['Nate', 'Bradshaw', '120', '20', '19', '825'],
['Amanda', 'Jefferson', '145', '8', '1', '714'],
['Jessica', 'Jones', '75', '6', '17', '660'],
['Alexandra', 'Harris', '1000', '7', '14', '764'],
['Mason', 'Viri', '1250', '19', '25', '807'],
['Jed', 'Chan', '950', '23', '5', '593'],
['David', 'Mitts', '780', '12', '23', '803'],
['Justin', 'Jackson', '50', '18', '11', '605'],
['Rick', 'Stone', '1400', '16', '18', '755'],
['Ed', 'Sanderson', '570', '30', '13', '711'],
['Ashley', 'Willis', '375', '27', '7', '698'],
['Kathryn', 'London', '800', '26', '4', '582'],
['Jignesh', 'Dashi', '650', '5', '24', '616'],
['Kendrick', 'Blicks', '330', '11', '15', '850'],
['Molly', 'James', '195', '15', '3', '679'],
['Issa', 'Rae', '45', '21', '9', '681'],
['Riley', 'Banks', '30', '10', '20', '771'],
['Iman', 'Hill', '930', '13', '6', '757'],
['Ted', 'Williams', '870', '14', '8', '695'],
['Will', 'Smith', '675', '22', '2', '601']]

#Sort by attributes 1 and 

s = sorted(s, key = operator.itemgetter(2),reverse = True)

print (s)
