import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders  } from "@angular/common/http";

@Component({
  selector: 'app-cursos',
  templateUrl: './cursos.component.html',
  styleUrls: ['./cursos.component.css']
})
export class CursosComponent implements OnInit {
  courseList: JSON;
  examData: JSON;
  show: number=0;
  radioValue: String[]=[];
  score:number=0;
  listChars:String[]=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];
  constructor(private httpClient:HttpClient) {
    this.getCourses();
   }

  ngOnInit() {

  }

  getCourses() {
    this.httpClient.get<JSON>('http://localhost:5000/courses/getData')
    .subscribe(data => {
      console.log(data);
      debugger;
      this.courseList = data as JSON;

      console.log(this.courseList);
      //globalData.sessionId = this.serverData['token'];
    })
  }

  generateExam(course:String, unit:String) {
    let options =  
    {headers: new  HttpHeaders({ 'Content-Type': 'application/json'
    ,'**Accept**': 'application/json'
})};
    
    var userData={course, unit};
    this.httpClient.post<JSON>('http://localhost:5000/courses/generateExam', userData, options)
    .subscribe(data => {
      this.examData = data as JSON;
      this.show=1;
      this.radioValue=[];
      this.score=0;
      console.log(this.examData);
    })
  }

  updateScore(newValue:string, index:number){
    this.radioValue[index]=newValue;
    this.score=0;
    debugger;
    for(var i=0;i<this.radioValue.length;i++){
      if(this.radioValue[i]==this.examData[i]['solution']){
        this.score+=1;
      }
    }
  }

}
