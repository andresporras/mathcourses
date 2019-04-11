import UserDll
import asyncio

def createUser(nUsuario):
        return UserDll.createUser(nUsuario)
def updateUser(nUsuario):
        return UserDll.updateUser(nUsuario)
def loginUser(nUsuario):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(UserDll.loginUser(nUsuario))
    loop.close()
    return result
    #return UserDll.loginUser(nUsuario)
def getUser(nUsuario):
        return UserDll.getUser(nUsuario)
def signUp(nUsuario):
    request= UserDll.getUser(nUsuario)
    if(request==None):
        UserDll.createSimpleUser(nUsuario)
        return loginUser(nUsuario)
    else:
        return "-1"
#class UserBll():
    
