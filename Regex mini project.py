#Q) 1) generate random passwrod
# 2) check password strength
# 3) count character used in pswd
# 4) gives a strength score using math
# 5) saves the result in a file using os 

import random
import re
import os
from collections import Counter
import string

# 1. Generate random password
chars = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(chars) for _ in range(12))  # 12-character password

# 2. Check password strength
uppercase = bool(re.search(r"[A-Z]", password))
lowercase = bool(re.search(r"[a-z]", password))
digit = bool(re.search(r"[0-9]", password))
special = bool(re.search(r"[^A-Za-z0-9]", password))
length_ok = len(password) >= 8

# Strength calculation (1 point for each rule passed)
strength = sum([uppercase, lowercase, digit, special, length_ok])

# 3. Count characters used
char_count = {
    "uppercase": len(re.findall(r"[A-Z]", password)),
    "lowercase": len(re.findall(r"[a-z]", password)),
    "digits": len(re.findall(r"[0-9]", password)),
    "special": len(re.findall(r"[^A-Za-z0-9]", password))
}

# 4. Calculate strength score (percentage)
strength_score = (strength / 5) * 100

# 5. Save result to a file
if not os.path.exists("easy_reports"):
    os.mkdir("easy_reports")

file_path = os.path.join("easy_reports", "password_report.txt")
with open(file_path, "w") as file:
    file.write(f"Generated Password: {password}\n")
    file.write(f"Character Count: {char_count}\n")
    file.write(f"Strength Score: {strength_score}%\n")

# Print results
print("Password Generated:", password)
print("Character Count:", char_count)
print("Strength Score:", strength_score, "%")
