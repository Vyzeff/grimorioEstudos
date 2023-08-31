import React, { Component } from "react";
import Game from "./Game";

export default class Home extends Component {
  render() {
    return <Game randChoiceNum={6} />;
  }
}
