# 📘 Quiz Application

A simple command-line quiz application built with Python to practice Object-Oriented Programming (OOP) and file handling.

The application reads questions from a file, displays them to the user, accepts answers, and calculates the final score.

# 🚀 Features

## OOP Design

Question class represents a single quiz question.

Quizz class manages questions, scoring, and game flow.

## File Handling

Questions are loaded from an external text file.

## Interactive CLI

Displays questions with multiple choices.

Takes user input for answers.

Shows whether the answer is correct or wrong.

## Score Tracking

Keeps count of correct answers.

Displays the final score at the end of the quiz.

# 📂 Project Structure
Quiz_Application/
│── quiz.py          # Main application
│── questions.txt    # File containing questions, options, and answers
│── README.md        # Documentation

# 📝 File Format for questions.txt

Each line should follow this format:

Question,Option1,Option2,Option3,Option4,CorrectOptionIndex


Question: The quiz question.

Option1..4: Multiple choice options.

CorrectOptionIndex: The correct option number (1-based index).

# ✅ Example
Which language is used for web development?,Python,HTML,C++,Java,2
What is 5 + 3?,5,8,9,10,2
Which planet is known as the Red Planet?,Earth,Mars,Venus,Jupiter,2

# ▶️ Usage
##  Run the Program
python quiz.py

# 💡 Example Run
Welcome to Quiz Application

Q1: Which language is used for web development?
1. Python
2. HTML
3. C++
4. Java
Your choice (1-4): 2
Correct!

Q2: What is 5 + 3?
1. 5
2. 8
3. 9
4. 10
Your choice (1-4): 1
Wrong

Final score: 1/2