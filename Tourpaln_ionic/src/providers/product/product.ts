import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable()
export class ProductProvider {
  url;

  constructor(public http: HttpClient) {
    console.log('Hello ProductProvider Provider');
    this.url = "http://127.0.0.1:8000/api/list/?format=json";
  }
  getProductList(){
  	return this.http.get(this.url)
  }
}
