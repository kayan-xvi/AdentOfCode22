from collections import defaultdict

with open(r'Python\Advent of Code 22\Advent7Input.txt') as r: 
    input = r.read().split('\n')



# Function to parse a line of input
def parse_input_line(line):
  if line.startswith('$'):
    # Split the line by space to get the command and arguments
    parts = line.split(' ')
    command = parts[0][1:] # remove the leading $ and the space
    args = parts[1:]
    return command, args
  else:
    # Split the line by space to get the size and name
    parts = line.split(' ')
    print(parts)
    size = int(parts[0])
    name = parts[1]
    return size, name

# Function to process the input
def process_input(input_lines):
  # Initialize the filesystem as a dictionary
  filesystem = {}
  
  # Initialize the current directory as /
  current_directory = '/'
  
  # Initialize the total size of each directory as a dictionary
  total_sizes = defaultdict(int)
  
  # Iterate through the input lines
  for line in input_lines:
    # Parse the line
    parsed_line = parse_input_line(line)
    
    # If the line is a command
    if isinstance(parsed_line, tuple):
      command, args = parsed_line
      # If the command is cd
      if command == 'cd':
        # If the argument is /, set the current directory to /
        if args[0] == '/':
          current_directory = '/'
        # If the argument is .., move one level up
        elif args[0] == '..':
          current_directory = current_directory.rsplit('/', 1)[0]
        # Otherwise, move one level down
        else:
          current_directory += '/' + args[0]
      # If the command is ls, add the contents to the filesystem
      elif command == 'ls':
        filesystem[current_directory] = args
    
    # If the line is a file or directory
    else:
      size, name = parsed_line
      # Update the total size of the current directory
      total_sizes[current_directory] += size
      # Update the filesystem with the file or directory
      filesystem[current_directory].append((size, name))
  
  return filesystem, total_sizes

# Function to find the total size of a directory
def find_total_size(filesystem, total_sizes, directory):
  # If the total size of the directory has already been calculated, return it
  if directory in total_sizes:
    return total_sizes[directory]
  
  # Initialize the total size as 0
  total_size = 0
  
  # Iterate through the contents of the directory
  for content in input:
    # If the content is a tuple, it is a file
    if isinstance(content, tuple):
      size, name = content
      # Add the size of the file to the total size
      total_size += size
    # If the content is a string, it is a directory
    else:
      # Find the total size of the directory
      total_size += find_total_size(filesystem, total_sizes, content)

  print(total_size)

for line in input: 
    print(line)
    parse_input_line(line)