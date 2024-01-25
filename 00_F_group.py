

import ply.lex as lex
### DEFINING TOKENS###

tokens = ('BEGINTABLE','MATCHDIV',
          'OPENTABLE', 'CLOSETABLE', 'OPENROW', 'CLOSEROW',
          'OPENHEADER', 'CLOSEHEADER', 'OPENHREF', 'CLOSEHREF',
          'CONTENT', 'OPENDATA', 'CLOSEDATA','GARBAGE','OPENABBR','OB','CB','CLOSEABBR','OPENLIST','TRASH','CLOSELIST')
t_ignore = '\t'


############### Tokenizer Rules################

def t_BEGINTABLE(t):
    '''<h3><span\sclass="mw-headline"\sid="Group_F">Group\sF</span></h3>'''
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
    return t

def t_CLOSEABBR(t):
    '''</abbr[^>]*>'''
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
    r'[A-Za-z0-9ñáãćéíøäæóōúńÁÉÜÚÑğÓÍïüšëčýÿû,$#§&.+\-:;@ \'")\(–]+'
    return t

def t_TRASH(t):
    r'<link.*?/>'

def t_OPENLIST(t):
    r'<li .*?>'
    return t

def t_CLOSELIST(t):
    '''</li[^>]*>'''
    return t

def t_MATCHDIV(t):
    '''<div\sitemscope=""\sitemtype="http&\#58;//schema.org/SportsEvent"\sclass="footballbox">'''
    return t
# def t_(t):
#     '''<span[^>]*>'''
#     return t

# def t_(t):
#     '''</span[^>]*>'''
#     return t

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
file_obj = open("Fifa_data.html", 'r', encoding="utf-8")
data = file_obj.read()
lexer = lex.lex()
lexer.input(data)
x = open("log.txt", "w", encoding="utf8")
# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    # print(tok)
    x.write(str(tok)+'\n')
    #x.close()
    
# Fill the blank here for parser and lexer
file_obj.close()


######## YACC ########

# import ply.lex as le
import ply.yacc as yacc

#from c_tkGroupStage import tokens

my_List=[]
list=[]
def p_init(p):
    '''init : start'''
