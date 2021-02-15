import React, { Component } from "react";

class Header extends Component {
  render() {
    return (
      <div className="text-center">
        <img
          src="https://miro.medium.com/max/700/1*wzxBpEqhB-8WT5BdsHQ9Qg.png"
          width="300"
          className="img-thumbnail"
          style={{ marginTop: "20px" }}
        />
        <hr />
        <h5>
          <i>Project</i>
        </h5>
        <h1>Student Mangement System React + Django</h1>
      </div>
    );
  }
}

export default Header;