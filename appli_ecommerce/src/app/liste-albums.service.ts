import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ListeAlbumsService {

  constructor(private http :HttpClient) { }

  getEverything() : Observable<any>{
    console.log("test service");
	  return this.http.get('http://localhost:8000',{withCredentials : true});
    
  }
}
