import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders  } from "@angular/common/http";


class courses{
  name: Text;
  selected: boolean;
}

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
  equation:String='<img src="http://latex.codecogs.com/gif.latex?$$ J(\theta) = \frac{1}{m} \sum^m_{i=1} Cost(h_\theta(x),y) $$" border="0"/>';
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
      // var listCourses = JSON.parse(JSON.stringify(data));
      // for(let c in this.courseList){
      //   var h =c;
      //   for(let u in c['units']){
      //     console.log(u['cod']);
      //   }
      // }
      //globalData.sessionId = this.serverData['token'];
    })
  }

  mixExam() {
    let options =  
    {headers: new  HttpHeaders({ 'Content-Type': 'application/json'
    ,'**Accept**': 'application/json'
})};
    debugger;
    this.httpClient.post<JSON>('http://localhost:5000/courses/mixExam', this.courseList, options)
    .subscribe(data => {
      this.examData = data as JSON;
      this.show=1;
      this.radioValue=[];
      this.score=0;
      console.log(this.examData);
    })
  }

  generateExam(course:String, unit:String) {
    let options =  
    {headers: new  HttpHeaders({ 'Content-Type': 'application/json'
    ,'**Accept**': 'application/json'
})};
    
    var userData={course, unit};
    debugger;
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
