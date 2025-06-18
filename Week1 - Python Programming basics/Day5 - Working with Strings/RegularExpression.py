import re

# Findall digits in a String
phone = "Contact me at 123-456-7890"
digits = re.findall(r"\d+",phone)
print(digits)

# Substitute the string
updated_phone = re.sub(r"\d","X",phone)
print(updated_phone)

# Search the string
search_me = re.search(r"\d", phone)
print(search_me)