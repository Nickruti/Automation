Input = open("input.txt", "a")
for i in range(1, 100):
    Input.write(str(i))
    Input.write("\n")
Input.close()
    