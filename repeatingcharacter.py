def find_first_repeating_character(s):
    """
    Function to find the first repeating character in a string and print its memory address.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    char: The first repeating character or None if no repeating character is found.
    """
    # Dictionary to store the count of each character
    char_count = {}
    
    for char in s:
        if char in char_count:
            # Print the character and its memory address
            print(f"First repeating character: {char}")
            print(f"Memory address: {id(char)}")
            return char
        else:
            char_count[char] = 1
            
    # If no repeating character is found, return None
    return None

# Test cases
print(find_first_repeating_character("hello"))  # Should return 'l' and its memory address
print(find_first_repeating_character("python")) # Should return None
print(find_first_repeating_character("swiss"))  # Should return 's' and its memory address
