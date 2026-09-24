text = " The color is pink "
print(text.upper())  # Output: THE COLOR IS PINK
print(text.lower())  # Output: the color is pink 
print(text.strip())  # Output: The color is pink
print(text.replace("pink", "blue"))  # Output: The color is blue
print(text.split())  # Output: ['The', 'color', 'is', 'pink']
print(text.find("color"))  # Output: 5
print(text.startswith(" The"))  # Output: True
print(text.endswith("pink "))  # Output: True
print(text.count("is"))  # Output: 1
print(text.isalpha())  # Output: False (because of spaces)
print(text.isdigit())  # Output: False
print(text.isalnum())  # Output: False (because of spaces)
print(text.title())  # Output: The Color Is Pink
print(text.capitalize())  # Output: The color is pink
print(text.center(30, "*"))  # Output: ******** The color is pink ********
print(text.lstrip())  # Output: The color is pink 
print(text.rstrip())  # Output:  The color is pink
print(text.swapcase())  # Output: tHE COLOR IS PINK
print(text.encode())  # Output: b' The color is pink '
print(text.isprintable())  # Output: True
print(text.isascii())  # Output: True
print(text.partition("color"))  # Output: (' The ', 'color', ' is pink ')
print(text.rpartition("is"))  # Output: (' The color ', 'is', ' pink ')
print(text.zfill(30))  # Output: 000000000000000 The color is pink
print(text.expandtabs(4))  # Output:  The color is pink      