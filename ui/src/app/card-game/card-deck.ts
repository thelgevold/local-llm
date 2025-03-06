import { Card } from './card';
import { PlayerCards } from './player-cards';
export class CardDeck {
    public cards: Card[] = [];

    constructor() {
        this.cards = this.cards.concat(this.createCards('clubs'))
        .concat(this.createCards('diamonds'))
        .concat(this.createCards('hearts'))
        .concat(this.createCards('spades'));
     
        this.shuffle(this.cards);
    }

    private createCards(suit: string) {
        let cards:Card[] = [];
        
        for(let i = 2; i < 15; i++) {
            cards.push(new Card(i, suit));
        }

        return cards;
    }

    public dealHand() {
        let cards = new PlayerCards();
        
        cards.tableCardsFaceUp = this.cards.splice(0, 3);
        cards.tableCardsFaceDown = this.cards.splice(0, 3);
        cards.onHand = this.cards.splice(0, 3);
        
        cards.sort();

        return cards;
    }

    public drawCard() {
        return this.cards.splice(0, 1)[0];
    }

    private shuffle(cards: Card[]) {
        let currentIndex = cards.length,  randomIndex;
      
        while (currentIndex != 0) {
      
          randomIndex = Math.floor(Math.random() * currentIndex);
          currentIndex--;
      
          [cards[currentIndex], cards[randomIndex]] = [cards[randomIndex], cards[currentIndex]];
        }
      }
}