"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
with open('src/foo.txt') as f:
    print(f.read())
    f.close()
    if f.closed:
        print('File was closed!')

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
with open('src/bar.txt', 'w') as f:
    f.write('My name is Daisy. \n')
    f.write('I like Python. \n')
    f.write('Even though it kind of confuses me. \n')
    f.close()
    if f.closed:
        print('Second file was closed!')
