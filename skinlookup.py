import asyncio
from minepi import Player
from PIL import Image

async def main(name):
    if len(str(name)) == 32:
        p = Player(uuid=name) # create a Player object by UUID
    else:
        p = Player(name=name) # create a Player object by name
    await p.initialize()  # initialize the Player object
    await p.skin.render_skin(hr=-35, vr=0)
    return p

if __name__ == '__main__':
    asyncio.run(main())