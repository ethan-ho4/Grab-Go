import React, { useState } from "react";
import logo from './logo2.jpg'
import './App.css';

function App() {
  return (
    <div className="App">
      <div>
        <img
          src={require("./logo2.jpg")}
          style={{
          position: "absolute",
          width: "250px",
          height: "125px",
          top: "5px",
           left: "20px",
           }}
         />
      <div>     
        
                        <textarea id = "textarea"
                          style={{
                          position: "absolute",
                          left: "20px",
                          top: "150px",
                          height: "200px",
                          width: "290px",
                          resize: "none"
                          }}> Write grocery list here
                        </textarea>
                        <button style={{position: "absolute",
                          left: "255px",
                          top: "360px",
                          height: "30px",
                          width: "60px",}}>Submit</button>

                        
      </div>
            </div>
              <iframe style = {{float: "right", width: "1100px", height: "745px"}}src="https://my.atlistmaps.com/map/29e4bf78-1973-4f74-98ec-20c1d91e85b7?share=true" allow="geolocation" width="100%" height="400px" frameborder="0" scrolling="no" allowfullscreen></iframe>
            </div>
  );
}


export default App;


