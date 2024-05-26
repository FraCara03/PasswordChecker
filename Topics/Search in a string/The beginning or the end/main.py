a = input()
start_index = a.find("old")  # Find the first occurrence of "old"
end_index = a.find("old", start_index + 1)  # Find the second occurrence of "old" after the start_index
print(end_index)
