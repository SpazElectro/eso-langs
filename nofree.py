code = ""

for i in range(500):
    code += "save {} {}\n".format(i, i + 1)

with open("nofree.test", "w") as file:
    file.write(code)