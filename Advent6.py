with open(r'Python\Advent of Code 22\Advent6Input.txt') as r: 
    input = r.read()
print(len(input))

def find_start_of_packet_marker(datastream):
  # Initialize a list to store the last four characters received
  last_four = []

  # Iterate through the datastream
  for i, c in enumerate(datastream):
    # Add the current character to the list of last four characters
    last_four.append(c)
    # If the list has more than four elements, remove the first element
    if len(last_four) > 14:
      last_four.pop(0)
    # If the last four characters are all different, return the index of the current character
    if len(set(last_four)) == 14:
        print(last_four)
        return i + 1

# Test the function
result = find_start_of_packet_marker(input)
print(result)  # Output: 7