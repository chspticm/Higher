# Something I was playing about with
# However https://www.clouddefense.ai/tools/code-checker/python points out the following.
# 1. The code has a logical error where it uses a while True loop to continuously prompt the user for input. However, the loop should have a condition to check if the input is a valid score to exit.
# 2. The use of except without specifying the type of exception to catch is not recommended as it can catch any exception, including unexpected ones. It is better to specify the type of exception to catch.
# 3. The code attempts to break out of the loop if an exception is raised, which is not ideal as it will break out of the loop regardless of the reason for the exception.
# 4. The total should be printed outside the loop or after the user enters a valid score, not in the finally block, to display the correct total.
# 5. The condition for exiting the loop should be based on the input score, not just on any exception being raised.

# which I totally agree with, just because it runs doesn't make it right.

total = 0
while True:
    try:
        print('Enter a non valid score to exit')
        score = int(input('What is the score?'))
        total = total + score
    except:
        break
    finally:
        print('The total is', total)
        
        