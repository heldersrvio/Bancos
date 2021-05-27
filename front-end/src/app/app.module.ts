import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { TopBarComponent } from './top-bar/top-bar.component';
import { BankListDisplayComponent } from './bank-list-display/bank-list-display.component';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent,
    TopBarComponent,
    BankListDisplayComponent,
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
