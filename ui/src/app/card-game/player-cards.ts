import { Card } from './card';

export class PlayerCards {
    onHand: Card[] = [];
    tableCardsFaceDown: Card[] = [];
    tableCardsFaceUp: Card[] = [];

    addCard(card: Card) {
        this.onHand.push(card);
        this.sort();
    }

    addCards(cards: Card[]) {
      this.onHand = this.onHand.concat(cards);
      this.sort();
  }

    sort() {
        this.onHand.sort(this.compare);
        this.tableCardsFaceUp.sort(this.compare);
    }

    findCard(playedCard: number) {
      if(this.onHand.length > 0) {
        return this.onHand.find(c => c.value === playedCard);
      }

      else if(this.tableCardsFaceUp.length > 0) {
        return this.tableCardsFaceUp.find(c => c.value === playedCard);
      }

      else {
        return this.tableCardsFaceDown.find(c => c.value === playedCard);
      }
    }

    getCards() {
      if(this.onHand.length > 0) {
        return [ ...Array(51 - this.onHand.length).keys() ].map( i => 0).concat(this.onHand.map(c => c.value));
      }
      else if (this.tableCardsFaceUp.length > 0) {
        return [ ...Array(51 - this.tableCardsFaceUp.length).keys() ].map( i => 0).concat(this.tableCardsFaceUp.map(c => c.value));
      }

      return [];
    }

    removeCard(card: Card) {
      if(this.onHand.length > 0) {
        const index = this.onHand.indexOf(card);
        this.onHand.splice(index, 1);
      }

      else if(this.tableCardsFaceUp.length > 0) {
        const index = this.tableCardsFaceUp.indexOf(card);
        this.tableCardsFaceUp.splice(index, 1);
      }  

      else if(this.tableCardsFaceDown.length > 0) {
        const index = this.tableCardsFaceDown.indexOf(card);
        this.tableCardsFaceDown.splice(index, 1);
      }
      
      this.sort();
    }

    compare(a: Card, b: Card) {
        if ( a.value < b.value ){
          return -1;
        }
        if ( a.value > b.value ){
          return 1;
        }
        return 0;
      }
}