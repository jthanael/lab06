import sys
print("Total arguments:", len(sys.argv))
print("Script name:", sys.argv[0])
print("Arguments:", sys.argv[1:])
total = 0
for arg in sys.argv[1:]:
    total += int(arg)
print("Sum =", total)


# python3 add.py 1 2 3 to call it from the command line.
