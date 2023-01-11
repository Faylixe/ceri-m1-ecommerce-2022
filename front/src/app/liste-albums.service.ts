import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ListeAlbumsService {
  //backend:string='http://localhost:8000'
  backend=environment.BACKEND_URL
  listeProd: { albumName: string, artisteName: string,prix:string,image:string,quantite:number }[] = [];
 

  constructor(private http :HttpClient) { }

  getEverything() : Observable<any>{
    console.log("test service");
    const options = {
	    withCredentials : true,
	    headers: new HttpHeaders({
		    'Content-Type':'application/json',
		    'Access-Control-Allow-Origin':'*'
	    })}
    return this.http.get(this.backend,options);
  }

  getMusicsByArtist(nom_Artiste:string,nom_Album:string): Observable<any> {
    var url=this.backend+"/"+nom_Artiste+"/"+ nom_Album;
    console.log("test service details" ,nom_Artiste,nom_Album);
	  
    const options = {
	    withCredentials : true,
	    headers: new HttpHeaders({
		    'Content-Type':'application/json',
		    'Access-Control-Allow-Origin':'*'
	    })}
    return this.http.get(url,options);
  }

  addProduit(albumN: string,nomArt:string,price:string,img:string,q:number) {
    this.listeProd.push({ albumName: albumN, artisteName:nomArt ,prix:price,image:img,quantite:q });
  }


  removeProduit(albumN: string) {
    let index = this.listeProd.findIndex(p => p.albumName === albumN);
    console.log("index",index)
    if (index !== -1) {
      this.listeProd.splice(index, 1);
    }
  }
  
  

  
}
