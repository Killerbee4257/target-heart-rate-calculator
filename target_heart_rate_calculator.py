"""
Name: Nigel Wilkerson
Problem: Translate the algorithm described in the flowchart and pseudocode created for the
        Target Heart-Rate Calculator algorithm into a Python program.
Date: 22 October 2025
Version: 1.0
"""


 #This is where the user inputs their age
age = int(input("Enter your age: "))

#These are the calculations
maxHr = 220-age
modMin = maxHr * .50
modMax = maxHr * .70
vigMin = maxHr * .70
vigMax = maxHr * .85

# This is where the results are displayed
# f-strings format the output neatly and round values to one decimal place
print(f"\n Maximum Heart Rate: {maxHr} bpm")
print(f"moderate range: {modMin:.1f} - {modMax:.1f} bpm")
print(f"vigorous range: {vigMin:.1f} - {vigMax:.1f} bpm")