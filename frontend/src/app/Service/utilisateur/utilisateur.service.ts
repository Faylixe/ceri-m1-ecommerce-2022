import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, Subscriber } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UtilisateurService {

  constructor(private _http : HttpClient) { }

  connexion(id : string, mdp : string){
   
    var correct = false; 
    let parametres = new HttpParams();
    parametres = parametres.append('nom_utilisateur', id);
    parametres = parametres.append('mot_de_passe', mdp);
    return Observable.create((observer: Subscriber<Boolean>) => { 
      this._http.get<any>('http://127.0.0.1:8080/api/v1/connexionUtilisateur',{ params: parametres})
      .subscribe(
        data => {
            console.log(" data -- ", data)
            correct=data;
        },
        error=>{
          console.log(" erreur recuperation connexion ", error)
        },
        ()=>{
          observer.next(correct);
        }
      );
    })
  }

  getUserInformations(id : string){
   
    var infos ={}; 
    let parametres = new HttpParams();
    parametres = parametres.append('nom_utilisateur', id);
    return Observable.create((observer: Subscriber<Object>) => { 
      this._http.get<any>('http://127.0.0.1:8080/api/v1/informationUtilisateur',{ params: parametres})
      .subscribe(
        data => {
            console.log(" data -- ", data)
            infos=data;
        },
        error=>{
          console.log(" erreur recuperation infos user ", error)
        },
        ()=>{
          observer.next(infos);
        }
      );
    })
  }

  createUser(nom : string, prenom : string, email : string, id : string, lieudenaissance : string, datedeNaissance : Date,
     mdp : string, status : string, sexe:string
    ){
   
    var correct = false; 
    let parametres = new HttpParams();
    parametres = parametres.append('prenom', prenom);
    parametres = parametres.append('nom', nom);
    parametres = parametres.append('nom_utilisateur', id);
    parametres = parametres.append('lieu_naissance', lieudenaissance);
    parametres = parametres.append('adresse_mail', email);
    parametres = parametres.append('date_naissance', datedeNaissance.toLocaleString());
    parametres = parametres.append('mot_de_passe', mdp);
    parametres = parametres.append('sexe', sexe);
    parametres = parametres.append('statut', status);
    return Observable.create((observer: Subscriber<Boolean>) => { 
      this._http.get<any>('http://127.0.0.1:8080/api/v1/inscrireUtilisateur',{ params: parametres})
      .subscribe(
        data => {
            console.log(" data -- ", data)
            correct=data;
        },
        error=>{
          console.log(" erreur inscription utilisateur  ", error)
        },
        ()=>{
          observer.next(correct);
        }
      );
    })
  }
  
}