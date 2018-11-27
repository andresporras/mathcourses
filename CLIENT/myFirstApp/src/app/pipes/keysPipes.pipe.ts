import {Pipe, PipeTransform} from '@angular/core';
//code taken from: https://stackoverflow.com/questions/35647365/how-to-display-json-object-using-ngfor
//improved with: https://stackoverflow.com/questions/39007130/the-pipe-could-not-be-found-angular2-custom-pipe

@Pipe({name: 'keys'})
export class KeysPipe implements PipeTransform {
  transform(value, args:string[]) : any {
    let keys = [];
    for (let key in value) {
      keys.push({key: key, value: value[key]});
    }
    return keys;
  }
}