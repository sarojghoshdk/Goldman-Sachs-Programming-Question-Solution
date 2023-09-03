def maxLength(a, k):
    max_length = 0
    current_sum = 0
    left = 0

    for right in range(len(a)):
        current_sum += a[right]

        while current_sum > k:
            current_sum -= a[left]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

# Sample input
n = 3
a = [1, 2, 3]
k = 4
result = maxLength(a, k)
print(result)  # Output: 2
