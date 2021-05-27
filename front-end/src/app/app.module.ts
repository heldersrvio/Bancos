import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { TopBarComponent } from './top-bar/top-bar.component';

import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent,
    TopBarComponent,
  ],
  imports: [
    BrowserModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
