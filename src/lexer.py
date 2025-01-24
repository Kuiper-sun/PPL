import re
from src.tokens import Token, TOKEN_TYPES, KEYWORDS, OPERATORS, DELIMITERS

class Lexer:
    def __init__(self, code):
        # Normalize the input code string
        if isinstance(code, bytes):
            code = code.decode('utf-8')

        # Replace problematic encoding sequences with proper characters
        self.code = code.replace('â€“', '–').replace('â€"', '-')  # Fix problematic characters
        self.tokens = []
        self.current_line = 1
        self.current_column = 1

    def tokenize(self):
        i = 0
        while i < len(self.code):
            char = self.code[i]

            # Skip whitespace
            if char.isspace():
                if char == '\n':
                    self.current_line += 1
                    self.current_column = 1
                else:
                    self.current_column += 1
                i += 1
                continue

            # Handle comments
            if i + 1 < len(self.code) and self.code[i:i+2] == '#/':
                i += 2
                self.current_column += 2
                
                while i < len(self.code):
                    if i + 1 < len(self.code) and self.code[i:i+2] == '/#':
                        i += 2
                        self.current_column += 2
                        break
                    
                    if self.code[i] == '\n':
                        self.current_line += 1
                        self.current_column = 1
                        i += 1
                    else:
                        self.current_column += 1
                        i += 1
                continue

            # Match string literals
            if char == '"':
                start = i
                i += 1
                self.current_column += 1
                while i < len(self.code) and self.code[i] != '"':
                    if self.code[i] == '\n':
                        self.current_line += 1
                        self.current_column = 1
                    else:
                        self.current_column += 1
                    i += 1
                if i < len(self.code):
                    i += 1
                    self.current_column += 1
                value = self.code[start:i]
                # Replace problematic minus sign in strings
                value = value.replace('â€“', '–')  # Fix the problematic dash in strings
                self.tokens.append(Token(TOKEN_TYPES['STRING'], value, self.current_line, self.current_column - len(value)))
                continue

            # Match numbers (including negative numbers)
            if char == '-' or char.isdigit():
                start = i
                if char == '-':
                    i += 1
                while i < len(self.code) and self.code[i].isdigit():
                    i += 1
                value = self.code[start:i]
                self.tokens.append(Token(TOKEN_TYPES['NUMBER'], value, self.current_line, self.current_column))
                self.current_column += i - start
                continue

            # Match keywords and identifiers
            if char.isalpha():
                start = i
                while i < len(self.code) and (self.code[i].isalnum() or self.code[i] == '_'):
                    i += 1
                value = self.code[start:i]
                token_type = TOKEN_TYPES['KEYWORD'] if value in KEYWORDS else TOKEN_TYPES['IDENTIFIER']
                
                if value in ['input', 'print']:
                    token_type = TOKEN_TYPES['IDENTIFIER']
                
                self.tokens.append(Token(token_type, value, self.current_line, self.current_column))
                self.current_column += i - start
                continue

            # Match operators
            if char in OPERATORS:
                # For operators, just use the standard minus
                op_value = char
                if char == 'â€"':
                    op_value = '-'
                self.tokens.append(Token(TOKEN_TYPES['OPERATOR'], op_value, self.current_line, self.current_column))
                self.current_column += 1
                i += 1
                continue

            # Match delimiters
            if char in DELIMITERS:
                self.tokens.append(Token(TOKEN_TYPES['DELIMITER'], char, self.current_line, self.current_column))
                self.current_column += 1
                i += 1
                continue

            # Unrecognized character
            raise ValueError(f"Unrecognized character '{char}' at line {self.current_line}, column {self.current_column}")

        return self.tokens
