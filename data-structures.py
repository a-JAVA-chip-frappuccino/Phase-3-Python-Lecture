# mutable: structure can be changed
# immutable: structure cannot be changed

# sequences

'''

for i in range(1, 6, 1): # (1, 2, 3, 4, 5)
    print(i)

for i in range(10, -1, -2): # (10, 8, 6, 4, 2, 0)
    print(i)

'''

# lists

'''

nums = [1, 2, 3, 4, 5]

nums[1] # returns item from list by index

len(nums) # length of list

nums.append(6) # adds item to end of list

poppedItem = nums.pop(3) # removes from end of list or by index (and returns)

nums.remove(1) # removes by item

nums[0:2] # returns sublist from list by index

colors = ["pink", "red", "green", "blue", "purple", "yellow", "orange", "grey"]

for i in range(len(colors)):
    print(colors[i])

i = 0

while i < len(colors):
    print(colors[i])
    i += 1 # same as i = i + 1

for color in colors:
    print(color)

colorsFirstLetter = []

for color in colors:
    if color[0] == 'p' or color[0] == 'g':
        colorsFirstLetter.append(color[0])

colorsFirstLetter2 = [color[0] for color in colors if color[0] == 'p' or color[0] == 'g']

nums = [0, 1, 2, 3, 4, 5]

numsCubed = []

for num in nums:
    if num > 1:
        numsCubed.append(num * num * num)

numsCubed2 = [(num * num * num) for num in nums if num > 1]

print(numsCubed2)

'''

# dictionaries

'''

squares = {1 : 1, 2 : 4, 3 : 9, 4 : 16}

squares[4]

squares[5] = 25

for key in squares:
    print(squares[key])

'''

# sets

'''

# animals = {"dog", "panda", "hamster"}

animals = set()

animals.add("hamster")
animals.add("dog")
animals.add("panda")
animals.add("dog") # will not add (duplicate)

for item in animals:
    print(item)

'''

# tuples

coordinate = (2, 4, -12) # (x, y, z) coordinate