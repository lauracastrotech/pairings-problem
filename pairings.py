def find_pairs(num_string):
  # Split the string into list of positive nubmers
  # Convert each number to an int
  # Loop through my list compare the current value with remaining items by looping through the list as well
  # Create two value tuple based on the comparison
  # Add the tuple to the set
  # return the set
  pairs = set()

  if not len(num_string) > 1:
    return pairs
  
  list_of_nums = num_string.split(' ')
  list_of_ints = [int(num) for num in list_of_nums]
  # print(f'{list_of_nums=}')
  # print(f'{list_of_ints=}')
  for int_num in list_of_ints:
    num_tup = ()
    for next_int in list_of_ints:
      if int_num < next_int:
        num_tup = (int_num, next_int)
        pairs.add(num_tup)
  
  return pairs


# Test cases
assert find_pairs("7 3 99") == {(7, 99), (3, 7), (3, 99)}
assert find_pairs("2 1") == {(1, 2)}
assert find_pairs("24 7 365 94") == {(7, 94), (24, 94), (94, 365), (7, 365), (24, 365), (7, 24)}
assert find_pairs("94") == set()

print("All tests passed!")
print("Finished early? Discuss time & space complexity")