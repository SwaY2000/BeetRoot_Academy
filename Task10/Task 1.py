def entry():
    with open("myfile.txt", "w+") as f:
        f.write(f"Hello file world")
        f.close()
def printf():
    with open("myfile.txt", "r+") as f:
        print(f.read())
#entry()
printf()