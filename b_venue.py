
import ply.lex as lex
import ply.yacc as yacc
logfile = open("logs.txt","a")
###DEFINING TOKENS###

tokens = ('BEGINTABLE', 
'OPENTABLE', 'CLOSETABLE', 'OPENROW', 'CLOSEROW',
'OPENHEADER', 'CLOSEHEADER', 'OPENHREF', 'CLOSEHREF',
'CONTENT', 'OPENDATA', 'CLOSEDATA' ,'OPENSPAN',
'CLOSESPAN', 'OPENDIV', 'CLOSEDIV', 'OPENSTYLE', 'CLOSESTYLE','GARBAGE')
t_ignore = '\t'


###############Tokenizer Rules################

def t_BEGINTABLE(t):

    '''<h3><span\sclass="mw-headline"\sid="Stadiums">Stadiums</span></h3>'''
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
    '''[A-Za-z0-9, ]+'''
    return t

def t_OPENDIV(t):
    '''<div[^>]*>'''

def t_CLOSEDIV(t):
    '''</div[^>]*>'''

def t_OPENSTYLE(t):
    '''<style[^>]*>'''

def t_CLOSESTYLE(t):
    '''</style[^>]*>'''

def t_OPENSPAN(t):
    '''<span[^>]*>'''

def t_CLOSESPAN(t):
    '''</span[^>]*>'''

def t_GARBAGE(t):
    r'<[^>]*>'

def t_error(t):
    t.lexer.skip(1)


#########################################################################################
#Fill with parsing rules
#########################################################################################
#########DRIVER FUNCTION#######
file_obj= open('venue.html','r',encoding="utf-8")
data=file_obj.read()
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
    #########Fill the blank here for parser and lexer
file_obj.close()

########### YACC ########

# import ply.lex as lex
import ply.yacc as yacc

#from b_tkVenue import tokens

def p_start(p):
    '''start : table'''
    #p[0] = p[1]

# def p_name(p):
#     '''name : CONTENT
#             | CONTENT name'''
#     if len(p) == 3:
#         p[0] = p[1]+ ' '+ p[2]
#     else:
#         p[0] = p[1]

def p_skiptag(p):
    '''skiptag : CONTENT skiptag
                | OPENHREF skiptag
                | CLOSEHREF skiptag
                | '''

def p_handleData(p):
    '''handledata : OPENDATA OPENHREF CONTENT CLOSEHREF CLOSEDATA OPENDATA CONTENT skiptag CLOSEDATA handledata
                  |'''
    if len(p)==11:
        print(p[3],p[7])
        logfile.write(p[3]+","+p[7]+'\n')
    

def p_handleRow(p):
    '''handlerow : OPENROW OPENHEADER skiptag CLOSEHEADER OPENHEADER skiptag CLOSEHEADER OPENHEADER skiptag CLOSEHEADER CLOSEROW handlerow
                | OPENROW OPENHEADER OPENHREF CONTENT CLOSEHREF CLOSEHEADER handledata CLOSEROW handlerow
                | OPENROW handledata CLOSEROW handlerow
                |'''

def p_table(p):
    '''table : BEGINTABLE skiptag OPENTABLE handlerow'''

# def p_empty(p):
#     '''empty :'''
#     pass

# def p_content(p):
#     '''content : CONTENT
#                 | empty'''
#     p[0] = p[1]

def p_error(p):
    pass

parser = yacc.yacc()

# while True:
#     try:
#         s = raw_input('calc > ')
#     except EOFError:
#         break
#     if not s: continue
#     result = parser.parse(s)
#     print(result)

file_obj= open('venue.html','r',encoding="utf-8")
data=file_obj.read()
res=parser.parse(data)

print(res)