import csv
import time
from time import perf_counter_ns
from collections import defaultdict

columns = defaultdict(list)
total_and_name = []

# Read the csv file into colums[x] that will separate each column into a dictionary using the first value as a key.
with open('Pokemon_numerical.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        for (k, v) in row.items():
            columns[k].append(v)
        total_and_name.append((int(row["Total"]), row["Name"]))  # Create a list that stores the names and totals

    total_and_name = sorted(total_and_name)  # Sort by total


# Function to make the linear search
def linear_search():
    poison_count = 0
    for i in range(len(columns["Name"])):
        if columns["Type 1"][i] == "Poison":  # Check if the value "Poison" is in the "Type 1" column.
            poison_count += 1
        elif columns["Type 2"][i] == "Poison":  # Check if the value "Poison" is in the "Type 2" column.
            poison_count += 1
    return poison_count


# Function to make the binary search
def binary_search(pokemon_totals, low, high, x):
    values_found = {}

    # Loop until the low value is higher than the high value
    while high >= low:
        mid = (high + low) // 2  # Calculate the middle value

        if pokemon_totals[mid][0] == x:  # Checks if the first value of the tuple matches with the value searched
            values_found[pokemon_totals[mid][1]] = x

            # Search to the left of mid
            temp_mid = mid - 1
            while temp_mid >= low and pokemon_totals[temp_mid][0] == x:
                values_found[pokemon_totals[temp_mid][1]] = x
                temp_mid -= 1

            # Search to the right of mid
            temp_mid = mid + 1
            while temp_mid <= high and pokemon_totals[temp_mid][0] == x:
                values_found[pokemon_totals[temp_mid][1]] = x
                temp_mid += 1
            break

        # If the value was not found, and the target value is bigger than the middle value,
        # it looks for the upper part of the list
        elif pokemon_totals[mid][0] < x:
            low = mid + 1

        # If the value was not found, and the target value is lower than the middle value,
        # it looks for the lower part of the list
        else:
            high = mid - 1
    return values_found


# Loops 100 times doing both searches
for i in range(1, 101):

    print(f"Starting linear problem {i}")
    t1_start = perf_counter_ns()  # Set the starting point for the time calculator
    linear_result = linear_search()
    t1_stop = perf_counter_ns()  # Set the stopping point for the time calculator
    print(f"Time taken: {t1_stop - t1_start} nanoseconds")
    print(f"Frequency of Poison found: {linear_result} \n")

    print(f"Starting binary problem {i}")
    t2_start = perf_counter_ns()  # Set the starting point for the time calculator
    binary_result = binary_search(total_and_name, 0, len(total_and_name) - 1, total_and_name[-1][0])
    t2_stop = perf_counter_ns()  # Set the stopping point for the time calculator
    print(f"Time taken: {t2_stop - t2_start} nanoseconds")
    print(f"Key / Value Maximums: {binary_result}")

    if i != 100:
        print("\nSleeping....\n")
        time.sleep(2)
    else:
        time.sleep(1)
        print("\nSearch finished.\n")


