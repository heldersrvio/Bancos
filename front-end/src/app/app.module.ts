import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { TopBarComponent } from './top-bar/top-bar.component';
import { BankListDisplayComponent } from './bank-list-display/bank-list-display.component';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { BankSearchComponent } from './bank-search/bank-search.component';

@NgModule({
  declarations: [
    AppComponent,
    TopBarComponent,
    BankListDisplayComponent,
    BankSearchComponent,
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
