def rotate(text, shift):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':  # Lowercase letters
            start = ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        elif 'A' <= char <= 'Z':  # Uppercase letters
            start = ord('A')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:  # Non-alphabetic characters (numbers, symbols, spaces) remain unchanged
            result += char
    return result
