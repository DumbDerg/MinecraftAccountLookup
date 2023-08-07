import asyncio
import os

import skinlookup
import urllib.request
import requests


# Gonna see if valid UUID or username before it's ran inside getPlayerInfo()
def checkIfValid(userInput):
    if 0 < len(str(userInput)) <= 16:
        try:
            urllib.request.urlopen("https://api.mojang.com/users/profiles/minecraft/" + userInput).read()
            return True
        except urllib.error.HTTPError:
            return False
    elif len(str(userInput)) == 32:
            test = requests.get('https://sessionserver.mojang.com/session/minecraft/profile/'+userInput)
            if str(test) != "<Response [204]>":
                return True
            else:
                return False

    else:
        return False


# Gets the player object
def getPlayerInfo(name):
    player = asyncio.run(skinlookup.main(name))
    return player
# Downloads the resources to the users download folder
def downloadSkin(player):
    urllib.request.urlretrieve(player.skin.raw_skin_url,"downloads/"+player.name+".png")


if __name__ == '__main__': pass