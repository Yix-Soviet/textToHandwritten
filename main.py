import pywhatkit
import os
import pause

text = str(input('Insert text: '))  # Input to insert the text to be converted.

pywhatkit.text_to_handwriting(text)  # Convert text

# Moves the result to the corresponding file folder and if it exists replaces it.
os.rename("./pywhatkit.png", "./img/result.png")

# Delay the process by 10 milliseconds si that the resulting file can be created.
pause.milliseconds(10)

os.remove("./pywhatkit_dbs.txt")  # Deletes the file that is created.
