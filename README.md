# ADynamicLanguageEmphasizingReadability

## String Parsing

In this project, you are going to combine the use of String methods with Loops in order to break up a piece of text into parts and get some info on the text itself.

You will be given a **template** to fill out. This will have the ```main``` function already filled out and its invocation already written. **There is nothing to change in the main method**

You will have to complete the other function skelletons to finish the assignment.

For the following tasks, you will need to replace the "default" function bodies with the correct ones.

# Task 1:

Inside ```main```, You will be given a base text called ```base_text``` that will contain some generic piece of text in English.

The first task will be to prepare the text for analysis. To do this, you will fill out the function called ```pre_process``` so that:
  - it accepts a string input
  - if the input string is empty, it should return an empty list: ``` return list()```.
  - otherwise, it converts all the words to lowercase.
  - it removes all non-letter characters (numbers and symbols) to leave only words composed of letters. Tip: Check the ```isalpha``` string mehtod.
  - it creates the "pre-processed list" with all the words that remain
  - it returns the pre-processed list.

note: you can complete the steps in any order as long as it works.
  

## Task 2

Complete the function called ```word_stats``` that will get some stats from the text passed in as an argument. It will have to do the following:
  - it accepts a list of words (all in lowercase)
  - if the input list is empty it returns an empty list.
  - otherwise, it will create a ```stats_list``` that will be a list composed of the following parameters:
    - first value: \[integer\] number of words
    - second value: \[integer\] smallest word 
    - third value:  \[integer\] smallest word size
    - fourth value: \[integer\] largest word 
    - fifth value: \[integer\] largest word size
    - six value: \[integer\] average word size
  - the function will return the ```stats_list```

## Task 3
Complete the function called ```frequency``` that will obtain the number of appearances of an input string in the list. It will have to do the following:
  - accept two imputs: a list of words, and a search string
  - if either input is empty (and/or has a 0 length), return a ```-1```
  - otherwise, your program should return ```str_freq```: the number of times the input string is **present** inside the list as either a complete word or as part of a word in the list.
  - the function will return the ```str_freq```.


## Rubric:

  - Getting the right list: 20%
  - correct num words: 10%
  - correct min word: 10%
  - correct max word: 10%
  - correct mean word: 10%
  - correct frequency for word 'and': 10%
  - correct frequency for word 'is': 10%
  - correct frequency for word 'the': 10%
  - correct frequency for word 'in': 10%

Note that:
  - The code does not run: -100%
  - bad comments: -10%
