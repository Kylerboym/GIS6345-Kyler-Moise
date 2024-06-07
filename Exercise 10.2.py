def cumsum(numbers):
    cumulative_sum = []
    total = 0
    for number in numbers:
        total += number
        cumulative_sum.append(total)
    return cumulative_sum

# Example usage:
t = [1, 2, 3]
print(cumsum(t))  # Output: [1, 3, 6]
