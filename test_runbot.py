import RUN_bot
import time as Sleep
from webexteamssdk import WebexTeamsAPI
# Get fresh private token - https://developer.webex.com/docs/getting-started
PRIVATE_TOKEN = "MWNiMTdlNGUtNTljNS00NWI4LTk0OGMtN2I5ZGQ2MjQ0YTk4YWFhMDZkOTMtNzEy_PE93_64bb227d-594d-4030-a56f-373e324be165"

api = WebexTeamsAPI(
    access_token=PRIVATE_TOKEN)

def test_Server_Response():
    assert RUN_bot.Server.http_check_withPort("http://localhost:", 7001) == 200

def test_Static_Domain():
    assert RUN_bot.Server.http_check("http://tough-bullfrog-sincerely.ngrok-free.app") == 200

def test_Config():
    assert RUN_bot.Server.config_check() == '''# Copy this file to .env and replace with live values
    WEBHOOKURL="https://tough-bullfrog-sincerely.ngrok-free.app"
    BOTTOKEN="ZDg5YWMzMjYtNWY3OC00YjA3LWI2NWUtMjBmMTIxOWQxZjIxMDQzZTNiZWYtNDE3_PE93_64bb227d-594d-4030-a56f-373e324be165"
    PORT=7001\n'''

room = "Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vYzdmMTk1ZTAtNmU1OC0xMWVlLThiYzgtYmZkZTE0OTRjNTMz"

ID = messages = api.messages.list(roomId=room)
for message in messages:
    ID = message.id
    break

def test_Bot_Response():
    messageID = api.messages.create(roomId=room,
                                    markdown=f"<@personEmail:sittolls@webex.bot|Sittolls Bot> Help").id
    counter = 0
    while( True ):
        counter = counter + 1
        if ( ID != messageID ):
            Sleep.sleep(3)
            break
        elif( counter == 1000 ):
            break

    botMessages = []
    messages = api.messages.list(roomId=room)
    counter = 0
    botcounter = 0
    for message in messages:
        counter = counter + 1
        
        if ( message.personId == "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8xMTA5YjdlYS1kODRkLTQ0Y2QtOWM0Ni01NTc0YTdmM2NlMGI" ):
            botcounter = botcounter + 1    
            if ( botcounter <= 2 ):
                botMessages.append(message.text)
            else:
                break

    assert botMessages == ['''Usage: Miras: (learn more about Miras) Diana: (learn more about Diana) info: (get your personal details) space: (get details about this space) say hi to everyone: (everyone gets a greeting using a call to the Webex SDK) help: (what you are reading now) stop: (STOPPING THE BOT - SPECIAL ADMIN CODE REQUIRED!!! ) Powered by Webex Node Bot Framework - https://github.com/webex/webex-node-bot-framework''',
                            f'''Hello Sittolls.''']
