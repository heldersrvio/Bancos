import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { catchError } from 'rxjs/operators';
import { AllBanks } from '../allBanks';

@Component({
    selector: 'app-bank-list-display',
    templateUrl: './bank-list-display.component.html',
    styleUrls: ['./bank-list-display.component.css'],
})
export class BankListDisplayComponent {
    buttonLabel = 'Listar todos os bancos'
    banks: string[] = []
    loading = false
    error = false
    
    constructor (private http: HttpClient) {

    }
    onClick(): void {
        this.loading = true
        this.buttonLabel = 'Atualizar'
        this.http.get<AllBanks>('https://bancos-back-end.herokuapp.com/bankslist').subscribe((obj) => {
            this.banks = obj.list
            this.error = false
            this.loading = false
        }, (_error) => {
            this.error = true
            this.loading = false
        })
    }
}