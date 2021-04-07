# This is a skeleton for your assignment 2 program.
# It contains the program structure, function names,
# the main function already written,
# and comment instructions regarding what you should write.

# Import the system module
import sys

# Import regular expressions module
import re

'''
The below function should be called on a file name.
It should open the file, read its contents, and store it in a variable.
Then it should remove punctuation marks and return the "cleaned" text.
'''


def cleanFileContents(f):
    # The below two lines open the file and read all the text from it
    # storing it into a variable called "text".
    # Set a breakpoint to line 15 and inspect the contents of the variable "text"
    # before and after executing the read() statement.
    # You do not need to modify the below two lines; they are already working as needed.
    with open(f, 'r') as f:
        text = f.read()

    # Review the regular expressions slides/reading and write a statement using regular
    # expressions below such that the following characters are replaced by "nothing": ,.!()-?;:"
    # (Remember to do exactly this and not something else, even if you think something else is better!
    # The assignment will be graded AUTOMATICALLY, and if you do something else, your output may be different.
    # Regardless of whether it is better or worse than the solution, you may be marked down if your output is different!)

    # Replace the below line by your call to the appropriate function of the regular expression module here.
    # Review the lecture/readings on regular expressions. You want the re.sub function.
    # Read its documentation to understand which argument goes where in the parentheses.
    # As it is, the below line simply assigns the value of the incoming "text" to a new variable called
    # "clean_text". There will be no difference between them if you leave it as is.
    clean_text = text  # Modify this statement!

    # Now, we will want to replace all tabs with spaces, and also all occurrences of more than one
    # space in a row with a single space. Review the regular expression slides/readings, and
    # write a statement below which replaces all occurrences of one or more whitespace-group characters
    # (that will include tabs) with a single space.

    # Your call to the appropriate function of the regular expression module here.
    # As is, this "pass" statement is doing nothing at all.
    pass  # Modify this statement!

    # Do not forget to return the result!
    return clean_text


'''
The below function takes a string as input, breaks it down into word tokens by space, and stores, in a dictionary table,
how many times each word occurred in the text. It returns the dictionary table.
'''


def countTokens(text):
    # Initializing an empty dictionary. Do not modify the line below, it is already doing what is needed.
    token_counts = {}

    # Use the split() function, defined for strings, to split the text by space.
    # Store the result in a variable, e.g. called "tokens". That variable will be of type "list".
    # You can see that if you step through the execution in the debugger.

    # Split the text into tokens here, as described above.

    # Iterate over each word in the list of tokens (write a for loop over the list).
    # Inside the loop:
    # If the word is not yet stored in the dictionary
    # "token_counts" as a key, store it there now, and initialize the key's value to 0.
    # Outside that if statement: now that we are sure the word is stored as a key, increment the count by 1.

    # Write a for loop here, doing what is described above.

    # Do not forget to return the result!
    return token_counts


'''
This silly "prediction funtion" will do the following "rudimentary data science":
If a review contains more of the word "good" than of the word "bad", it predicts "positive".
If it contains more of the word "bad" than of the word "good",
it predicts "negative". If the count is equal (note that this includes zero count), it cannot make a prediction.
'''

# Constants. Constants are important to avoid typo-related bugs, among other reasons.
# Use these constants as return values for the below function.

POS_REVIEW = "POSITIVE"
NEG_REVIEW = "NEGATIVE"
NONE = "NONE"
POS = 'good'
NEG = 'bad'


def predictSimplistic(counts):
    # This line retrieves the count for "good". If the word "good" is not found in "counts", it returns 0.
    pos_count = counts.get(POS, 0)
    # Write a similar statement to retrieve the count of "bad".
    # neg_count =

    # Write an if-elif-else block here, following the logic described in the function description.
    # Do not forget to return the prediction! You will be returning one of the constants declared above.
    # You may choose to store a prediction in a variable and then write the return statement outside
    # of the if-else block, or you can have three return statements within the if-else block.

    # You will modify the below return statement or move it into your if-else block when you write it.
    return NONE


'''The main function is the entry point of the program.
When debugging, if you want to start from the very beginning,
start here. NB: Put the breakpoint not on the "def" line but below it.
Do not modify this function; we already wrote it for you.
You need to modify the functions which it calls.
'''


def main(argv):
    # The file that you will read should be passed as the argument to the program.
    # From python's point of view, it is the element number 1 in the array called argv.
    # argv is a special variable name. We don't define it ourselves; python knows about it.
    filename = argv[1]  # Place the first breakpoint here, when starting.

    # Now, we will call a function called cleanFileContents on the filename we were passed.
    # NB: We could have called the function directly on argv[1]; that would have the same effect.
    clean_text = cleanFileContents(filename)

    # Now, we will count how many times each word occurs in the review.
    # We are passing the text of the review, cleaned from punctuation, to the function called countTokens.
    # We assign the output of the function to a new variable we call tokens_with_counts.
    tokens_with_counts = countTokens(clean_text)

    # Call the simplistic prediction function on the obtained counts.
    # Store the output of the function in a new variable called "prediction".
    prediction = predictSimplistic(tokens_with_counts)

    # Finally, let's print out what we predicted:
    print("The prediction for file {} is {}".format(filename, prediction))


# The below code is needed so that this file can be used as a module.
# If we want to call our program from outside this window, in other words.
if __name__ == "__main__":
    main(sys.argv)
