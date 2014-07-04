# input will prompt user for a bill amount at the command line
amount = float(input('Enter the amount of the bill: '))

tip_15 = amount * .15
tip_20 = amount * 0.2

print('A 15%% tip is: %.2f. A 20%% tip is: %.2f.' % (tip_15, tip_20))

print('Total price with 15%% tip is: %.2f' % (amount + tip_15))
print('Total price with 20%% tip is: %.2f' % (amount + tip_20))
input('Press ENTER to exit')
