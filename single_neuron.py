def weighted_sum_with_bias(x1, x2):
    w1 = 5.0
    w2 = 5.0
    bias = -5.0

    total = x1 * w1 + x2 * w2 + bias
    return 1 if total >= 1 else 0

try:
    x1 = int(input("Enter x1 (0 or 1): "))
    x2 = int(input("Enter x2 (0 or 1): "))

    if x1 not in [0, 1] or x2 not in [0, 1]:
        print("Inputs x1 and x2 must be either 0 or 1.")
    else:
        result = weighted_sum_with_bias(x1, x2)
        print("Output:", result)
except ValueError:
    print("Invalid input. Please enter numeric values.")