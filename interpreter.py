import sys

try:
    file = sys.argv[1]
except:
    print("No file provided.")
    exit()

cells = [0]
currentCellPosition = 0

def testIfCellExists():
    try:
        cellExistsTest = cells[currentCellPosition]
    except:
        cells.append(0)

with open(file) as f:
    data = f.read()
    charIndex = 0

    for char in data:
        charIndex += 1

        if char == ">":
            currentCellPosition += 1

            testIfCellExists()
            
        elif char == "<":
            currentCellPosition -= 1

            if currentCellPosition < 0:
                print("Error at char " + str(charIndex) + ", Cell position cannot be lower than 0")
                break
        elif char == "+":
            testIfCellExists()
            
            cells[currentCellPosition] += 1
        elif char == "-":
            testIfCellExists()
            
            cells[currentCellPosition] -= 1
        elif char == ".":
            testIfCellExists()
            
            print("> {}".format(cells[currentCellPosition]))
        elif char == "/":
            testIfCellExists()
            
            cells[currentCellPosition] /= 2
        elif char == "*":
            testIfCellExists()
            
            cells[currentCellPosition] *= 2
    
    print("Cells used: {} File characters: {}".format(len(cells), charIndex))