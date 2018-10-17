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
    x = str('function(documento, tipoDocumento, nombre, apellido, usuario, password, genero, ciudadResidencia, paisResidencia, ciudadNacimiento, paisNacimiento, correo1, correo2, fechaNacimiento){'
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
    ', usuario:usuario'
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
    a =db.eval(x, user.documento, user.tipoDocumento, user.nombre, user.apellido, user.usuario, user.password, user.genero, user.ciudadResidencia, user.paisResidencia, user.ciudadNacimiento, user.paisNacimiento, user.correo1, user.correo2, user.fechaNacimiento);
    return a

def loginUser(user):
    query = str('function(usuario){var userData =JSON.parse(JSON.stringify(db.userData.findOne({usuario:usuario}))); if(userData!=null){return userData["password"];} return "0";}')
    password=db.eval(query, user.usuario)
    if(password=="0"):
        return 0
    elif(not sha256_crypt.verify(user.password, password)):
        return -1
    else:
        return 1
def getUser(user):
    x = str('function(usuario){var userData =JSON.parse(JSON.stringify(db.userData.findOne({usuario:usuario}))); return userData;}')
    a=db.eval(x, user.usuario)
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

    



