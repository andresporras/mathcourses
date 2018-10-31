
import { Component } from '@angular/core';
import { HttpClient, HttpHeaders  } from "@angular/common/http";
import {RequestOptions, Request, RequestMethod} from '@angular/http';
import { map, catchError, tap } from 'rxjs/operators';
import {ActivatedRoute, Router} from "@angular/router";
import {globalData} from '../utils/globalClasses';
import { componentFactoryName } from '@angular/compiler';

// export function getMySuperTemplate(template: string) {
//   return DEFAULT_PREFIX + template + '.html';
// }

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  serverData: JSON;
  employeeData: JSON;
  title = 'welcome to math courses';
  // nameValue='';
  // passValue='';
  usuario='';
  pas='';
  loginSuccess=0;
  componentSelector="";

  constructor(private httpClient:HttpClient, private router : Router){
    this.componentSelector=globalData.componentSelector;
  }

  sayHi(){
    console.log("hello world");
  }

  // doLogin(){
  //   const options = new RequestOptions({
  //     method: RequestMethod.Get,
  //     url: 'http://localhost:5000/todos/case2/todo1'
  //   });
  //   const req = new Request(options);
  //   console.log(req);
  // }

  private extractData(res: Response) {
    let body = res;
    return body || { };
  }

  doLogin() {
    let options =  
    {headers: new  HttpHeaders({ 'Content-Type': 'application/json'
    ,'Accept': 'application/json'
//   ,'Access-Control-Allow-Origin':'*'
//   ,"Access-Control-Allow-Credentials": "true"
//   ,"Access-Control-Allow-Methods": "GET, HEAD, OPTIONS, POST, PUT, DELETE"
// ,"Access-Control-Request-Headers": "X-Requested-With, Content-Type, Accept, Origin, Authorization"
})};
    
    var userData={usuario: this.usuario, password: this.pas};
    this.httpClient.post<any>('http://127.0.0.1:5000/user/loginUser', userData, options)
    .subscribe(data => {
      this.serverData = data as JSON;
      globalData.sessionId = this.serverData['token'];
      debugger;
      if(data=="-1"){
       this.loginSuccess=1;
      }
      else{
        this.loginSuccess=2;
        console.log(this.serverData);
        //this.router.navigateByUrl('/menu');
      }

    })
  }
   
}
