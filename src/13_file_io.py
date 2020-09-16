"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
text = open('foo.txt', 'r')
print(text.read())
text.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
text2 = open('bar.txt', 'w')
text2.write('Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit, sed do eiusmo\nconsectetur adipiscing elit, sed do eiusmo')
text2.close()

text2 = open('bar.txt', 'r')
print(text2.read())
text2.close()

