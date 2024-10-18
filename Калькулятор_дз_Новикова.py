n1 = float(input('Enter first number: '))
n2 = float(input('Enter second number: '))
print('First number:', n1)
print('Second number:', n2)

message = ('\n'
           'Choice operation\n'
           '+: Addition\n'
           '-: Subtraction\n'
           '*: Multiplication\n'
           '/: Division\n'
           'Choice:\n')

choice = input(message)

if choice == '+':
    result = n1 + n2
elif choice == '-':
    result = n1 - n2
elif choice == '*':
    result = n1 * n2
elif choice == '/':
    try:
        result = n1 / n2
    except ZeroDivisionError:
        result = 'division by 0 is not allowed'
else:
    result = 'Unknown operation'

print('Result:', result)