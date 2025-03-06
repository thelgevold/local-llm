export class Card {
    
    imagePath: string;

    constructor(public value: number, public suite: string|undefined) {
        this.imagePath = `assets/card-images/${value}_of_${suite}.png`;
    }
}