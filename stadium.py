# import ply.lex as lex
import ply.yacc as yacc

from tk import tokens

def p_start(p):
    '''start : table'''
    p[0] = p[1]

def p_name(p):
    '''name : CONTENT
            | CONTENT name'''
    if len(p) == 3:
        p[0] = p[1]+ ' '+ p[2]
    else:
        p[0] = p[1]

def p_skiptag(p):
    '''skiptag : CONTENT skiptag
                | OPENHREF skiptag
                | CLOSEHREF skiptag
                |'''

def p_handleData(p):
    '''handledata : OPENDATA OPENHREF CONTENT CLOSEHREF CLOSEDATA handledata
                  | OPENDATA skiptag CLOSEDATA handledata
                  |'''
    if len(p)==7:
        print(p[3])

def p_handleRow(p):
    '''handlerow : OPENROW OPENHEADER skiptag CLOSEHEADER OPENHEADER skiptag CLOSEHEADER OPENHEADER skiptag CLOSEHEADER CLOSEROW handlerow
                | OPENROW OPENHEADER OPENHREF CONTENT CLOSEHREF CLOSEHEADER handledata CLOSEROW handlerow
                | OPENROW handledata CLOSEROW handlerow
                |'''

def p_table(p):
    '''table : BEGINTABLE skiptag OPENTABLE handlerow'''

def p_empty(p):
    '''empty :'''
    pass

def p_content(p):
    '''content : CONTENT
                | empty'''
    p[0] = p[1]

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

file_obj= open('Fifa_data.html','r',encoding="utf-8")
data=file_obj.read()
res=parser.parse(data)

print(res)