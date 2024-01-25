

import ply.lex as lex
logfile = open("logs.txt","a")
### DEFINING TOKENS###


tokens = ('BEGINROUND','MATCHDIV',
          'OPENTABLE', 'CLOSETABLE', 'OPENROW', 'CLOSEROW',
          'OPENHEADER', 'CLOSEHEADER', 'OPENHREF', 'CLOSEHREF',
          'CONTENT', 'OPENDATA', 'CLOSEDATA','GARBAGE','OPENABBR','OB','CB','CLOSEABBR','OPENLIST','TRASH','CLOSELIST')
t_ignore = '\t'


############### Tokenizer Rules################

def t_BEGINROUND(t):
    '''<span\sclass="mw-headline"\sid="Round_of_16">Round\sof\s16</span>'''
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
    '''start : bskip BEGINROUND skip MATCHDIV handleMatch'''

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
# def p_handleRow(p):
#     '''handleRow : OPENROW OPENHEADER OPENABBR CONTENT CLOSEABBR CLOSEHEADER OPENHEADER CONTENT OPENLIST OPENHREF OPENABBR CONTENT CLOSEABBR CLOSEHREF CLOSELIST OPENLIST OPENHREF OPENABBR CONTENT CLOSEABBR CLOSEHREF CLOSELIST OPENLIST OPENHREF OPENABBR CONTENT CLOSEABBR CLOSEHREF CLOSELIST CLOSEHEADER OPENHEADER OPENABBR CONTENT CLOSEABBR CLOSEHEADER OPENHEADER OPENABBR CONTENT CLOSEABBR CLOSEHEADER OPENHEADER OPENABBR CONTENT CLOSEABBR CLOSEHEADER OPENHEADER OPENABBR CONTENT CLOSEABBR CLOSEHEADER OPENHEADER OPENABBR CONTENT CLOSEABBR CLOSEHEADER OPENHEADER OPENABBR CONTENT CLOSEABBR CLOSEHEADER OPENHEADER OPENABBR CONTENT CLOSEABBR CLOSEHEADER OPENHEADER OPENABBR CONTENT CLOSEABBR  CLOSEHEADER OPENHEADER CONTENT CLOSEHEADER CLOSEROW handleRow
#     | OPENROW handleData CLOSEROW handleRow
#     | '''

#handling data
# def p_handleData(p):
#     '''handleData : OPENDATA CONTENT CLOSEDATA handleData
#     | OPENHEADER   CONTENT  OPENHREF CONTENT CLOSEHREF  CLOSEHEADER handleData
#     | OPENHEADER   CONTENT  OPENHREF CONTENT CLOSEHREF  CONTENT  CONTENT  CLOSEHEADER handleData
#     | OPENDATA CONTENT OPENHREF CONTENT CLOSEHREF CLOSEDATA handleData
#     | OPENDATA CLOSEDATA handleData
#     | '''
#     if len(p)==5:
#         print(p[2])
#         my_List.append(p[2])
#     if len(p)==8:
#         print(p[2],p[4])
#         my_List.append(p[4])
#     if len(p)==10:
#         print(p[4])
#         my_List.append(p[4])
#     if len(p)==10:
#         print(p[2],p[4],p[6],p[7])
#         my_List.append(p[7])

