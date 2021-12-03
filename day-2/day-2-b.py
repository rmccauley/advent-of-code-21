f1 = open('day-2-b.txt', 'r')
Lines = f1.readlines()
fCount = 0
pfCount = 0
eCount = 0
aim = 0

for line in Lines:
  direction = line.split(' ')[0]
  count = int(line.split(' ')[1].strip())

  if direction == 'forward': #only increase depth when moving forward
    fCount += count
    pfCount = count
    if aim != '0':
      eCount += aim * pfCount
  elif direction == 'down':
    aim += count
  elif direction == 'up':
    aim -= count

print(fCount*eCount)

# Answer for my input: 1813062561