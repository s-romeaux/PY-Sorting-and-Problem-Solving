# Write your solution for algorithm 2 below
def sort_list(input_list):
    sorted_list = sorted(input_list)
    return sorted_list

sample_list = [22, 87, 5, 91, 34, 74, 92, 68, 43, 11, 26, 3, 65, 19, 57]
print(f"Unsorted list: {sample_list}")

# Creating a new sorted list using the sort_list function
sorted_sample_list = sort_list(sample_list)
print(f"Employing the stated method: {sorted_sample_list}")
