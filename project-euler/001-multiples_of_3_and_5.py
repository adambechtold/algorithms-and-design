from typing import List

# link: https://projecteuler.net/problem=1
# date: 2024.02.18

def sum_multiples(maximum_number: int, multiples: List[int]) -> int:
    count = 0

    for num in range(1, maximum_number + 1):
        for m in multiples:
            if num % m == 0:
                count += num
                break

    return count

print(sum_multiples(9, [3,5]))
print(sum_multiples(999, [3, 5]))

