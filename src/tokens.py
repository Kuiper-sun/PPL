# Define token types
TOKEN_TYPES = {
    'KEYWORD': 'Keyword',
    'IDENTIFIER': 'Identifier',
    'NUMBER': 'Number',
    'OPERATOR': 'Operator',
    'DELIMITER': 'Delimiter',
    'STRING': 'String',
    'COMMENT': 'Comment'
}

# Define specific keywords, operators, delimiters, etc.
KEYWORDS = {'if', 'else', 'while', 'return', 'for', 'break', 'continue'}
OPERATORS = {'+', '-', '*', '/', '=', '==', '!=', '>', '<', '>=', '<='}
DELIMITERS = {'(', ')', '{', '}', ';', ',', '.', ':', '->'}

# Token class to represent individual tokens
class Token:
    def __init__(self, type_, value, line, column):
        self.type = type_
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        return f"Token({self.type!r}, {self.value!r}, {self.line}, {self.column})"

    def __str__(self):
        return f"{self.type}: {self.value} (Line: {self.line}, Col: {self.column})"
