number = int(input("Enter an integer: "))
product_of_numbers = 1
for digit in str(number):
    product_of_numbers *= int(digit)
    if product_of_numbers < 9:
        break

print("Product of an integer:", product_of_numbers)