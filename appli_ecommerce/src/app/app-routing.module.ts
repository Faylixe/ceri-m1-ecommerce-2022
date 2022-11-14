import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { AppComponent } from './app.component';
import { HeaderComponent } from 'src/app/header/header.component';
import { BodyComponent } from 'src/app/body/body.component';


const routes: Routes = [
  {path: '' , component : AppComponent},
  {path: 'header' , component : HeaderComponent},
  {path: 'body' , component : BodyComponent},


];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
