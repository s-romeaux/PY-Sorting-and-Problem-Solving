# Write your solution for algorithm 3 below
def sort_descending(input_list):
    sorted_desc_list = sorted(input_list, reverse=True)
    return sorted_desc_list

sample_list = [22, 87, 5, 91, 34, 74, 92, 68, 43, 11, 26, 3, 65, 19, 57]
print(f"Unsorted list: {sample_list}")

# Creating a new sorted list in descending order using sort_descending function
sorted_desc_sample_list = sort_descending(sample_list)
print(f"Employing the stated method: {sorted_desc_sample_list}")
