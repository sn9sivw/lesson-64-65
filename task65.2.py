import random


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    steps = 0
    while left <= right:
        steps += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return steps
        elif arr[mid] < target:
            right = mid - 1
        else:
            left = mid + 1
    return steps


def average_steps(num_trials=1000):
    total_steps = 0
    for _ in range(num_trials):
        array = sorted(random.sample(range(101), 32))
        target = random.randint(0, 100)
        total_steps += binary_search(array, target)
    average = total_steps / num_trials
    print(f"Среднее число шагов при двоичном поиске: {average:.2f}")


average_steps()
