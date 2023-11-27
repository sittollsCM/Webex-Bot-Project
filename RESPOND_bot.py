from webexteamssdk import WebexTeamsAPI
import datetime as DT
import time as Sleep
# Get fresh private token - https://developer.webex.com/docs/getting-started
PRIVATE_TOKEN = "ZDIyYzI2OWQtNWZmOC00MzFhLTlkOGQtNzBlNzBkZmEzNWNhYTJiNWEwYzAtOTVl_PE93_64bb227d-594d-4030-a56f-373e324be165"
PRIVATE_TOKEN1 = "NjRkMTY4MjgtNDk5OC00ZGNmLWEzOTQtZTMxYTJlOGVkMGZhMTljNTYwNDQtM2Yz_PE93_64bb227d-594d-4030-a56f-373e324be165"
BOT_TOKEN = "ZDg5YWMzMjYtNWY3OC00YjA3LWI2NWUtMjBmMTIxOWQxZjIxMDQzZTNiZWYtNDE3_PE93_64bb227d-594d-4030-a56f-373e324be165"
ORG_TOKEN = "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi82NGJiMjI3ZC01OTRkLTQwMzAtYTU2Zi0zNzNlMzI0YmUxNjU"

api = WebexTeamsAPI(
    access_token=PRIVATE_TOKEN1)

roomName = "WEBEX organization environment"

def findOrg(ORG):
    orgs = api.organizations.list()
    
    for org in orgs:
        if( org.id == ORG ):
            return org.id

def findRoom(roomTitle):
    rooms = api.rooms.list()
    # print("\nRooms:")
    for room in rooms:
        # print(room.title)
        if ( room.title == roomTitle ):
            roomID = room.id
    # print("\n")
    
    # print("Main room: " + roomName + "\n\n")
    return roomID

def findBot(botTitle, roomID):
    users = api.memberships.list(roomId=roomID)
    # print("Users:")
    for user in users:
        # print(user.personDisplayName)
        if ( user.personDisplayName == botTitle ):
            botID = user.personId
    # print("\n")
    return botID

orgID = findOrg(ORG_TOKEN)
roomID = findRoom(roomName)
botID = findBot("Sittolls Bot", roomID)
BOTEMAIL = "sittolls@webex.bot"

def writeToChat(msg):
    return api.messages.create(roomId=roomID, markdown=f"{msg}").id

def writeToChatToBot(msg):
    return api.messages.create(roomId=roomID, markdown=f"<@personEmail:{BOTEMAIL}|Sittolls Bot> {msg}").id

def readBotMessagesFromChat(amount):
    response = []
    messages = api.messages.list(roomId=roomID)
    counter = 0
    botcounter = 0
    # open("temp", "w+")
    for message in messages:
        counter = counter + 1
        # Serializing messages with timestamps
        # time = DT.datetime.strptime(str(message.created), '%Y-%m-%dT%H:%M:%S.%fZ')
        # open("temp", "a+").write(str(time) + " - {\n" + message.text + "\n} - " + message.personEmail + "\n\n")
        
        if ( message.personId == botID ):
            botcounter = botcounter + 1    
            if ( botcounter <= amount ):
                # print( f"The {botcounter}'th message from {api.people.get( message.personId ).displayName} - {message.text}"  )
                response.append(message.text)
            else:
                break
    return response
    # open("temp", "a+").write("Total messages: " + str(counter))

def getLastMessageId():
    messages = api.messages.list(roomId=roomID)
    for message in messages:
        return message.id

# Test functionality
# displayNumber = 1
# readBotMessagesFromChat(displayNumber)