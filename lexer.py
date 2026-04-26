import re

# Define the 'Vocabulary' of your language
TOKEN_TYPES = [
    ('NUMBER',   r'\d+'),          # Integer
    ('PLUS',     r'\+'),           # Addition
    ('MINUS',    r'-'),            # Subtraction
    ('MUL',      r'\*'),           # Multiplication
    ('DIV',      r'/'),            # Division
    ('LPAREN',   r'\('),           # (
    ('RPAREN',   r'\)'),           # )
    ('IDENT',    r'[a-zA-Z_]\w*'), # Variable names
    ('ASSIGN',   r'='),            # Assignment
    ('SKIP',     r'[ \t]+'),       # Spaces and tabs
    ('NEWLINE',  r'\n'),           # Line breaks
    ('SEMICOLON',r';'),            # Semicolon
    ('LET',      r'let'),          # let 
    ('MISMATCH', r'.'),            # Anything else (Error)
]

def lex(code):
    tokens = []
    # Combine all regex patterns into one master pattern
    master_pattern = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_TYPES)
    
    for match in re.finditer(master_pattern, code):
        kind = match.lastgroup
        value = match.group()
        
        if kind == 'NUMBER':
            value = int(value)
        elif kind == 'SKIP' or kind == 'NEWLINE':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character: {value}')
            
        tokens.append((kind, value))
    return tokens

# Let's test it!
code = "let x = 10 + 5 * 2"
print(f"Code: {code}")
print(f"Tokens: {lex(code)}")