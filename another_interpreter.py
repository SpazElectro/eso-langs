import sys

try:
    file = sys.argv[1]
except:
    print("No file provided.")
    exit()

variables = {}

with open(file) as f:
    data = f.read()

    lines = data.split("\n")

    for fullLine in lines:
        line = fullLine.split(" ")

        if line[0] == "print":
            try:
                testArguments = line[1]
            except:
                print("ERROR: No print arguments at line " + str(lines.index(fullLine) + 1))
                break

            if fullLine[6:7] == "$":
                try:
                    testVariable = variables[fullLine[7:]]
                except:
                    print("ERROR: Variable {} is not defined".format(fullLine[7:]))
                    break

                print(variables[fullLine[7:]])
            else:
                print(fullLine[6:])
        elif line[0] == "save":
            try:
                testArguments = line[1]
            except:
                print("ERROR: No save arguments at line " + str(lines.index(fullLine) + 1))
                break
            try:
                testArguments = line[2]
            except:
                print("ERROR: No save arguments at line " + str(lines.index(fullLine) + 1))
                break
            
            try:
                variables[line[1]] = int(fullLine[6 + line[1].__len__():])
            except:
                variables[line[1]] = fullLine[6 + line[1].__len__():]
        elif line[0] == "free":
            try:
                testArguments = line[1]
            except:
                print("ERROR: No free arguments at line " + str(lines.index(fullLine) + 1))
                break

            del variables[line[1]]
        
        try:
            if variables[line[0]]:
                if line[1] == "+=":
                    variables[str(line[0])] += int(line[2])
                elif line[1] == "-=":
                    variables[str(line[0])] -= int(line[2])
                elif line[1] == "=":
                    try:
                        variables[str(line[0])] = int(line[2])
                    except Exception as e:
                        variables[str(line[0])] = line[2]
                elif line[1] == "/=":
                    variables[str(line[0])] /= int(line[2])
                elif line[1] == "*=":
                    variables[str(line[0])] *= int(line[2])
        except:
            pass

input("")