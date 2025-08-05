def is_pangram(statement):
    required_letters = set("abcdefghijklmnopqrstuvwxyz")

   
    statement_letters = set(statement.lower())
    return required_letters <= statement_letters
