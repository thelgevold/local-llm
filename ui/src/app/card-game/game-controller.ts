import { HttpClient } from '@angular/common/http';
import { PlayerCards } from './player-cards';
import { Card } from './card';
import { CardDeck } from './card-deck';

export class GameController {
    currentPlayerIndex = 0;
    cardsPlayed: Card[] = [];
    players: PlayerCards[] = [];
    cardDeck: CardDeck = new CardDeck();
    currentCard: Card;
    winner = -1;

    constructor(private httpClient: HttpClient) {}

    async startGame() {
        this.players.push(this.cardDeck.dealHand());
        this.players.push(this.cardDeck.dealHand());

        if(this.players[1].onHand[0].value < this.players[0].onHand[0].value) {
            this.currentPlayerIndex = 1;
            await this.computerPlay();
        }
    }

    async computerPlay() {
        await this.sleep(1000);

        let onHand = this.players[this.currentPlayerIndex].getCards();

        let mostRecentCard = [0];

        if(this.cardsPlayed.length > 0) {
            mostRecentCard = [this.cardsPlayed[this.cardsPlayed.length - 1].value];
        }

        let cards = mostRecentCard.concat(onHand);
        let playedCardPayload: any = await this.httpClient.post('/api/next_card_play', cards).toPromise();
        let playedCard = JSON.parse(playedCardPayload);
      
        if(playedCard === 0) {
            this.pullPile(0);
            return;
        }

        let foundCard = this.players[this.currentPlayerIndex].findCard(playedCard);

        if(!foundCard) {
            console.log(cards);
            throw Error('Invalid play ' + playedCard);
        }

        this.drawCard(foundCard);

        this.currentCard = foundCard;
        this.cardsPlayed.push(foundCard);

        if(foundCard.value === 10) {
            await this.sleep(1000);
        }

        let removed = this.updatePile(foundCard);

        let winner = this.checkIfWinner();

        if(winner) {
            return;
        }

        if(removed) {
            this.computerPlay();
            console.log('Computer played a 10');
            return;
        }
     
        this.currentPlayerIndex = 0;
    }

    sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
     }

    humanPlay(card: Card, round: number) {
        if(this.currentPlayerIndex !== 0) {
            return;
        }

        if(round == 1){
            if(this.players[this.currentPlayerIndex].onHand.length > 0) {
                return;
            }
        }

        if(round == 2){
            if(this.players[this.currentPlayerIndex].tableCardsFaceUp.length > 0) {
                return;
            }
        }

        let valid = this.isValidPlay(card);

        if(!valid) {
            return;
        }

        this.currentCard = card;
        this.cardsPlayed.push(card);
        this.drawCard(card);
        
        let removed = this.updatePile(card);
        
        let winner = this.checkIfWinner();

        if(winner) {
            return;
        }

        if(removed) {
            return;
        }

        this.currentPlayerIndex = 1;
        this.computerPlay();
    }

    async pullPile(currentPlayerIndex) {
        this.players[this.currentPlayerIndex].addCards(this.cardsPlayed);
        this.cardsPlayed = [];
        this.currentCard = null;

        this.currentPlayerIndex = currentPlayerIndex;

        if(this.currentPlayerIndex === 1) {
            await this.computerPlay();
        }
    }

    updatePile(card: Card) {
        if(card.value === 10) {
            this.cardsPlayed = [];
            this.currentCard = null;
            return true;
        }

        if(this.cardsPlayed.length >= 4) {
            let index = this.cardsPlayed.length - 1;
            
            let allSame = card.value === this.cardsPlayed[index].value && 
                          card.value === this.cardsPlayed[index - 1].value &&
                          card.value === this.cardsPlayed[index - 2].value &&
                          card.value === this.cardsPlayed[index - 3].value;

            if(allSame) {
                this.cardsPlayed = [];
                this.currentCard = null;
                console.log('4 of a kind');
                return true;
            }
        }

        return false;
    }

    drawCard(card: Card) {
        this.players[this.currentPlayerIndex].removeCard(card);

        if(this.cardDeck.cards.length > 0 && this.players[this.currentPlayerIndex].onHand.length <= 2) {
            this.players[this.currentPlayerIndex].addCard(this.cardDeck.drawCard());
        }
    }

    isValidPlay(card: Card) {
        if(this.cardsPlayed.length > 0) {
            let mostRecentCard = this.cardsPlayed[this.cardsPlayed.length - 1];

            if(card.value === 2 || card.value === 10) {
                return true;
            }

            if(card.value < mostRecentCard.value) {
                return false;
            }
        }

        return true;
    }

    checkIfWinner() {
        if(this.players[this.currentPlayerIndex].onHand.length === 0 && this.players[this.currentPlayerIndex].tableCardsFaceUp.length === 0) {
            this.winner = this.currentPlayerIndex;
            return true;
        }

        return false;
    }
}