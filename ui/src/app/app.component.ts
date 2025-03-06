import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { GameComponent } from './card-game/game.component';
import { HttpClientModule } from '@angular/common/http';

@Component({
  standalone: true,
  imports: [RouterModule, GameComponent, HttpClientModule],
  selector: 'idiot-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent {
}
