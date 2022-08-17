def smaller()
n1 = input('Insert first number:')
n2 = input('Insert second number:')
if n1>n2:
print('The smaller number is {}'.format(n2))
elif n1==n2:
print('Both are Equal')
else:
print('The smaller number is{}'.format(n1))
smaller()
