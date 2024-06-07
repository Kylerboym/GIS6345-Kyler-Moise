def nested_sum(nested_lists):
    total = 0
    for sublist in nested_lists:
        total += sum(sublist)
    return total

# Example usage:
t = [[1, 2], [3], [4, 5, 6]]
print(nested_sum(t))  # Output: 21