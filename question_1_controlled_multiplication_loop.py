


# Set the maximum allowed value for the product
threshold = 100
# Initialize the product to 1 (multiplicative identity)
product = 1
# Start multiplying from the integer 1
currentNumber = 1


# Continue multiplying consecutive integers until the product exceeds the threshold
while product <= threshold:
    product *= currentNumber
    if product > threshold:
        break
    currentNumber += 1

#Print output
print(f"the final product is {product}. The integer that caused the product to exceed the threshold is {currentNumber}")

