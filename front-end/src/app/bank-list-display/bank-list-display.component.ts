import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { catchError } from 'rxjs/operators';

@Component({
    selector: 'app-bank-list-display',
    templateUrl: './bank-list-display.component.html',
    styleUrls: ['./bank-list-display.component.css'],
})
export class BankListDisplayComponent {
    buttonLabel = 'Listar todos os bancos'
    banks = {
        list: []
    }
    constructor (private http: HttpClient) {

    }
    onClick(): void {
        this.buttonLabel = 'Atualizar'
        this.http.get('https://bancos-back-end.herokuapp.com/bankslist').subscribe((obj) => console.log(obj))
    }
}