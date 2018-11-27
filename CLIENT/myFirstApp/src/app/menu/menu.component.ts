import { Component, OnInit } from '@angular/core';
import {globalData} from '../../utils/globalClasses';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css']
})
export class MenuComponent implements OnInit {
  gd:any= globalData;
  constructor() { }

  ngOnInit() {
  }

  public abrirSeccion(variable:string){
    this.gd.componentSeccion= variable;
    console.log(variable);
  }

}
