import difflib

# filename1 = input("Link to Standard File: ")
# filename2 = input("Link to Comparing file: ")

# file1 = open(filename1)
# file2 = open(filename2)

file1 = open("textfile1.txt")
file2 = open("textfile2.txt")

print("Comparing files for any differences")

diff = difflib.ndiff(file1.readlines(), file2.readlines())
delta = ''.join(x[0:] for x in diff if x.startswith('- '))
print (delta)

file1.close()
file2.close()
