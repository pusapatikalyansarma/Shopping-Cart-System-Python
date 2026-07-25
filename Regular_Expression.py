import re

text = "My phone number is 9876543210"

pattern = r"[0-9]{10}"

result = re.search(pattern, text)

if result:
    print("Valid phone number found")
    print(result.group())
else:
    print("Phone number not found")