#staring rule
def p_begTable(p):
    '''start : bskip BEGINTABLE skip OPENTABLE handleRow CLOSETABLE skip MATCHDIV handleMatch'''

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
             | OPENLIST bskip
             | CLOSELIST bskip
             | OPENTABLE bskip
             | CLOSETABLE bskip
             | '''

#handling row
def p_handleRow(p):
    '''handleRow : OPENROW OPENHEADER OPENABBR CONTENT CLOSEABBR CLOSEHEADER OPENHEADER CONTENT OPENLIST OPENHREF OPENABBR CONTENT CLOSEABBR CLOSEHREF CLOSELIST OPENLIST OPENHREF OPENABBR CONTENT CLOSEABBR CLOSEHREF CLOSELIST OPENLIST OPENHREF OPENABBR CONTENT CLOSEABBR CLOSEHREF CLOSELIST CLOSEHEADER OPENHEADER OPENABBR CONTENT CLOSEABBR CLOSEHEADER OPENHEADER OPENABBR CONTENT CLOSEABBR CLOSEHEADER OPENHEADER OPENABBR CONTENT CLOSEABBR CLOSEHEADER OPENHEADER OPENABBR CONTENT CLOSEABBR CLOSEHEADER OPENHEADER OPENABBR CONTENT CLOSEABBR CLOSEHEADER OPENHEADER OPENABBR CONTENT CLOSEABBR CLOSEHEADER OPENHEADER OPENABBR CONTENT CLOSEABBR CLOSEHEADER OPENHEADER OPENABBR CONTENT CLOSEABBR  CLOSEHEADER OPENHEADER CONTENT CLOSEHEADER CLOSEROW handleRow
    | OPENROW handleData CLOSEROW handleRow
    | '''

#handling data
def p_handleData(p):
    '''handleData : OPENDATA CONTENT CLOSEDATA handleData
    | OPENHEADER   CONTENT  OPENHREF CONTENT CLOSEHREF  CLOSEHEADER handleData
    | OPENHEADER   CONTENT  OPENHREF CONTENT CLOSEHREF  CONTENT  CONTENT  CLOSEHEADER handleData
    | OPENDATA CONTENT OPENHREF CONTENT CLOSEHREF CLOSEDATA handleData
    | OPENDATA CLOSEDATA handleData
    | '''
    if len(p)==5:
        #print(p[2])
        my_List.append(p[2])
    if len(p)==8:
        #print(p[2],p[4])
        my_List.append(p[4])
    if len(p)==10:
        #print(p[4])
        my_List.append(p[4])
    if len(p)==10:
        #print(p[2],p[4],p[6],p[7])
        my_List.append(p[7])

def p_tableData(p):
    '''tableData : OPENROW OPENHEADER OPENHREF CONTENT CLOSEHREF CONTENT CLOSEHEADER OPENHEADER OPENHREF CONTENT CLOSEHREF CLOSEHEADER OPENHEADER CONTENT OPENHREF CONTENT CLOSEHREF CLOSEHEADER CLOSEROW OPENROW OPENDATA handleList CLOSEDATA OPENDATA OPENHREF CONTENT CLOSEHREF CLOSEDATA OPENDATA handleList CLOSEDATA CLOSEROW handleStadium
                | '''

    if len(p)>2:
        list.append(p[4])
        list.append(p[10])
        list.append(p[16])

        

def p_handleList(p):
    '''handleList : skip OPENLIST OPENHREF CONTENT CLOSEHREF skip CLOSELIST handleList
                  | '''
    if len(p)==9:
        list.append(p[4])

def p_handleStadium(p):
    '''handleStadium : OPENHREF CONTENT CLOSEHREF CONTENT OPENHREF CONTENT CLOSEHREF CONTENT CONTENT OPENHREF CONTENT CLOSEHREF skip
                     | '''
    if len(p)>2:
        list.append(p[2])
        list.append(p[4])
        list.append(p[6])
        list.append(p[8])
        list.append(p[9])
        list.append(p[11])



def p_handleMatch(p):
    '''handleMatch : skip OPENTABLE tableData CLOSETABLE handleStadium handleMatch
                   | MATCHDIV skip OPENTABLE tableData CLOSETABLE handleStadium handleMatch
                   | '''


#handling unnecessary content by skip
def p_skip(p):
    '''skip : CONTENT skip
            | OPENHREF skip
            | CLOSEHREF skip
            | OPENABBR skip
            | CLOSEABBR skip
            | '''

def p_error(p):
    # print("ERROR :",p)
    pass

parser = yacc.yacc()

file_obj = open('Fifa_data.html', 'r', encoding="utf-8")
data = file_obj.read()
parser.parse(data)
# print(list)
# printing my_List

teams = [my_List[9], my_List[19], my_List[29],my_List[39]]
goalsA = [my_List[3],my_List[13],my_List[23],my_List[33]]
goalsF = [my_List[4],my_List[14],my_List[24],my_List[34]]


print("Enter 'knock',to see the team that get knockout:")

print("Enter 'group',to see the TEAM,GA,GF that get knockout:")

print("Enter 'details' to see the match details of particular team in that group:")

choice=input("Enter your choice:")
logfile = open("logs.txt","a")
if choice == "knock":
    print("Teams advanced to knockout stage: ",teams[0],teams[1])
    logfile.write("Teams advanced to knockout stage:\t "+teams[0]+teams[1]+'\n')

elif choice == 'group': 
    print("Goals forwarded and conceded:")
    logfile.write("Goals forwarded and conceded:")
    for i in range(len(teams)):
        print(teams[i] + " " + goalsF[i] +" "+goalsA[i])
        logfile.write(teams[i] + " " + goalsF[i] +" "+goalsA[i]+'\n')


matches = [list[0]+list[1]+list[2],list[10]+list[11]+list[12],list[21]+list[22]+list[23],list[34]+list[35]+list[36],list[43]+list[44]+list[45],list[55]+list[56]+list[57]]
players = ["",list[9],list[19]+list[20],list[30]+list[31]+list[32]+list[33],"",list[52]+list[53]+list[54]]
details = [list[3]+list[4]+list[5]+list[6]+list[7]+list[8],list[13]+list[14]+list[15]+list[16]+list[17]+list[18],list[24]+list[25]+list[26]+list[27]+list[28]+list[29],list[37]+list[38]+list[39]+list[40]+list[41]+list[42],list[46]+list[47]+list[48]+list[49]+list[50]+list[51],list[58]+list[59]+list[60]+list[61]+list[62]+list[63]]

# ['Morocco', '0–0', 'Croatia', 'Al Bayt Stadium', ', ', 'Al Khor', 'Attendance: 59,407', 'Referee: ', 'Fernando Rapallini',||8

#  'Batshuayi', 'Belgium', '1–0', 'Canada', 'Ahmad bin Ali Stadium', ', ', 'Al Rayyan', 'Attendance: 40,432', 'Referee: ', 'Janny Sikazwe',||18

#  'Aboukhlal', 'Saïss', 'Belgium', '0–2', 'Morocco', 'Al Thumama Stadium', ', ', 'Doha', 'Attendance: 43,738', 'Referee: ', 'César Arturo Ramos',||29

#  'Majer', 'Livaja', 'Kramarić', 'Davies', 'Croatia', '4–1', 'Canada', 'Khalifa International Stadium', ', ', 'Al Rayyan', 'Attendance: 44,374', 'Referee: ', 'Andrés Matonte',||42

#  'Croatia', '0–0', 'Belgium', 'Ahmad bin Ali Stadium', ', ', 'Al Rayyan', 'Attendance: 43,984', 'Referee: ', 'Anthony Taylor',||51
 
# 'Aguerd', 'En-Nesyri', 'Ziyech', 'Canada', '1–2', 'Morocco', 'Al Thumama Stadium', ', ', 'Doha', 'Attendance: 43,102', 'Referee: ', 'Raphael Claus']

if choice == "details":
    x=int(input("Enter the match number whose match detail you want to see from 1 to 6:"))
    logfile.write("Match details:\t")
    print(matches[x-1] +"  " + players[x-1]+"  "+details[x-1])
    logfile.write(matches[x-1] +"  " + players[x-1]+"  "+details[x-1]+'\n')


# print(list)