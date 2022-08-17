def larger()
n1 = input('Insert first number:')
n2 = input('Insert second number:')
if n1>n2:
print('The greater number is {}'.format(n1))
elif n1==n2:
print('Both are Equal')
else:
print('The greater number is{}'.format(n2))
larger()
