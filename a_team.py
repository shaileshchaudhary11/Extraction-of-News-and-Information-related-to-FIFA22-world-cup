import ply.lex as lex
### DEFINING TOKENS###

tokens = ('BEGINTABLE',
          'OPENTABLE', 'CLOSETABLE', 'OPENROW', 'CLOSEROW',
          'OPENHEADER', 'CLOSEHEADER', 'OPENHREF', 'CLOSEHREF',
          'CONTENT', 'OPENDATA', 'CLOSEDATA','GARBAGE')
t_ignore = '\t'


############### Tokenizer Rules################

def t_BEGINTABLE(t):
    '''<table\sclass="wikitable\ssortable \smw-collapsible\smw-collapsed">'''
    return t


def t_OPENTABLE(t):
    '''<tbody[^>]*>'''
    return t


def t_CLOSETABLE(t):
    '''</tbody[^>]*>'''
    return t


def t_OPENROW(t):
    '''<tr[^>]*>'''
    return t


def t_CLOSEROW(t):
    '''</tr[^>]*>'''
    return t


def t_OPENHEADER(t):
    '''<th[^>]*>'''
    return t


def t_CLOSEHEADER(t):
    '''</th[^>]*>'''
    return t


def t_OPENHREF(t):
    '''<a[^>]*>'''
    return t


def t_CLOSEHREF(t):
    '''</a[^>]*>'''
    return t


def t_OPENDATA(t):
    '''<td[^>]*>'''
    return t


def t_CLOSEDATA(t):
    '''</td[^>]*>'''
    return t


def t_CONTENT(t):
    '''[A-Za-z0-9,#:& ]+'''
    return t

def t_GARBAGE(t):
    r'<[^>]*>'

def t_error(t):
    t.lexer.skip(1)


#########################################################################################
# Fill with parsing rules
#########################################################################################
######### DRIVER FUNCTION#######
file_obj = open('teams.html', 'r', encoding="utf-8")
data = file_obj.read()
lexer = lex.lex()
lexer.input(data)
x = open("log.txt", "w", encoding="utf8")

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
    x.write(str(tok)+'\n')
# Fill the blank here for parser and lexer
file_obj.close()

######### YACC ########




# import ply.lex as lex
import ply.yacc as yacc
logfile = open("logs.txt","a")
#from a_tkTeam import tokens

def p_init(p):
    '''init : start'''
#staring rule
def p_begTable(p):
    '''start : BEGINTABLE OPENTABLE handleRow CLOSETABLE'''

#handling row
def p_handleRow(p):
    '''handleRow : OPENROW OPENHEADER CONTENT CLOSEHEADER OPENHEADER CONTENT CLOSEHEADER OPENHEADER CONTENT CLOSEHEADER CLOSEROW handleRow
    | OPENROW handleData CLOSEROW handleRow
    | '''

#handling data
def p_handleData(p):
    '''handleData : OPENDATA CONTENT OPENHREF CONTENT CLOSEHREF CLOSEDATA handleData
    | OPENDATA skip CLOSEDATA handleData
    | '''
    if len(p)==8:

        print(p[4])
        logfile.write(p[4]+'\n')


#handling unnecessary content by skip
def p_skip(p):
    '''skip : CONTENT skip
            | OPENHREF skip
            | CLOSEHREF skip
            | '''

def p_error(p):
    pass

parser = yacc.yacc()

file_obj = open('teams.html', 'r', encoding="utf-8")
data = file_obj.read()
parser.parse(data)