def p_tableData(p):
    '''tableData : OPENROW OPENHEADER OPENHREF CONTENT CLOSEHREF CONTENT CLOSEHEADER OPENHEADER OPENHREF CONTENT CLOSEHREF CLOSEHEADER OPENHEADER CONTENT OPENHREF CONTENT CLOSEHREF CLOSEHEADER CLOSEROW OPENROW OPENDATA handleList CLOSEDATA OPENDATA OPENHREF CONTENT CLOSEHREF CLOSEDATA OPENDATA handleList CLOSEDATA CLOSEROW handleStadium
                | OPENROW OPENHEADER OPENHREF CONTENT CLOSEHREF CONTENT CLOSEHEADER OPENHEADER OPENHREF CONTENT CLOSEHREF CONTENT OPENHREF CONTENT CLOSEHREF CONTENT CLOSEHEADER OPENHEADER CONTENT OPENHREF CONTENT CLOSEHREF CLOSEHEADER CLOSEROW OPENROW OPENDATA handleList CLOSEDATA OPENDATA OPENHREF CONTENT CLOSEHREF CLOSEDATA OPENDATA handleList CLOSEDATA CLOSEROW handleStadium
                | OPENROW OPENHEADER OPENHREF CONTENT CLOSEHREF CONTENT CLOSEHEADER OPENHEADER OPENHREF CONTENT CLOSEHREF CONTENT OPENHREF CONTENT CLOSEHREF CONTENT CLOSEHEADER OPENHEADER CONTENT OPENHREF CONTENT CLOSEHREF CLOSEHEADER CLOSEROW OPENROW OPENDATA handleList CLOSEDATA OPENDATA OPENHREF CONTENT CLOSEHREF CLOSEDATA OPENDATA handleList CLOSEDATA CLOSEROW OPENROW OPENHEADER OPENHREF CONTENT CLOSEHREF CLOSEHEADER CLOSEROW OPENROW OPENDATA handlepenList CLOSEDATA OPENHEADER CONTENT CLOSEHEADER  OPENDATA handlepenList CLOSEDATA CLOSEROW handleStadium
                | '''
    if len(p)>2 and len(p)<45:
        list.append(p[4])
        list.append(p[10])
        list.append(p[16])
    if len(p)>45:
        list.append(p[4])
        list.append(p[10])
        list.append(p[21])

        

def p_handleList(p):
    '''handleList : skip OPENLIST OPENHREF CONTENT CLOSEHREF skip CLOSELIST handleList
                  | '''
    if len(p)==9:
        list.append(p[4])

def p_handlepenList(p):
    '''handlepenList : skip OPENLIST OPENHREF CONTENT CLOSEHREF skip CLOSELIST handlepenList
                  | skip OPENLIST CONTENT OPENHREF CONTENT CLOSEHREF skip CLOSELIST handlepenList
                  | '''
    if len(p)==9:
        # print(p[4])
        list.append(p[4])
    if len(p)==10:
        #print(p[5])
        list.append(p[5])

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
s="Lusail Stadium, Lusail,Attendance: 88,966,Referee: Szymon Marciniak (Poland)"
l=list[209:224]
l.append(s)

data = {
    "round16" :[list[0:13],list[13:25],list[25:37],list[37:49],list[49:68],list[68:82],list[82:98],list[98:112]],"quarter":[list[112:131],list[131:153],list[153:163],list[163:175]],"semi":[list[175:186],list[186:197]],"third place":[list[197:209]],"final":[l]
}

choice = input("Enter round16,quarter,semi,or final to see desire result: ")
logfile.write(choice+'\n')
if choice =="round16":
    for key in data:
        if 'round16' in key:
            print(key)
            for sublist in data[key]:
                print(sublist)
                logfile.write(str(sublist)+'\n')
elif choice == "quarter":
        for key in data:
            if 'quarter' in key:
                print(key)
                for sublist in data[key]:
                    print(sublist)
                    logfile.write(str(sublist)+'\n')

elif choice == "semi":
        for key in data:
            if 'semi' in key:
                print(key)
                for sublist in data[key]:
                    print(sublist)
                    logfile.write(str(sublist)+'\n')
    
elif choice == "third":
        for key in data:
            if 'third' in key:
                print(key)
                for sublist in data[key]:
                    print(sublist)
                    logfile.write(str(sublist)+'\n')

elif choice == "final":
        for key in data:
            if 'final' in key:
                print(key)
                for sublist in data[key]:
                    print(sublist)
                    logfile.write(str(sublist)+'\n')

else:
    print("Invalid choice!!")



# print(data['final'])

# for i in data:
#     print(i)
#     print(data[i])
# for i in lis:
#     print(i)
# print(data)

