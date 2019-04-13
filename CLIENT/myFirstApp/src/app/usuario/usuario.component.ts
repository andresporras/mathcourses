import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders  } from "@angular/common/http";
import {ActivatedRoute, Router} from "@angular/router";
import {globalData} from '../../utils/globalClasses';

interface updateFails{
  message:String;
  classes:String;
}

@Component({
  selector: 'app-usuario',
  templateUrl: './usuario.component.html',
  styleUrls: ['./usuario.component.css']
})



export class UsuarioComponent implements OnInit {
  show: number=0;
  newPas='';
  oldPas='';
  fieldE='';
  fieldP='';
  serverData: JSON;
  updateFails:updateFails[]=[];
  currentFail=5;
  updateSuccess=0;
  constructor(private httpClient:HttpClient, private router : Router) {
    this.updateFails.push({message:"login input data is not correct", classes:"alert alert-danger"});
    this.updateFails.push({message:"user already exist", classes:"alert alert-warning"});
    this.updateFails.push({message:"password is incorrect", classes:"alert alert-warning"});
    this.updateFails.push({message:"use a valid email", classes:"alert alert-warning"});
    this.updateFails.push({message:"email successfully changed", classes:"alert alert-success"});
    this.updateFails.push({message:"something wrong happen", classes:"alert alert-warning"});
    this.updateFails.push({message:"password successfully changed", classes:"alert alert-success"});
    this.updateFails.push({message:"password must have 8 or more characters", classes:"alert alert-warning"});
   }

  ngOnInit() {
  }

  showForm(index:number) {
    this.show=index;
  }

  updatePassword() {
    if(this.newPas.length<8 || this.oldPas.length<8){
      this.currentFail= 7;
        this.updateSuccess=1;
    }
    else{
      let options =  
      {headers: new  HttpHeaders({ 'Content-Type': 'application/json'
      ,'Accept': 'application/json'
  })};
       
      var userData={oldPas: this.oldPas, newPas: this.newPas, email:globalData.userEmail};
      debugger; 
      this.httpClient.post<JSON>('http://localhost:5000/user/updatePas', userData, options)
      .subscribe(data => {
        var result = data as JSON;
        
        if(result['result']=="0"){
          this.currentFail= 5;
        }
        else if(result['result']=="1"){
          this.currentFail= 6;
          this.oldPas="";
          this.newPas="";
        }
        else if(result['result']=="2"){
          this.currentFail= 2;
        }
        debugger;
        // this.examData = data as JSON;
        // this.show=1;
        // this.radioValue=[];
        // this.score=0;
        this.updateSuccess=1;
      })  
    }

    
    // else if(this.regexpEmail.test(this.usuario)==false){
    //   this.currentFail= 3;
    //   this.loginSuccess=1;
    // }
    // else{
    //   this.createUser();
    // }
    
  }

  updateEmail(){

    if(globalData.regexpEmail.test(this.fieldE)==false){
      this.currentFail= 3;
    }
    else{
      let options =  
      {headers: new  HttpHeaders({ 'Content-Type': 'application/json'
      ,'Accept': 'application/json'
  })};
       
      var userData={newEmail: this.fieldE, password: this.fieldP, oldEmail:globalData.userEmail};
      debugger; 
      this.httpClient.post<JSON>('http://localhost:5000/user/updateUser', userData, options)
      .subscribe(data => {
        var result = data as JSON;
        if(result['result']=="-1"){
          this.currentFail= 1;
        }
        else if(result['result']=="0"){
          this.currentFail= 5;
        }
        else if(result['result']=="1"){
          this.currentFail= 4;
          globalData.userEmail=this.fieldE;
          this.fieldE="";
          this.fieldP="";
        }
        else if(result['result']=="2"){
          this.currentFail= 2;
        }
        debugger;
        // this.examData = data as JSON;
        // this.show=1;
        // this.radioValue=[];
        // this.score=0;
        this.updateSuccess=1;
      })  
    }

    
  }

  


}
