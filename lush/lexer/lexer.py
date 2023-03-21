import sys

import ply.lex as lex


tokens = (
    'COMMENT_BLOCK',
    'COMMENT_LINE',
    'ID',
    'STRING',
    'PASS',
    'INTEGER',
    'NUMBER',
    'DASH',
    'PLUS',
    'SLASH',
    'ASTERISK',
    'EXTRACT',
    'EXCLAMATION_MARK',
    'EQUALS',
    'LESS',
    'GREATER',
    'LESS_EQ',
    'GREATER_EQ',
    'STICK',
    'AMPERSAND',
    'NOT_EQUALS',
    'OPENING_CURLY_BRACKET',
    'CLOSING_CURLY_BRACKET',
    'OPENING_PARENTHESIS',
    'CLOSING_PARENTHESIS',
    'COMMA',
    'EXPRESSION_ENDS',
)

t_PASS = r':'
t_DASH = r'-'
t_PLUS = r'\+'
t_SLASH = r'\/'
t_ASTERISK = r'\*'
t_EXTRACT = r'\->'
t_EXCLAMATION_MARK = r'!'
t_EQUALS = r'\='
t_LESS = r'<'
t_GREATER = r'>'
t_LESS_EQ = r'<='
t_GREATER_EQ = r'>='
t_STICK = r'\|'
t_AMPERSAND = r'\&'
t_NOT_EQUALS = r'!='
t_OPENING_CURLY_BRACKET = r'{'
t_CLOSING_CURLY_BRACKET = r'}'
t_OPENING_PARENTHESIS = r'\('
t_CLOSING_PARENTHESIS = r'\)'
t_COMMA = r'\,'
t_EXPRESSION_ENDS = r'\n'

t_ignore = ' \t'


def t_INTEGER(t):
    r'\d+'
    t.integer_value = int(t.value)
    return t


def t_COMMENT_BLOCK(t):
    r'\+-+\+$(.*)^\+-+\+'
    t.comment_text = t.lexmatch.group(1)
    return t


def t_COMMENT_LINE(t):
    r'=== (.*)'
    t.comment_text = t.lexmatch.group(1)
    return t


def t_ID(t):
    r'[A-Z][A-Za-z0-9]*(\s+[A-Za-z0-9]+)*'
    t.id = t.value
    return t


def t_NUMBER(t):
    r'[-\\+]?\d+(.\d+)?'
    t.number_value = float(t.value)
    return t


def t_STRING(t):
    r'(\'[^\\](.*)\')|("[^\\](.*)")'
    t.value = t.lexmatch.group(1)


def t_error(t):
    print('Illegal character has been found.')
    sys.exit(0)


if __name__ == '__main__':
    lexer = lex.lex()

    lexer.input("""
    +--------------------------------------------+
     This is an example program of Lush language.
     ---
     It contains all the tokens can any Lush
     program have. Enjoy lexing!
    +--------------------------------------------+


    Import: Terminal
    Unpack: Terminal

    === A single line comment
    ===

    Name: 'Anatoly'     === The name of the user
    Age: 21             === The user age
    Money: 7700.0       === The user money
    Is male: True       === Is user a male?


    Location: '683013 Ryabinovskaya st. 3-15, Petropavlovsk-Kamchatsky, Russia'
    Greeting message: "Hello, I am {Name}!\n Glad to see you here!"


    === Function definition:
    One arg with return: (Name: Text): Nothing {
        Terminal -> Write: Name
    }

    Two args with return: (Name: Text, Age: Int): Text {
        Return: '#Name# is #Age# y.o.'
    }

    Three args without return: (A: Text, B: Boolean, C: Number) {
        If: A = 'Hello world' & B | C = 17 {
            Result: 'Yes'
        }

        Else: {
            Result: 'No'
        }
    }

    === Math:
    A: 1.0
    B: 6.0
    C: -17.0
    Pi: 3.14159

    Terminal -> Write: A + B
    Terminal -> Write: A - B
    Terminal -> Write: A * B
    Terminal -> Write: A / B

    Terminal -> Write: A + B - С
    Terminal -> Write: A * B / С

    Terminal -> Write: A + (B + С)
    Terminal -> Write: Sqrt: (Squared: Sin: A + Squared: Cos: B)

    Terminal -> Write: A + B * C / A + (A + (B * C) * Sin: B / A) + (A + 5.0 - 3 * 1 / C)


    === Comparison
    If: A >= 0 & B <= 0 | A < 0 & C > 15 | (A != B & C > 50.0) {
        Terminal -> Write: 'Gosh, interesting...'
    }


    === Booleans
    A1: True
    A2: True
    A3: False

    If: A1 | A2 | A3 & A1 | (A3 & A2 | (A3 = A2) & A1) | A1 & A3 {
        App -> Close!
    }
    """)

    while True:
        token = lexer.token()

        if not token:
            break

        print(token)