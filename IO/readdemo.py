f = open("demofile.txt", "a")
result = f.write("Hello my Name is Ankit Singh")
print(result)  # op:-28
f.close()


f = open("demofile.txt", "r")
print(f.read())


with open("demofile.txt") as f:
    print(f.read())

    """ op:-Hello my Name is Ankit Singh
        Hello my Name is Ankit Singh """
