import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule, HttpClient } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import {RouterModule, Routes} from "@angular/router";
import { AppComponent } from './app.component';
//import { NavbarComponent } from './navbar/navbar.component';
import { MenuComponent } from './menu/menu.component';
import { CursosComponent } from './cursos/cursos.component';
import { UsuarioComponent } from './usuario/usuario.component';

//routes mapping
const appRoutes: Routes = [
 // { path: "", redirectTo: "", pathMatch: "full" },
 { path: "menu", component: MenuComponent },
  // { path: "projects", component: ProjectsComponent},
  // { path: "profile", component: ProfileComponent},
];



@NgModule({
  declarations: [
    AppComponent,
    MenuComponent,
    CursosComponent,
    UsuarioComponent,
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule,
    RouterModule.forRoot(appRoutes),
    //NavbarComponent,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
