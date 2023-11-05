# Function to solve the fractional knapsack problem
def fractional_knapsack(items, capacity):
    # Calculate the value-to-weight ratios for each item
    for item in items:
        item.append(item[1] / item[0])

    # Sort the items by their value-to-weight ratios in descending order
    items.sort(key=lambda x: x[2], reverse=True)

    total_value = 0
    remaining_capacity = capacity

    for item in items:
        weight, value, ratio = item
        if remaining_capacity >= weight:
            # Take the whole item
            total_value += value
            remaining_capacity -= weight
        else:
            # Take a fraction of the item
            fraction = remaining_capacity / weight
            total_value += fraction * value
            break

    return total_value

if __name__ == "__main__":
    items = [
        [10, 60],  # Weight, Value
        [20, 100],
        [30, 120]
    ]
    capacity = 50

    max_value = fractional_knapsack(items, capacity)
    print(f"Maximum value that can be obtained: {max_value}")

