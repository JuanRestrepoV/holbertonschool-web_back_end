// 5-building.js

export default class Building {
  constructor(sqft) {
    if (new.target !== Building) {
      this.evacuationWarningMessage();
    }
    this.sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(val) {
    this._sqft = val;
  }

  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}