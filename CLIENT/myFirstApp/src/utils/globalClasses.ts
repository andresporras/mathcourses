
export class product 
{ 
  id: string; 
  nombre: string; 
  caracteristicas:string; 
  fechaLanzamiento:Date;
  correoFabricante:string;
  paisFabricacion:string;
  precio:number;
  unidadesDisponibles:number;
  unidadesVendidas: number;
  imagen: number[];

}

export  class userClass
{ 
    public sessionId: string; 
}

export abstract class globalData {    
  public static sessionId:string="";     
  public static userEmail:string="";  
  public static componentSelector:string="app-menu";
  public static componentSeccion:string="app-cursos";

  public static makeid() {
    var text = "";
    var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
  
    for (var i = 0; i < 100; i++)
      text += possible.charAt(Math.floor(Math.random() * possible.length));
  
    return text;
  }
}