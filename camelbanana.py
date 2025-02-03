def camel_banana(n, d, c):
    bananas_left = n
    trips = 0

    while bananas_left > 0:
        if bananas_left <= c:
            return bananas_left - d

        max_trips = (bananas_left + c - 1) // c
        bananas_left -= 2 * (max_trips - 1) + 1
        trips += 1

        if trips == d:
            break

    return bananas_left

# Example
print(camel_banana(3000, 1000, 1000))
