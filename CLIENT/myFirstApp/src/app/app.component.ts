
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

interface choice{
  idChoice:String;
  textChoice:String;
}

interface loginFails{
  message:String;
  classes:String;
}

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
  loginFailMessage="";
  defaultChoice="0";
  choices:choice[]=[];
  loginFails:loginFails[]=[];
  currentFail=0;
  regexpEmail = new RegExp('^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$');

  constructor(private httpClient:HttpClient, private router : Router){
    this.componentSelector=globalData.componentSelector;
    this.choices.push({idChoice:"0", textChoice:"sign in"});
    this.choices.push({idChoice:"1", textChoice:"sign up"});
    this.choices.push({idChoice:"2", textChoice:"recover password"});
    this.loginFails.push({message:"login input data is not correct", classes:"alert alert-danger"});
    this.loginFails.push({message:"user already exist", classes:"alert alert-warning"});
    this.loginFails.push({message:"password must have 8 or more characters", classes:"alert alert-warning"});
    this.loginFails.push({message:"use a valid email", classes:"alert alert-warning"});
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

  cleanLogin() {
    this.usuario="";
    this.pas="";
  }

  
  login(){
    let options =  
    {headers: new  HttpHeaders({ 'Content-Type': 'application/json'
    ,'Accept': 'application/json'
})};
    
    var userData={usuario: this.usuario, password: this.pas};
    this.httpClient.post<any>('http://127.0.0.1:5000/user/loginUser', userData, options)
    .subscribe(data => {
      this.serverData = data as JSON;
      globalData.sessionId = this.serverData['token'];
      debugger;
      if(globalData.sessionId=="-1"){
       this.currentFail= 0;
       this.loginSuccess=1;
      }
      else{
        globalData.userEmail=this.usuario;
        this.loginSuccess=2;
        console.log(this.serverData);
        //this.router.navigateByUrl('/menu');
      }
    })
  }

  createUser(){
    let options =  
    {headers: new  HttpHeaders({ 'Content-Type': 'application/json'
    ,'Accept': 'application/json'
})};
    
    var userData={usuario: this.usuario, password: this.pas};
    this.httpClient.post<any>('http://127.0.0.1:5000/user/signUp', userData, options)
    .subscribe(data => {
      this.serverData = data as JSON;
      globalData.sessionId = this.serverData['token'];
      debugger;
      if(globalData.sessionId=="-1"){
        this.currentFail= 1;
        this.loginSuccess=1;
      }
      else{
        this.loginSuccess=2;
        console.log(this.serverData);
        //this.router.navigateByUrl('/menu');
      }

    })
  }

  doLogin() {
    if(this.defaultChoice=="0"){
      this.login();
    }
    else if(this.defaultChoice=="1"){
      if(this.pas.length<8){
        this.currentFail= 2;
        this.loginSuccess=1;
      }
      else if(this.regexpEmail.test(this.usuario)==false){
        this.currentFail= 3;
        this.loginSuccess=1;
      }
      else{
        this.createUser();
      }
      
    }
    
  }
   
}
