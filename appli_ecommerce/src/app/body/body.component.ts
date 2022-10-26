import { Component, OnInit } from '@angular/core';
import { ListeAlbumsService } from '../liste-albums.service';


@Component({
  selector: 'app-body',
  templateUrl: './body.component.html',
  styleUrls: ['./body.component.css']
})
export class BodyComponent implements OnInit {
  listeAlb:any;
  liste : ListeAlbumsService

  constructor(liste:ListeAlbumsService) {
    this.liste=liste;

   }

   ngOnInit(): void {
	  this.afficheListeAlbums();
  }

  afficheListeAlbums(){
    this.liste.getEverything().subscribe(
			(data : any) => {
				this.listeAlb=JSON.parse(JSON.stringify(data));
				console.log("liste albums = "+ this.listeAlb);
			});
			(error : any) => {
				console.log("une erreur c'est produite");
			}
  }
}

