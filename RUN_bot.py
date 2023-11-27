# import ngrok python sdk
import ngrok
import os
import requests

BOTTOKEN = "ZDg5YWMzMjYtNWY3OC00YjA3LWI2NWUtMjBmMTIxOWQxZjIxMDQzZTNiZWYtNDE3_PE93_64bb227d-594d-4030-a56f-373e324be165"
AUTHTOKEN = "2WyYHZqerSVsfNt3xLZQ6olzzmc_7K8mrKX69BT7bEpAsuMUU"
API_KEY = "2XyaAtrBcL5yOWlshjgVqD6wXaP_7LioYQo2hKQTPevWLCUmr"
STATIC_DOMAIN = "tough-bullfrog-sincerely.ngrok-free.app"
PORT = 7001

class Server: 
    
    def clear_server():
        ngrok.disconnect()
        print( "\n-----All the sessions cleared-----\n" )

    def connect_server():
        # Establish connectivity
        print( "HTTP Server powering up..." )
        listener = ngrok.connect(PORT, authtoken=AUTHTOKEN, domain=STATIC_DOMAIN)
        return listener.url()
    
    def config_update(address):
        # Update the ip address with new one
        print("Updating the address of env...\n")

        open('.env', 'w+').write(
            '''# Copy this file to .env and replace with live values
    WEBHOOKURL="''' + address + '''"
    BOTTOKEN="''' + BOTTOKEN + '''"
    PORT=''' + str(PORT) + '''\n'''
        )
    
    def config_check():
        return open('.env', "r").read()
    
    def http_check(URL):
        response = requests.get(url=URL)
        return response.status_code
    
    def http_check_withPort(URL, Port):
        response = requests.get(url=URL + str(Port))
        return response.status_code
    
    def start_bot(command):
        # Start Webex Bot
        os.system("cmd /c" + command)

    def shutdown_server():
        print( "\n\n-----HTTP Server shutdown-----" )
        ngrok.disconnect()



def bot_startup():
    try:
        while(True):
            Server.clear_server()

            url = Server.connect_server()

            # Output ngrok url to console
            print(f"Ingress established at {url}\n")

            Server.config_update(url)

            config = Server.config_check()
            print(config)

            # status = Server.http_check()
            # print("HTTP status: " + status)

            cmd = "npm start"
            Server.start_bot(cmd)

            # Shutdown instructions
            input( "Server running...\n\nPress (Ctrl+C) to shutdown the server" )

    except (KeyboardInterrupt):
        Server.shutdown_server()

# prompt = input("START THE BOT? - Y/N")
# if ( prompt == "Yes" or prompt == "Y" or prompt == "y" or prompt == "start" ):
#     bot_startup()
# else:
#     print("PROGRAM SHUTDOWN...")

# bot_startup()