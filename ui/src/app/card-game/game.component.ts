import { Component } from '@angular/core';
import { CardDeck } from './card-deck';
import { HttpClient } from "@angular/common/http";
import { PlayerCards } from './player-cards';
import { CommonModule } from '@angular/common';
import { Card } from './card';
import { GameController } from './game-controller';

@Component({
  standalone: true,
  imports: [CommonModule],
  selector: 'game',
  templateUrl: './game.component.html',
  styleUrls: ['./game.component.scss'],
})
export class GameComponent {
    gameController: GameController;

    constructor(private httpClient: HttpClient) {
        this.gameController = new GameController(httpClient);
    }

    async ngOnInit() {
      this.gameController.startGame();
    }

    async play(card: Card, round: number) {
        this.gameController.humanPlay(card, round);
    }

    pullPile(currentPlayerIndex) {
        this.gameController.pullPile(currentPlayerIndex);
    }
}
