import csv
import time
from time import perf_counter_ns
from collections import defaultdict
import copy

columns = defaultdict(list)

# read the csv file as a dictionary of lists
with open('planets.csv') as planets:
    reader = csv.DictReader(planets)
    for row in reader:
        for (k, v) in row.items():
            columns[k].append(v)


def selectionSort(mass_column):
    steps = 0  # define a local variable to count the steps

    # Outer for loop that loops for every element in the list
    for i in range(len(mass_column) - 1):
        min = i  # set the minimum value to be i

        # Inner for loop that loops for every element in between the min value and the end of the list
        for j in range(min + 1, len(mass_column)):
            steps += 1

            # If the element in the min index is bigger than the target element j, then j becomes the minimum element
            if float(mass_column[j]) < float(mass_column[min]):
                min = j

        mass_column[i], mass_column[min] = mass_column[min], mass_column[i]  # switch the values at index i and min

    return steps


def insertionSort(mass_column_2):
    steps = 0  # define a local variable to count the steps

    # Check if the list has 1 or fewer elements. If so, the list is already sorted
    if len(mass_column_2) <= 1:
        return steps

    # Loop through every element on the list but the first one (index 0)
    for i in range(1, len(mass_column_2)):
        key = float(mass_column_2[i])  # set the key to be the value at index i
        j = i - 1  # set the value j to be one value less than the key value

        #  Loop while the key value is smaller than the value before it
        while key < float(mass_column_2[j]):
            mass_column_2[j + 1] = str(mass_column_2[j])  # Move the value of j to the right of the list to make space
            # for the insertion of the key value
            j -= 1  # Make j be one value less
            steps += 1  # Increment one step

        mass_column_2[j + 1] = str(key)  # After the proper space has been made, insert the key value at the right spot
    return steps


# Display the initial list that will be later be sorted
print("Original Mass Data:")
print(f" {columns['Mass (10^24kg)']} \n")

# Loop 100 times
for i in range(1, 101):
    mass_column = copy.copy(columns["Mass (10^24kg)"])  # Copy the data into a variable that will be sorted
    mass_column_2 = copy.copy(columns["Mass (10^24kg)"])  # Copy the data into a variable that will be sorted

    print(f"Starting Selection Sort: {i} \n")
    t1_start = perf_counter_ns()  # Starting point for the time counter
    print(f"Steps taken: {selectionSort(mass_column)}")
    t1_stop = perf_counter_ns()  # Ending point for the time counter
    print(f"Sorted data: {mass_column}")
    print(f"Time taken: {t1_stop - t1_start}")

    print(f"\nStarting Insertion Sort: {i} \n")
    t2_start = perf_counter_ns()  # Starting point for the time counter
    print(f"Steps taken: {insertionSort(mass_column_2)}")
    t2_stop = perf_counter_ns()  # Ending point for the time counter
    print(f"Sorted data: {mass_column_2}")
    print(f"Time taken: {t2_stop - t2_start}")

    print("\nSleeping...\n")

    time.sleep(1)
