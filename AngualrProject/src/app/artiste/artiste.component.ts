import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-artiste',
  templateUrl: './artiste.component.html',
  styleUrls: ['./artiste.component.css']
})
export class ArtisteComponent implements OnInit {

  constructor() { }
  isConnected = false;

  ngOnInit(): void {
    this.isConnected = false;
  }

}
