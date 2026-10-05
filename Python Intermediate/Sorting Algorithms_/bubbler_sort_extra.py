def bubble_sort_steps(items):
    sorted_items = items.copy()
    iterations = 0
    swaps = 0

    for i in range(len(sorted_items) - 1):
        iterations += 1

        for j in range(len(sorted_items) - 1 - i):
            if sorted_items[j] > sorted_items[j + 1]:
                temporary = sorted_items[j]
                sorted_items[j] = sorted_items[j + 1]
                sorted_items[j + 1] = temporary
                swaps += 1

    return sorted_items, iterations, swaps


def validated_bubble_sort(items):
    if not isinstance(items, list):
        raise ValueError("Error: Input must be a list")

    if not items:
        raise ValueError("Error: List cannot be empty")

    if any(
        not isinstance(item, (int, float)) or isinstance(item, bool)
        for item in items
    ):
        raise ValueError("Error: List contains non-numeric elements")

    sorted_items, _, _ = bubble_sort_steps(items)
    return sorted_items