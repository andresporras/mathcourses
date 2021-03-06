#https://pythonprogramming.net/password-hashing-flask-tutorial/ hash with passlib
from pymongo import MongoClient
from bson.code import Code
from passlib.hash import sha256_crypt

client = MongoClient('localhost', 27017)

db = client['users']

collection = db['userData']

def createUser(user):
    user.password = sha256_crypt.encrypt(user.password)
    #nombre = user.nombre
    #a=  db.eval(Code('function exec(){var c=db.userData.find(); return c;} exec();'));
    x = str('function(documento, tipoDocumento, nombre, apellido, email, password, genero, ciudadResidencia, paisResidencia, ciudadNacimiento, paisNacimiento, correo1, correo2, fechaNacimiento){'
    'var text = "";'
    'var possible = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz0123456789";'
    'for (var i = 0; i < 100; i++){'
    'text += possible.charAt(Math.floor(Math.random() * possible.length));'
    '}'
    'db.userData.insert('
    '{'
    'documento: {codigo: documento, tipo:tipoDocumento}'
    ',nombre:nombre'
    ', apellido:apellido'
    ', email:email'
    ', password:password'
    ', idlogeo: text'
    ', genero: genero'
    ', residencia: {ciudad: ciudadResidencia, pais:paisResidencia}'
    ', lugarNacimiento: {ciudad: ciudadNacimiento, pais:paisNacimiento}'
    ', correo1:correo1'
    ', correo2:correo2'
    ', fechaRegistro: new Date()'
    ', fechaNacimiento: new Date(fechaNacimiento)'
    '});'
    'return text;'
    '}')
    #a =db.eval(Code('function(){db.userData.insert({nombre:"oscar2"}); return "hola mundo";}'));
    #a =db.eval(Code('function exec(){var c=JSON.parse(JSON.stringify(db.userData.find({nombre:"andres"})[0])); return c;}'));
    a =db.eval(x, user.documento, user.tipoDocumento, user.nombre, user.apellido, user.email, user.password, user.genero, user.ciudadResidencia, user.paisResidencia, user.ciudadNacimiento, user.paisNacimiento, user.correo1, user.correo2, user.fechaNacimiento);
    return a
async def updateUser(user):
    try:
        query = str('function(email){var userData =JSON.parse(JSON.stringify(db.userData.findOne({email:email}))); if(userData!=null){return userData["password"];} return "0";}')
        password= db.eval(query, user.oldEmail)
        if(getUser(user.newEmail)!=None):
            return -1
        elif(password=="0"):
            return 0
        elif(sha256_crypt.verify(user.password, password)):
            result = collection.update_one({"email":user.oldEmail}, 
            { "$set":{"email":user.newEmail}
                    } )
            return 1
        else:
            return 2
    except Exception as er:
        return er

async def updatePas(user):
    try:
        query = str('function(email){var userData =JSON.parse(JSON.stringify(db.userData.findOne({email:email}))); if(userData!=null){return userData["password"];} return "0";}')
        password= db.eval(query, user.email)
        if(password=="0"):
            return 0
        elif(sha256_crypt.verify(user.oldPas, password)):
            newPassword = sha256_crypt.encrypt(user.newPas)
            result = collection.update_one({"password":password, "email":user.email}, 
            { "$set":{"password":newPassword}
                    } )
            return 1
        else:
            return 2
    except Exception as er:
        return er
    
    #codCreateUser = str('function(newEmail, oldEmail, pas){'
    #'db.userData.update({email: oldEmail,password: pas},{$set:{"email":newEmail}})'
    #'return text;'
    #'}')
    #a =db.eval(codCreateUser, user.newEmail, user.oldEmail, password);
def createSimpleUser(user):
    password = sha256_crypt.encrypt(user.password)
    #nombre = user.nombre
    #a=  db.eval(Code('function exec(){var c=db.userData.find(); return c;} exec();'));
    codCreateUser = str('function(email, password){'
    'var text = "";'
    'var possible = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz0123456789";'
    'for (var i = 0; i < 100; i++){'
    'text += possible.charAt(Math.floor(Math.random() * possible.length));'
    '}'
    'db.userData.insert('
    '{email:email'
    ', password:password'
    '});'
    'return text;'
    '}')
    #a =db.eval(Code('function(){db.userData.insert({nombre:"oscar2"}); return "hola mundo";}'));
    #a =db.eval(Code('function exec(){var c=JSON.parse(JSON.stringify(db.userData.find({nombre:"andres"})[0])); return c;}'));
    a =db.eval(codCreateUser, user.email, password);
    return a

async def loginUser(user):
    query = str('function(email){var userData =JSON.parse(JSON.stringify(db.userData.findOne({email:email}))); if(userData!=null){return userData["password"];} return "0";}')
    password= db.eval(query, user.email)
    if(password=="0"):
        return 0
    elif(not sha256_crypt.verify(user.password, password)):
        return -1
    else:
        return 1
def getUser(email):
    x = str('function(email){var userData =JSON.parse(JSON.stringify(db.userData.findOne({email:email}))); return userData;}')
    a=db.eval(x, email)
    return a

    #    nombre=""
    #apellido=""
    #usuario=""
    #password=""
    #idLogeo=""
    #fechaRegistro=datetime.datetime.now().date()
    #fechaNacimimento=datetime.datetime.now().date()
    #genero=""
    #residencia=0
    #nacionalidad=0
    #correo1=""
    #correo2=""

    



