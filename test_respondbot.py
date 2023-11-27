import test_RESPOND_bot as Test
import time as Sleep

class Miras:
    name = "Sittolls"
    email = "miras.baigashev@gmail.com"
class Diana:
    name = "Diana Sarsembayeva"
    email = "dianasarsembaeva98@gmail.com"

USER = Diana

def test_bot_answering():
    messageID = Test.writeToChatToBot("Hello!")
    counter = 0
    while( True ):
        counter = counter + 1
        if ( Test.getLastMessageId() != messageID ):
            Sleep.sleep(1)
            break
        elif( counter == 1000 ):
            break
    botMessages = Test.readBotMessagesFromChat(2)
    assert botMessages == ['''Usage: Miras: (learn more about Miras) Diana: (learn more about Diana) info: (get your personal details) space: (get details about this space) say hi to everyone: (everyone gets a greeting using a call to the Webex SDK) help: (what you are reading now) stop: (STOPPING THE BOT - SPECIAL ADMIN CODE REQUIRED!!! ) Powered by Webex Node Bot Framework - https://github.com/webex/webex-node-bot-framework''', 
                           '''Sorry, I don't know how to respond to "Sittolls Bot Hello!"'''] or botMessages == ['''Sorry, I don't know how to respond to "Sittolls Bot Hello!"''']
    # for msg in botMessages[::-1]:
    #     print(msg)

def test_bot_command_Miras():
    messageID = Test.writeToChatToBot("Miras")
    counter = 0
    while( True ):
        counter = counter + 1
        if ( Test.getLastMessageId() != messageID ):
            Sleep.sleep(1)
            break
        elif( counter == 1000 ):
            break
    botMessages = Test.readBotMessagesFromChat(1)
    assert botMessages == ['''Miras Baigashev - IT2-2101, Developer and Operator, Student ID: 31133''']
    # for msg in botMessages[::-1]:
    #     print(msg)

def test_bot_command_Diana():
    messageID = Test.writeToChatToBot("Diana")
    counter = 0
    while( True ):
        counter = counter + 1
        if ( Test.getLastMessageId() != messageID ):
            Sleep.sleep(1)
            break
        elif( counter == 1000 ):
            break
    botMessages = Test.readBotMessagesFromChat(1)
    assert botMessages == ['''Diana Sarsembayeva - IT2-2101, Developer and Operator, Student ID: 31130''']
    # for msg in botMessages[::-1]:
    #     print(msg)

def test_bot_command_Info():
    messageID = Test.writeToChatToBot("Info")
    counter = 0
    while( True ):
        counter = counter + 1
        if ( Test.getLastMessageId() != messageID ):
            Sleep.sleep(1)
            break
        elif( counter == 1000 ):
            break
    botMessages = Test.readBotMessagesFromChat(1)
    assert botMessages == [f'''Here is your personal information: Name: {USER.name} Email: {USER.email} Avatar URL: undefined''']
    # for msg in botMessages[::-1]:
    #     print(msg)

def test_bot_command_Space():
    messageID = Test.writeToChatToBot("Space")
    counter = 0
    while( True ):
        counter = counter + 1
        if ( Test.getLastMessageId() != messageID ):
            Sleep.sleep(1)
            break
        elif( counter == 1000 ):
            break
    botMessages = Test.readBotMessagesFromChat(1)
    assert botMessages == ['''The title of this space: WEBEX organization environment The roomID of this space: Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vYzdmMTk1ZTAtNmU1OC0xMWVlLThiYzgtYmZkZTE0OTRjNTMz The type of this space: group''']
    # for msg in botMessages[::-1]:
    #     print(msg)

def test_bot_command_Hi_Everyone():
    messageID = Test.writeToChatToBot("Say Hi to everyone!")
    counter = 0
    while( True ):
        counter = counter + 1
        if ( Test.getLastMessageId() != messageID ):
            Sleep.sleep(1)
            break
        elif( counter == 1000 ):
            break
    botMessages = Test.readBotMessagesFromChat(2)
    assert botMessages == ['''Hello Diana Sarsembayeva''', 
                           '''Hello Sittolls'''] or botMessages == ['''Hello Sittolls''', 
                                                                    '''Hello Diana Sarsembayeva''']
    # for msg in botMessages[::-1]:
    #     print(msg)

def test_bot_command_Help():
    messageID = Test.writeToChatToBot("Help")
    counter = 0
    while( True ):
        counter = counter + 1
        if ( Test.getLastMessageId() != messageID ):
            Sleep.sleep(1)
            break
        elif( counter == 1000 ):
            break
    botMessages = Test.readBotMessagesFromChat(2)
    assert botMessages == ['''Usage: Miras: (learn more about Miras) Diana: (learn more about Diana) info: (get your personal details) space: (get details about this space) say hi to everyone: (everyone gets a greeting using a call to the Webex SDK) help: (what you are reading now) stop: (STOPPING THE BOT - SPECIAL ADMIN CODE REQUIRED!!! ) Powered by Webex Node Bot Framework - https://github.com/webex/webex-node-bot-framework''',
                            f'''Hello {USER.name}.''']
    # for msg in botMessages[::-1]:
    #     print(msg)

def test_bot_command_Shutdown():
    messageID = Test.writeToChatToBot("Stop")
    counter = 0
    while( True ):
        counter = counter + 1
        if ( Test.getLastMessageId() != messageID ):
            Sleep.sleep(1)
            break
        elif( counter == 1000 ):
            break
    botMessages = Test.readBotMessagesFromChat(1)
    assert botMessages == ['''You want to shut me down? If so, provide a termination code please..''']
    # for msg in botMessages[::-1]:
    #     print(msg)