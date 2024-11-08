# Higher Algorithms Tasks
Each bullet point is a task. in the form
- Filename
    - Task Description

Save each task with the filename of the main bullet point. copy and paste the description into the file, add your name and date. By now all of your programs should be modular. Use the "Higher Algorithms.md" file to track your progress

## File Access
- Reading from text file - Single Value
    - Read the contents of file1.txt and display them on screen
- Writing to text file - Single Value
    - Write your name to the file name.txt
- Reading from text file - Multiple Value
    - Read the contents of file2.txt into an Array name[4] String) and then display the array contents. 
- Writing to text file - Multiple Value
    - Enter five test scores (0-100) into an Array and write the array to the file scores.txt.
- Reading from CSV file into parallel arrays
    - Read the contents of the file file3.csv into the following arrays name[5] (String), score[5] (Integer), pass[5] (Boolean)
- Writing parallel arrays into a CSV file
    - Enter 5 place names and their populations into an Array, write the contents of the arrays to the file places.txt
- Reading from CSV file into array of records
    - Read the contents of the file file4.csv into the array of records birds[10] Bird(name (string), wingspan (real), species (string)) display the array’s contents in a table 
- Writing from an array of records into a CSV file
    - Create an array of record[5] people(forename(string), day of birth(integer), month of birth(integer), year of birth(integer)), populate the array and write it to the file friends.csv
  
## String Handling / Slicing
- Extract Character from the left of a string
    - Display the first 5 letters of the string ‘Computing’
- Extract Character from the right of a string
    - Display the last 5 letters of the string ‘Science’
- Extract Character from the middle of a string
    - Display from the 3rd to 8th characters of ‘Save the world’
- Concatenate a new string from the sub-strings of two or more other strings
    - Display the string using the first 5 characters of ‘Robertson’ and last 2 of ‘2025’

## Pre-defined functions
- Convert from ASCII to Character
    - Use a loop to display your name in ASCII codes
- Convert from Character to ASCII
    - Display the ASCII codes for a..z and A..Z in a table with the character
- Modulus
    - Display the number of meters and centimetres separately for 5 given heights (1.85, 2.60, 1.5, 3.67, 4.98)

## Higher Standard Algorithms

### Using **Arrays** returning **Value**
- Find Max - whole array traversed
    - Which of these numbers is the largest [10,12,32,45,32,56,43,12,23,2] ?
- Find Min - whole array traversed
    - Which of these words is the shortest? [Barlowe, Caddel, Hart, Kaz, Laurier, Madden, Elrod, Whitlock].
- Count Occurrences - whole array traversed
    - How many times does the letter 'o' appear in this string? 'Man I love computing, so much'
- Linear Search - Whole array traversed
    - Does the number 8 appear in this list? [5,7,6,5,4,3,4,9,7,5,4,3,5,6,2]
- Linear Search - Returns when found
    - is the number 7 on this list? [5,7,6,5,4,3,4,9,7,5,4,3,5,6,2]. Display the number of times the array was traversed

### Using **Arrays** returning **Position**
- Find Max - whole array traversed
    - What is the position of the largest number [10,12,32,45,32,56,43,12,23,2] ?
- Find Min - whole array traversed
    - What is the position of the shortest word? [Barlowe, Caddel, Hart, Kaz, Laurier, Madden, Elrod, Whitlock].
- Count Occurrences - whole array traversed
    - Display the positions of the number 5 and how many times it appears in this list? [5,7,6,5,4,3,4,9,7,5,4,3,5,6,2]
- Linear Search - Whole array traversed
    - At what position does the number 8 appear in this list? [5,7,6,5,4,3,4,9,7,5,4,3,5,6,2]
- Linear Search - Returns when found
    - Display the position of the number 5 on this list. [5,7,6,5,4,3,4,9,7,5,4,3,5,6,2]

### Using **Array of records** returning **Value**
- Find Max - whole array traversed
    - Read the contents of the file file4.csv into the array of records birds[10] Bird(name (string), wingspan (real), species (string)). Display the name of the bird with the shortest wingspan.
- Find Min - whole array traversed
    - Read the contents of the file file4.csv into the array of records birds[10] Bird(name (string), wingspan (real), species (string)). Display the name of the bird with the shortest species name.
- Count Occurrences - whole array traversed
    - Read the contents of the file file3.csv into the array of records Pupil (name[5] (String), score[5] (Integer), pass[5] (Boolean)). How many passed?
- Linear Search - Whole array traversed
    - for the task above what were their names?
- Linear Search - Returns when found
    - Read the contents of the file file4.csv into the array of records birds[10] Bird(name (string), wingspan (real), species (string)). Are there any owls in the file?

### Using **Array of records** returning **Position**
- Find Max - whole array traversed
    - Read the contents of the file file3.csv into the array of records Pupil (name[5] (String), score[5] (Integer), pass[5] (Boolean)). What is the position of the pupil with the highest mark?
- Find Min - whole array traversed
    - Read the contents of the file file3.csv into the array of records Pupil (name[5] (String), score[5] (Integer), pass[5] (Boolean)). What is the position of the lowest scoring pupil?
- Count Occurrences - whole array traversed
    - Read the contents of the file file3.csv into the array of records Pupil (name[5] (String), score[5] (Integer), pass[5] (Boolean)). How many pupils have 3 letter names?
- Linear Search - Whole array traversed
    - Read the contents of the file file3.csv into the array of records Pupil (name[5] (String), score[5] (Integer), pass[5] (Boolean)). Display all the positions of the pupils that passed.
- Linear Search - Returns when 
    - Read the contents of the file file3.csv into the array of records Pupil (name[5] (String), score[5] (Integer), pass[5] (Boolean)). Did anyone fail?
