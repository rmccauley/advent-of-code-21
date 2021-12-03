f1 = open('day-2-a.txt', 'r')
Lines = f1.readlines()
fCount = 0
eCount = 0

for line in Lines:
  direction = line.split(' ')[0]
  count = int(line.split(' ')[1].strip())

  if direction == 'forward':
    fCount += count
  elif direction == 'down':
    eCount += count
  elif direction == 'up':
    eCount -= count

print(fCount*eCount)

# Answer for my input: 1947824