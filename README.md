<h2 align="center"></h2>
<h1 align="center">PYTHON SIMPLE PROJECTS</h1>
<h2 align="left">INTRODUCTION</h2>
<h3 align="left">This repository provides a variety of simple Python projects that make extensive use of looping and conditional statements. These projects serve as practical examples to help beginners understand how these fundamental concepts are applied in real-world programming scenarios.</h3>
<h2 align="center"></h2>

<h2 align="center">PROJECTS</h2>
<h3 align="left"> Anagram Checker: </h3>
This project checks if two provided strings are anagrams of each other. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once. The program ignores spaces, punctuation, and capitalization.


Input Prompt: The program starts by prompting the user to enter two words, converting them to lowercase to ensure the comparison is case-insensitive.

Sort the Letters: The words are then sorted alphabetically. This means that if the two words are anagrams, their sorted versions will be identical.

Compare Sorted Versions: The program compares the sorted versions of the two words. If they match, the words are anagrams; otherwise, they are not.

Output the Result: The result is printed, indicating whether the words are anagrams or not.
<h2 align="center"></h2>


<h3 align="left"> Count The Number of Words In a Sentence: </h3>

This project counts the number of words in a given sentence. It also handles multiple spaces, punctuation, and special characters, providing an accurate word count.
1. Taking User Input
We start by taking input from the user. The input() function prompts the user to enter a passage and stores it in the variable a.

2. Initializing the Word Count
We initialize a counter variable count to zero. This variable will keep track of the number of words in the passage.


3. Iterating Through the Passage
We use a for loop to iterate through each character in the passage. The range(len(a)) generates a sequence of indices from 0 to the length of the passage minus one.


4. Identifying Word Boundaries
Within the loop, we check if the current character (a[i]) is a space (' ') and if the next character (a[i+1]) is not a space. This condition helps us identify the boundaries between words.

5. Counting Words
Each time we find a word boundary, we increment the count by one. Finally, we print the total number of words by adding one to the count (since the number of words is always one more than the number of spaces between them).
<h2 align="center"></h2>


<h3 align="left"> Evaluating The Password Strength: </h3>
A simple tool to evaluate the strength of a password based on its length, use of uppercase and lowercase letters, numbers, and special characters. The program provides feedback on how to improve the password strength.
<h2 align="center"></h2>

<h3 align="left"> Prime Number Checker: </h3>
Checking if a number is prime is a common problem in programming. A prime number is one that is greater than 1 and has no divisors other than 1 and itself.
Initial Check: We first check if the input number a is less than 2. If it is, we immediately know it’s not a prime number.
Square Root Optimization: We iterate from 2 up to the square root of a (int(a**0.5) + 1). If a is divisible by any number in this range, it’s not a prime number.
Early Termination: If we find any divisor, we set is_prime to False and break out of the loop early, saving unnecessary computations.
<h2 align="center"></h2>

<h3 align="left"> Simple Clock: </h3>
A basic digital clock application that displays the current time. It updates every second and provides a simple GUI for time display.
1. Importing the Time Module
The import time statement allows us to use Python's built-in time module, which provides various time-related functions. In this case, we use it to pause the program execution for a specific duration.

2. Initializing the Time Variables
We start by initializing three variables: h, m, and s, representing hours, minutes, and seconds, respectively. Initially, they are all set to zero.

3. Creating an Infinite Loop
The while True: statement creates an infinite loop, meaning the code inside the loop will run indefinitely. This is essential for a clock, which needs to update continuously.

4. Displaying the Time
Within the loop, we print the current values of h, m, and s to display the time.

5. Adding a One-Second Delay
To simulate the passing of time, we use time.sleep(1) to pause the program for one second before continuing to the next iteration of the loop. This creates a one-second interval between each update of the time variables.

6. Updating the Seconds
After the one-second delay, we increment the seconds (s) by one.



7. Handling the Overflow of Seconds and Minutes
To handle the overflow of seconds (when s reaches 60), we reset s to 0 and increment m (minutes) by one.

Similarly, when m reaches 60, we reset both m and s to 0 and increment h (hours) by one.

8. Resetting the Clock After 12 Hours
In this example, we assume a 12-hour clock format. Therefore, when h reaches 12, we reset h, m, and s to 0.
<h2 align="center"></h2>

<h3 align="left"> Ticket Booking: </h3>
A simple ticket booking system that allows users to book tickets, view available seats, and cancel bookings. It simulates a basic booking system with essential functionalities.
<h2 align="center"></h2>

<h3 align="left"> Calculator: </h3>
A basic calculator that performs simple arithmetic operations like addition, subtraction, multiplication, and division. It provides a simple command-line interface for user interaction.
<h2 align="center"></h2>

<h3 align="left"> Factorial: </h3>
This project calculates the factorial of a given number using both iterative and recursive approaches. The user inputs a number, and the program outputs its factorial.
<h2 align="center"></h2>

<h3 align="left"> Create Factorial: </h3>
Similar to the Factorial Calculator, this project provides additional functionalities and optimizations for calculating factorials, including memoization techniques.
<h2 align="center"></h2>

<h3 align="left"> Create Heart: </h3>
Python's Turtle graphics module provides a fun and interactive way to create visual patterns and designs. In this blog post, we'll walk through a Python script that uses Turtle graphics to draw a red heart shape on a black background.
Setting up the Turtle Screen and Turtle:

screen = turtle.Screen(): Initializes the Turtle Screen object.
screen.bgcolor("black"): Sets the background color of the screen to black.
heart = turtle.Turtle():Creates a Turtle object named heart for drawing.
Configuring the Heart Turtle:

heart.color("red"): Sets the pen color to red.
heart.fillcolor("red"): Sets the fill color to red (for filling the heart shape).
heart.pensize(3): Sets the pen size to 3 pixels.
heart.speed(5): Sets the drawing speed to 5 (medium speed).
Drawing the Heart Shape:

heart.begin_fill(): Begins the filling of the shape with the specified fill color (red).
Left Side of the Heart:
heart.left(140): Turns the turtle left by 140 degrees.
heart.forward(180): Moves the turtle forward by 180 units.
heart.circle(-90, 200): Draws the left arc of the heart shape using a circle with a radius of -90 (to draw clockwise) and an arc of 200 degrees.
Right Side of the Heart:
heart.setheading(60): Sets the turtle's heading to 60 degrees.
heart.circle(-90, 200): Draws the right arc of the heart shape.
heart.forward(180): Moves the turtle forward to complete the heart shape.
Finishing Up:

heart.end_fill(): Ends the filling of the heart shape, ensuring it is completely colored red.
heart.hideturtle(): Hides the turtle cursor.
turtle.done(): Keeps the Turtle graphics window open until closed by the user.
<h2 align="center"></h2>

<h3 align="left"> Age Calculator: </h3>
This project calculates the age of a person based on their birthdate. The user inputs their birthdate, and the program outputs their age in years, months, and days.
<h2 align="center"></h2>

<h3 align="left"> To Do Lists: </h3>
A simple to-do list application that allows users to add, view, and delete tasks. It provides a command-line interface for managing daily tasks and organizing work.
<h2 align="center"></h2>
