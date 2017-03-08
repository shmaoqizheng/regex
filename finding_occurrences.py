import re
book = open("")
text = book.read()

regex = r"[^\w]wife[^\w]"
matches = text.findall(regex, text)
print len(matches)

text.replace(regex, "unicorn")
