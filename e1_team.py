
import ply.lex as lex
logfile = open("logs.txt","a",encoding="utf-8")

### DEFINING TOKENS###

tokens = ('BEGINTABLE',
          'OPENTABLE', 'CLOSETABLE', 'OPENROW', 'CLOSEROW',
          'OPENHEADER', 'CLOSEHEADER', 'OPENHREF', 'CLOSEHREF',
          'CONTENT', 'OPENDATA', 'CLOSEDATA','GARBAGE','OPENABBR','OB','CB','CLOSEABBR')
t_ignore = '\t'

############### Tokenizer Rules################

def t_BEGINTABLE(t):
    '''<span\sclass="mw-headline"\sid="Current_squad">Current\ssquad</span>'''
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

def t_OPENABBR(t):
    '''<abbr[^>]*>'''

def t_CLOSEABBR(t):
    '''</abbr[^>]*>'''

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
    '''[A-Za-z0-9áéñÁíóúüïÉã,#:&\-  ]+'''
    return t

def t_OB(t):
    r'\(.*?'

def t_CB(t):
    r'.*?\)'

def t_GARBAGE(t):
    r'<[^>]*>'

def t_error(t):
    t.lexer.skip(1)


#########################################################################################
# Fill with parsing rules
#########################################################################################
######### DRIVER FUNCTION#######
file_obj = open("squad_name.html", 'r', encoding="utf-8")
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
    #x.close()
    
# Fill the blank here for parser and lexer
file_obj.close()


######### YACC

# import ply.lex as lex
import ply.yacc as yacc

#from e1_tkTeam import tokens

def p_init(p):
    '''init : start'''
#staring rule
def p_begTable(p):
    '''start : bskip BEGINTABLE skip OPENTABLE handleRow CLOSETABLE'''

def p_bskip(p):
    '''bskip : CONTENT bskip
             | OPENHREF bskip
             | CLOSEHREF bskip
             | OPENDATA bskip
             | CLOSEDATA bskip
             | OPENROW bskip
             | CLOSEROW bskip
             | OPENHEADER bskip
             | CLOSEHEADER bskip
             | OPENABBR bskip
             | CLOSEABBR bskip
             | OPENTABLE bskip
             | CLOSETABLE bskip
             | '''
#handling row
def p_handleRow(p):
    '''handleRow : OPENROW OPENHEADER CONTENT CLOSEHEADER OPENHEADER CONTENT CLOSEHEADER OPENHEADER CONTENT CLOSEHEADER OPENHEADER CONTENT skip CLOSEHEADER OPENHEADER CONTENT CLOSEHEADER OPENHEADER CONTENT CLOSEHEADER OPENHEADER CONTENT CLOSEHEADER CLOSEROW handleRow
    | OPENROW handleData CLOSEROW handleRow
    | '''

#handling data
def p_handleData(p):
    '''handleData : OPENDATA skip CLOSEDATA OPENDATA skip CLOSEDATA OPENHEADER OPENHREF CONTENT CLOSEHREF skip CLOSEHEADER handleData 
    | OPENDATA skip CLOSEDATA handleData
    | '''
    # print(p)
    if len(p)==14:
        print(p[9])
        logfile.write(p[9]+'\n')

#handling unnecessary content by skip
def p_skip(p):
    '''skip : CONTENT skip
            | OPENHREF skip
            | CLOSEHREF skip
            | '''

def p_error(p):
    #print('error:',p)
    pass

parser = yacc.yacc()

file_obj = open("squad_name.html", 'r', encoding="utf-8")
data = file_obj.read()
parser.parse(data)