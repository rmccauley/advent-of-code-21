f1 = open('day-1-a.txt', 'r')
Lines = f1.readlines()
previousDepth = None
increaseCount = 0

for currentDepth in Lines:
  currentDepth = int(currentDepth)
  if (previousDepth):
    if (currentDepth > previousDepth):
      increaseCount += 1

  previousDepth = currentDepth

print(increaseCount)

# Answer for my input: 1711