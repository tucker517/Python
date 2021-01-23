""" 
This is a basic demo to show how file operations are performed.
"""

# A very basic method to open files, not good as with a context manager.
# If we don't pass any args more we are reading the file. To write we pass 'w', appending to a file is a 'a', and reading is a 'r', to readandwrite is 'r+'
# f = open('test.txt', 'r')
# print(f.name)
# f.close() # If we don't explicitly close the file we can run into issues with leaks that cause applications to run over the maximum amount of file descriptors and cause system crashes.
# Now we use the context manager with. This is a file context manager. This handles operations like closure automatically and this is considered a best practice.

# with open('test.txt', 'r') as f:
#     size_to_read = 10 # Here we set a variable equal to int to pass to read.
#     
#     f_contents = f.read(size_to_read) # Here we initialize the f_contents variable and read the first 10 characters of the file.
#     
#     print(f.tell()) # Shows the int position of the current function.
#     f.seek(0) # Seek allows us to change the int position we are reading in the file. 
#     print(f.tell())
#     while len(f_contents) > 0: # If run alone this is an infinite loop because at this point f_contents is always > 0 if text is in the file.
#         print(f_contents, end='*') # Print an asterix after every 10th char to see whats happening.
#         f_contents = f.read(size_to_read) # Here we re-initialize the variable f_contents. Now python jumps back to the while loop and evaluates if the len is = 0. This checks that we are not at the end of the file and ends the loop once the len = 0.
          
#     f_contents = f.read(100) # Read accepts a int argument for number of characters to read- in.
#     print(f_contents, end='')
#     
#     f_contents = f.read(100) # If you do the same thing again downline in code, read picks up the count where it left off.
#     print(f_contents, end='')
    
#     for line in f: # This is not going to be a memory problem because it loops through each line and doesn't 
#         print(line, end='')
        
#     f_contents = f.read() # This reads the whole file, can cause problems with largefiles.
#     print(f_contents, end='')
#     f_contents = f.readlines() # This reads individual lines from a file everytime its called.
#     print(f_contents, end='')
    
    
# Now lets do some writing operations.
# 'a' lets us write to a file without overwriting the file.
# with open('test2.txt', 'w') as f:
#     f.write('Test Text for the new File!')
#     f.seek(0)
#     f.write('R') # Here we see that f.write only changes the first letter of the sentence because the position was reset and the character value updated.
    

# Now lets try to do some read/write write operations.

# with open('test.txt', 'r') as rf: # Reads a file
#     with open('test_copy.txt', 'w') as wf: # Opens and writes to a new file. 
#         for line in rf:
#             wf.write(line)
            
# Now lets work with pictures. The 'rb' kwarg allows us to read bit data instead of text. The 'wb' allows us to write bit data.
with open('tucker_pic.jpg', 'rb') as rf:
    with open('tucker_pic_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
            
        
            
            