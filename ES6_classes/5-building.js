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
	/* eslint-disable */
  evacuationWarningMessage() {
    throw TypeError('Class extending Building must override evacuationWarningMessage');
  }
	/* eslint-disable */
}