# 16
# ['Dumfries', 'Blind', 'Depay', 'Wright', 'Netherlands', '3–1', 'United States', 'Khalifa International Stadium', ', ', 'Al Rayyan', 'Attendance: 44,846', 'Referee: ', 'Wilton Sampaio', 
# 
# 'Álvarez', 'Messi', 'Fernández', 'Argentina', '2–1', 'Australia', 'Ahmad bin Ali Stadium', ', ', 'Al Rayyan', 'Attendance: 45,032', 'Referee: ', 'Szymon Marciniak', 
# 
# 'Mbappé', 'Giroud', 'Lewandowski', 'France', '3–1', 'Poland', 'Al Thumama  Stadium', ', ', 'Doha', 'Attendance: 40,989', 'Referee: ', 'Jesús Valenzuela', 
# 
# 'Saka', 'Kane', 'Henderson', 'England', '3–0', 'Senegal', 'Al Bayt Stadium', ', ', 'Al Khor', 'Attendance: 65,985', 'Referee: ', 'Iván Barton', 
# 
# 'Maeda', 'Perišić', 'Yoshida', 'Asano', 'Mitoma', 'Minamino', 'Pašalić', 'Livaja', 'Brozović', 'Vlašić', 'Japan', '1–1', 'Croatia', 'Al Janoub Stadium', ', ', 'Al Wakrah', 'Attendance: 42,523', 'Referee: ', 'Ismail Elfath', 
# 
# 'Paquetá', 'Richarlison', 'Neymar', 'Vinícius', 'Paik Seung-ho', 'Brazil', '4–1', 'South Korea', 'Stadium 974', ', ', 'Doha', 'Attendance: 43,847', 'Referee: ', 'Clément Turpin', 
# 
# 'Hakimi', 'Benoun', 'Ziyech', 'Sabiri', 'Busquets', 'Soler', 'Sarabia', 'Morocco', '0–0', 'Spain', 'Education City Stadium', ', ', 'Al Rayyan', 'Attendance: 44,667', 'Referee: ', 'Fernando Rapallini', 
# 
# 'Leão', 'Guerreiro','Pepe', 'Ramos', 'Akanji', 'Portugal', '6–1', 'Switzerland', 'Lusail Stadium', ', ', 'Lusail', 'Attendance: 83,720', 'Referee: ', 'César Arturo Ramos', 
# 

# Quarter
# 'Petković', 'Neymar', 'Oršić', 'Modrić', 'Majer', 'Vlašić','Marquinhos', 'Pedro', 'Casemiro', 'Rodrygo', 'Croatia', '1–1', 'Brazil', 'Education City Stadium', ', ', 'Al Rayyan', 'Attendance: 43,893', 'Referee: ', 'Michael Oliver', 
# 
# 'Weghorst', 'Messi', 'Molina', 'L. de Jong', 'Weghorst', 'Koopmeiners', 'Berghuis', 'Van Dijk', 'La. Martínez', 'Fernández', 'Montiel', 'Paredes', 'Messi', 'Netherlands', '2–2', 'Argentina', 'Lusail Stadium', ', ', 'Lusail', 'Attendance: 88,235', 'Referee: ', 'Antonio Mateu Lahoz', 
# 
# 'En-Nesyri', 'Morocco', '1–0', 'Portugal', 'Al Thumama Stadium', ', ', 'Doha', 'Attendance: 44,198', 'Referee: ', 'Facundo Tello',
# 
#  'Kane', 'Giroud', 'Tchouaméni', 'England', '1–2', 'France', 'Al Bayt Stadium', ', ', 'Al Khor', 'Attendance: 68,895', 'Referee: ', 'Wilton Sampaio',



# semi 
#  'Álvarez', 'Messi', 'Argentina', '3–0', 'Croatia', 'Lusail Stadium', ', ', 'Lusail', 'Attendance: 88,966', 'Referee: ', 'Daniele Orsato', 

# 'Kolo Muani', 'T. Hernandez', 'France', '2–0', 'Morocco', 'Al Bayt Stadium', ', ', 'Al Khor', 'Attendance: 68,294', 'Referee: ', 'César Arturo Ramos', 
# 

# third place
# 'Oršić', 'Gvardiol', 'Dari', 'Croatia', '2–1', 'Morocco', 'Khalifa International Stadium', ', ', 'Al Rayyan', 'Attendance: 44,137', 'Referee: ', 'Abdulrahman Al-Jassim', 
# 

# final
# 'Di María', 'Messi', 'Mbappé', 'Montiel', 'Paredes', 'Dybala', 'Messi', 'Kolo 
# Muani', 'Tchouaméni', 'Coman', 'Mbappé', 'Argentina', '3–3', 'France',]
