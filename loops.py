

# loop for the list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# Loop through the letters in the word "banana":
for x in "banana":
  print(x)

# break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

# range 0 1 2 3 4 5 [0 - 6]
for x in range(6):
  print(x)

for x in range(2, 30, 3):
  print(x)

# Exception for loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")

# loop + inner loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

# loop for Dict (Map)
dictVar = {"key": "value"}
for k, v in dictVar.values():
    print(k)
    print(v)

# for loops cannot be empty,
# but if you for some reason have a for loop with no content,
# put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass

# continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# ------------------------------------------------------------

# while
i = 1
while i < 6:
    print(i)
    i += 1



