import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { catchError } from 'rxjs/operators';
import { Bank } from '../bank';

@Component({
  selector: 'app-bank-search',
  templateUrl: './bank-search.component.html',
  styleUrls: ['./bank-search.component.css']
})
export class BankSearchComponent implements OnInit {

  error = false
  inputText = ''
  result = ''

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
  }

  onClick(): void {
    if (this.inputText.length > 0) {
      this.http.get<Bank>(`https://bancos-back-end.herokuapp.com/bankname/${this.inputText}`).subscribe((obj) => this.result = obj.name)
    }
  }

}
