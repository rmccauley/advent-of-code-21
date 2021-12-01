f1 = open('day-1-b.txt', 'r')
Lines = f1.readlines()
previousDepth = None
increaseCount = 0
i = 0

for line in Lines:
  if (i == 2): # set first reading
    previousDepth = int(Lines[i])+int(Lines[i-1])+int(Lines[i-2])
  elif i > 2: # start comparing and setting fresh previous readings
    currentDepth = int(Lines[i])+int(Lines[i-1])+int(Lines[i-2])
    if currentDepth > previousDepth:
      increaseCount += 1
    previousDepth = currentDepth
  i += 1

print(increaseCount)

# Answer: 1743