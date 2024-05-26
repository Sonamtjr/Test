def reverse_string(s):
    """
    Recursive function to reverse a given string.
    
    Parameters:
    s (str): The string to be reversed.
    
    Returns:
    str: The reversed string.
    """
    # Base case: if the string is empty or contains only one character
    if len(s) <= 1:
        return s
    else:
        # Recursive case: reverse the remaining string and append the first character to the end
        return reverse_string(s[1:]) + s[0]

# Test cases
print(reverse_string("hello"))  # Should return "olleh"
print(reverse_string("python")) # Should return "nohtyp"
print(reverse_string(""))       # Should return ""
