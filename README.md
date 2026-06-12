# week1
for purpose of submission regarding basic coding
# Personal Introduction Program

## Project Overview
The objective of this project is to build a foundational Python application that interacts with a user via the command line. The program prompts the user for personal information (name, age, hobby, and field of study), stores this data in variables, and utilizes string formatting to output a customized, friendly welcome message. 

## Setup Instructions
To run this program on your local machine, follow these step-by-step instructions:
1. Ensure Python 3.x is installed on your operating system. You can download it from [python.org](https://www.python.org/).
2. Clone this repository or download the project folder containing the files.
3. Open your terminal or command prompt.
4. Navigate to the directory where the files are saved.
5. Run the script using the following command:
   `python personal_intro.py`

## Code Structure
The project follows a simple and clean file hierarchy:
* `README.md`: Contains project documentation and assessment checklist items.
* `personal_intro.py`: The main Python executable script containing the core logic.
* `requirements.txt`: Lists dependencies (currently empty as only standard libraries are used).
* `screenshot.png`: Visual evidence of the program running successfully.

## Visual Documentation
Below is a screenshot demonstrating the functionality of the program running in the terminal:

![Program Execution Screenshot](screenshot.png)
*(Note for submission: Ensure you capture your terminal running the code and save it as screenshot.png in the same folder before uploading).*

## Technical Details
The script utilizes core Python fundamentals:
* **Algorithms/Architecture:** The program uses a simple linear procedural architecture, executing top-to-bottom within a `main()` function block.
* **Data Structures (Variables):** String data structures are used to capture and store user input in memory (`name`, `age`, `hobby`, `field_of_study`).
* **Input/Output Built-ins:** The `input()` function handles dynamic standard input from the console, while the `print()` function handles standard output.
* **String Formatting:** Python f-strings (`f"..."`) are utilized for efficient string interpolation, allowing variables to be injected directly into the printed welcome message.

## Testing Evidence
The application was validated using standard user inputs to ensure formatting and variables render correctly. 

**Test Case 1:**
* **Inputs:** * Name: Alex
  * Age: 21
  * Hobby: Coding
  * Study: Computer Science
* **Validation:** Program correctly output "🎉 Welcome Alex! 🎉" and "You are 21 years old and love Coding."

**Test Case 2:**
* **Inputs:** * Name: Rohan
  * Age: 20
  * Hobby: Developing dashboards
  * Study: Engineering at IIT Patna
* **Validation:** Program successfully captured multi-word strings and output exactly as formatted in the f-string block with no syntax errors.
