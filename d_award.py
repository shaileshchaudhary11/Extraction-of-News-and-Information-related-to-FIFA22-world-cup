
import ply.lex as lex
logfile = open("logs.txt","a",encoding="utf-8")
### DEFINING TOKENS###

tokens = ('BEGINTABLE',
          'OPENTABLE', 'CLOSETABLE', 'OPENROW', 'CLOSEROW',
          'OPENHEADER', 'CLOSEHEADER', 'OPENHREF', 'CLOSEHREF',
          'CONTENT', 'OPENDATA', 'CLOSEDATA','GARBAGE','OPENABBR','OB','CB','CLOSEABBR','OPENSPAN','CLOSESPAN')
t_ignore = '\t'

############### Tokenizer Rules################

def t_BEGINTABLE(t):
    '''<h2><span\sclass="mw-headline"\sid="Awards">Awards</span></h2>'''
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

def t_OPENSPAN(t):
    '''<span[^>]*>'''
    return t

def t_CLOSESPAN(t):
    '''</span[^>]*>'''
    return t


def t_CONTENT(t):
    '''[A-Za-z0-9áéñÁíćóúüïÉã,#:&\-  ]+'''
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
file_obj = open("d_award.html", 'r', encoding="utf-8")
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


############## YACC #########

# import ply.lex as lex
import ply.yacc as yacc

#from d_tkAward import tokens

my_List = []

def p_init(p):
    '''init : start'''
#staring rule
def p_begTable(p):
    '''start : BEGINTABLE skip OPENTABLE handleRow CLOSETABLE'''

#handling row
def p_handleRow(p):
    '''handleRow : OPENROW handleData CLOSEROW handleRow
                 | '''

#handling data
def p_handleData(p):
    '''handleData : OPENHEADER OPENHREF CONTENT CLOSEHREF CLOSEHEADER handleData
                  | OPENHEADER CONTENT CLOSEHEADER handleData
                  | OPENDATA OPENSPAN skip CLOSESPAN CONTENT OPENHREF CONTENT CLOSEHREF CLOSEDATA handleData
                  | OPENDATA skip CLOSEDATA handleData
                  | '''
    if len(p)==7:
        my_List.append(p[3])
    if len(p)==5:
        my_List.append(p[2])
    if len(p)==11:
        my_List.append(p[7])

#handling unnecessary content by skip
def p_skip(p):
    '''skip : CONTENT skip
            | OPENHREF skip
            | CLOSEHREF skip
            | '''

def p_error(p):
    print(p)
    pass

parser = yacc.yacc()

file_obj = open('d_award.html', 'r', encoding="utf-8")
data = file_obj.read()
parser.parse(data)

#print(my_List)

#Printing Player Name corresponding Award
print(my_List[0],"->",my_List[3],'\n')
logfile.write(my_List[0]+"->"+my_List[3]+'\n')
print(my_List[1],"->",my_List[4],'\n')
logfile.write(my_List[1]+"->"+my_List[4]+'\n')
print(my_List[2],"->",my_List[5],'\n')
logfile.write(my_List[2]+"->"+my_List[5]+'\n')
print(my_List[6],"->",my_List[9],'\n')
logfile.write(my_List[6]+"->"+my_List[9]+'\n')
print(my_List[7],"->",my_List[10],'\n')
logfile.write(my_List[7]+"->"+my_List[10]+'\n')
print(my_List[8],"->",my_List[11],'\n')
logfile.write(my_List[8]+"->"+my_List[11]+'\n')
print(my_List[15],"->",my_List[16],'\n')
logfile.write(my_List[15]+"->"+my_List[16]+'\n')
print(my_List[17],"->",my_List[18],'\n')
logfile.write(my_List[17]+"->"+my_List[18]+'\n')
print(my_List[19],"->","England")
logfile.write(my_List[19]+"->"+"England")
