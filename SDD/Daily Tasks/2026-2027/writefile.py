# reading and writing from a file
# Mr Stratton
# 10/09/26

def main():
    # Writing to a file
    txtFile = open('name.txt','w') # Write to the file
    txtFile.write('Mr Stratton \n') # /n means take a new line
    txtFile.write('Woz \'ere')   
    txtFile.close()
    
    # Writing to a file
    txtFile = open('name.txt','a') # Append to the file
    txtFile.write('New Message here') # /n means take a new line
    txtFile.close()
    
    # Read from a file
    txtFile = open('name.txt','r') # open the file to read
    message = txtFile.read() # read in the contents of the file
    print(message) # display the stored contents
    txtFile.close() # close the file

main()