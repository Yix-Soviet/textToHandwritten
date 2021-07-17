import pywhatkit
import os
import pause

text = str(input('Insert text: ')) # 

pywhatkit.text_to_handwriting(f"{text}")

os.rename("./pywhatkit.png", "./img/result.png")
pause.milliseconds(10)
os.remove("./pywhatkit_dbs.txt")
