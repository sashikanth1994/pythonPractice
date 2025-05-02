def printTextFiles (lis : list):
    for l in lis:
        with open(l, "r") as file:
            print(file.read())

if __name__ == "__main__":
    file = open("members.txt", "a")
    # existing_members = file.readlines()
    newName = input("Enter a name which needs to be added: ")

    file.write("\n" + newName)
    file.close()

    printTextFiles(["a.txt", "b.txt", "c.txt"])


