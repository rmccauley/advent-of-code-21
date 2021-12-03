f1 = open('day-3-a.txt', 'r')
Lines = f1.readlines()
gamma = ''
epsilon = ''

def binaryToDecimal(binaryVal):
  res = 0
  for digit in binaryVal:
    res = res * 2 + int(digit)
  return res

# Create an array of 0's as long as the first line's count since all lines are of equal length
# This will count up for each '1' in the list
positionCounter = [0] * len(Lines[1].strip())

count = 0
for line in Lines: # Loop over each line
  for n in range(0, len(Lines[1].strip())): # Variable length lines, loop over each character, strip newline
    positionCounter[n] += int(Lines[count].strip()[n]) # Increment the counter in this position
  count += 1

for x in range(0, len(positionCounter)):
  # Turn truthy values into integers, then back into string to build out the gamma and epsilon strings
  gamma += str(int(positionCounter[x] > count/2))
  epsilon += str(int(positionCounter[x] <= count/2))

gammaBinaryValue = binaryToDecimal(gamma)
epsilonBinaryValue = binaryToDecimal(epsilon)

print('Gamma Binary = ' + gamma)
print('Epsilon Binary = ' + epsilon)
print('Gamma Binary Value = ' + str(gammaBinaryValue))
print('Epsilon Binary Value = ' + str(epsilonBinaryValue))
print('Result: ' + str(gammaBinaryValue * epsilonBinaryValue))



# Answer: 4006064