import { Component, OnInit } from '@angular/core';

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
  pas1='';
  pas2='';
  fieldE='';
  fieldP='';
  updateFails:updateFails[]=[];
  currentFail=0;
  updateSuccess=0;
  constructor() {
    this.updateFails.push({message:"login input data is not correct", classes:"alert alert-danger"});
    this.updateFails.push({message:"user already exist", classes:"alert alert-warning"});
    this.updateFails.push({message:"password must have 8 or more characters", classes:"alert alert-warning"});
    this.updateFails.push({message:"use a valid email", classes:"alert alert-warning"});
   }

  ngOnInit() {
  }

  showForm(index:number) {
    this.show=index;
  }

  updatePassword() {
    if(this.pas1.length<8){
      this.currentFail= 2;
        this.updateSuccess=1;
    }
    // else if(this.regexpEmail.test(this.usuario)==false){
    //   this.currentFail= 3;
    //   this.loginSuccess=1;
    // }
    // else{
    //   this.createUser();
    // }
    
  }

}
