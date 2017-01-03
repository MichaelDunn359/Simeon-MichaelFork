#!C:/Python27/python
'''
#import sqlite3
import webapp2
import codecs


#print "Content-type: text/html\n\n"
#print "<html><head><title>Hello World from Python</title></head><body>Hello World from a Python CGI Script</body></html>"

#I've dumped some ideas in here



#=========================================================functions
def loadLobby(intin):
    lobbyinstance = lobbies[intin]
    if lobbyinstance.getPassword() == "" :
        #no password standard load 
        loadPage(lobbyinstance)
        return 1
    else:
        #load password pages
        loadPasswordPage(lobbyinstance)
        return 1
            
    
def loadPasswordPage(lobbyinstance):
    #this is where we use the json to send the lobby deets?
    return 1
def loadPage(lobbyinstance):
    #this is where we use the json to send the lobby deets?
    return 1

def makeLobby(editableByAll, memberCount, lobbyName):
        lobby = Lobby(editableByAll, memberCount, lobbyName)
        lobbies.append(lobby)
        return lobby
    


def initdabase():
    db = sqlite3.connect('testdatabse.db')
    c = db.cursor()
    #makes database connection object stored as testdatabase.db
    
    #creates table in the database
    db.execute('create table lobby (lobbyname text, password text)')
    
    #insert format
    #c.execute("insert into lobby values('hey', 'heypass') ")
    
    #drop if exists 
    #c.executescript('drop table if exists lobby;')
    #save and close boys
    db.commit()
    c.close()
    db.close()
    return 1 
   
    #==============================================================OBJECTS=========================================
#lobby object
class Lobby(object):
    editableByAll = None
    memberCount = 0
    lobbyName = ""
    array = [[0 for x in range(320)] for y in range(180)] 
    password = ""
    chatArray = ["+++chat log+++"] #we can sort chat list expansion later

    #initializer 
    def __init__(self, editableByAll, memberCount, lobbyName, array, password):
        self.editableByAll = editableByAll
        self.lobbyName = lobbyName
        self.memberCount = memberCount
        self.array = array
        self.password = password
        return 1
     

    def getPasword(self):
        return self.password

#need to make getters and setters for all attributes
#=============================================================================MAIN=============================================
#lobbies = [10]


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('value equals')
        #self.response.write(self.request.get("val"))
    def load(self):
        codecs.

app = webapp2.WSGIApplication([('/', MainPage),])
page = codecs.open("index.html", 'r', 'utf-8')

'''

import webapp2
import codecs
#import canvas
#import cover
#hello world copy pasta

class MainPage(webapp2.RequestHandler):
    def get(self):
        print "running"
        #self.response.headers['Content-Type'] = 'text/plain'
        #self.response.write('Hello, World!')
        page = codecs.open("Html/index.html", 'r', 'utf-8')
        self.response.write(page.read())
        
    def hello(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')
        #page = codecs.open("index.html", 'r', 'utf-8')
        #self.response.write(page.read())


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
