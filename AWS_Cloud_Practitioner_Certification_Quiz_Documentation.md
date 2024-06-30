### AWS Cloud Practitioner Certification Quiz Documentation

#### Overview:
This Python program is designed to run a quiz testing knowledge about AWS (Amazon Web Services) Cloud Practitioner essentials. The quiz consists of a series of multiple-choice questions with options for each question.

#### Class:
- **Question:** 
  - This class represents a single question in the quiz.
  - **Attributes:**
    - `prompt`: Contains the actual question.
    - `options`: A list of options for the question.
    - `correct_option`: The correct option among A, B, C, or D.

#### Functions:
- **run_quiz(questions):**
  - This function takes a list of `Question` objects as input and runs the quiz.
  - **Parameters:**
    - `questions`: A list of `Question` objects.
  - The function iterates through each question, displays the question along with options, takes user input for the answer, and evaluates if the answer is correct.
  - The function keeps track of the score and outputs the final score along with any wrong answers.
  - At the end of the quiz, it provides feedback based on the score achieved.

#### Quiz Execution:
- The `run_quiz()` function is executed with the provided list of `Question` objects named `questions`.
- For each question, the program displays the question prompt, options, prompts the user to enter their choice (A, B, C, or D), and checks if the answer is correct or not.
- At the end of the quiz, the program displays the total score, lists any wrong answers, and provides a pass/fail message based on the score achieved.

#### Additional Notes:
- The quiz contains a total of 65 questions related to various AWS services and concepts.
- The program provides feedback based on the score obtained and informs the user whether they passed the AWS Cloud Practitioner Certification Quiz or not.

This documentation provides an overview of the AWS Cloud Practitioner Certification Quiz implemented in Python. Feel free to use this program to test your knowledge about AWS services.

