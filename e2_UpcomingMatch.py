

import ply.lex as lex
logfile = open("logs.txt","a",encoding="utf-8")

### DEFINING TOKENS###

tokens = ('BEGINTABLE',
          'OPENTABLE', 'CLOSETABLE', 'OPENROW', 'CLOSEROW',
          'OPENHEADER', 'CLOSEHEADER', 'OPENHREF', 'CLOSEHREF',
          'CONTENT', 'OPENDATA', 'CLOSEDATA','GARBAGE','OPENABBR','OB','CB','CLOSEABBR','OPENDIV','CLOSEDIV','ENDTABLE')
t_ignore = '\t'


############### Tokenizer Rules################

def t_BEGINTABLE(t):
    '''<span\sclass="mw-headline"\sid="2023">2023</span>'''
    return t
# def t_ENDTABLE(t):
#     '''<span\sclass="mw-headline"\sid="2023">2023</span>'''
#     return t

def t_OPENTABLE(t):
    '''<tbody[^>]*>'''
    return t


def t_CLOSETABLE(t):
    '''</tbody[^>]*>'''
    return t


# def t_OPENROW(t):
#     '''<tr[^>]*>'''
#     # return t


# def t_CLOSEROW(t):
#     '''</tr[^>]*>'''
#     # return t


# def t_OPENHEADER(t):
#     '''<th[^>]*>'''
#     # return t


# def t_CLOSEHEADER(t):
#     '''</th[^>]*>'''
#     # return t

def t_OPENDIV(t):
    '''<div[^>]*>'''
    return t

def t_CLOSEDIV(t):
    '''</div[^>]*>'''
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


# def t_OPENDATA(t):
#     '''<td[^>]*>'''
#     # return t


# def t_CLOSEDATA(t):
#     '''</td[^>]*>'''
#     # return t


def t_CONTENT(t):
    '''[A-Za-z0-9áéñÁíóúü,#.:\-&; ]+'''
    return t


# def t_OB(t):
#     r'\(.*?'

# def t_CB(t):
#     r'.*?\)'

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

######### YACC ###########

# import ply.lex as lex
import ply.yacc as yacc

#from e2_tkUpcomingMatch import tokens

my_List = []

def p_init(p):
    '''init : bskip BEGINTABLE handleDiv
            | bskip BEGINTABLE OPENHREF CONTENT CLOSEHREF handleDiv'''
# #staring rule
# def p_begTable(p):
#     '''start : bskip BEGINTABLE handleDiv ENDTABLE'''

def p_bskip(p):
    '''bskip : CONTENT bskip
             | OPENHREF bskip
             | CLOSEHREF bskip
             | OPENDIV bskip
             | CLOSEDIV bskip
             | OPENTABLE bskip
             | CLOSETABLE bskip
             | '''

#handling row
def p_handleDiv(p):
    '''handleDiv : OPENDIV handleData OPENTABLE skip CLOSETABLE CLOSEDIV handleDiv
                 | '''

#handling data
def p_handleData(p):
    '''handleData : OPENHREF CONTENT CLOSEHREF CONTENT CONTENT CONTENT OPENHREF CONTENT CLOSEHREF'''
    if len(p)>1:
        # print(p[2])
        # print(p[8])
        my_List.append(p[2])
        my_List.append(p[8])

        # print(p[2],"vs",p[8])
    

#handling unnecessary content by skip
def p_skip(p):
    '''skip : CONTENT skip
             | OPENHREF skip
             | CLOSEHREF skip
             | OPENDIV skip
             | CLOSEDIV skip
             | '''

def p_error(p):
    #print('Error:',p)
    pass

parser = yacc.yacc()

file_obj = open('squad_name.html', 'r', encoding="utf-8")
data = file_obj.read()
parser.parse(data)

#print(my_List)

# #printing last five matches played by england
first_10 = my_List[:10]

print("<---UPCOMING FIVE MATCHES --->")

# Iterate over the list in pairs using the zip function
for x, y in zip(first_10[::2], first_10[1::2]):
    print(x,"vs",y)
    logfile.write(x+"vs"+ y+'\n')


