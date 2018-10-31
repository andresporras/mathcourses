import UserDll
import asyncio

def createUser(nUsuario):
        return UserDll.createUser(nUsuario)
def loginUser(nUsuario):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(UserDll.loginUser(nUsuario))
    loop.close()
    return result
    #return UserDll.loginUser(nUsuario)
def getUser(nUsuario):
        return UserDll.getUser(nUsuario)
#class UserBll():
    
