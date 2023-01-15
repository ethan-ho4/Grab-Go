import React, { useState } from "react";
import logo from './logo2.jpg'
import './App.css';

function App() {
  const testData = [
    'test1', 'test2', 'test3'
  ]

  const handleDivClick = (event, value) => {
    console.log(value);
    setBigDiv(<div style={{
    }}>
      This is a test div
    </div>)

  }

  const handleClick = (event) => {
    console.log(textValue);
    // DO API CALL HERE
    // fetch
    // .then((data) => {
      const tempArray = [];
      testData.forEach((value) => {
        tempArray.push(
        <div key={value} onClick={event => handleDivClick(event, value)}>
          {value}
        </div>)
      })
      setTestDivs(tempArray);
    // })
  }

  const handleChange = (event) => {
    setTextValue(event.target.value);
  }

  const [textValue, setTextValue] = useState('Write grocery list here');
  const [testDivs, setTestDivs] = useState([]);
  const [bigDiv, setBigDiv] = useState('');

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
                          value={textValue}
                          onChange={handleChange}
                          style={{
                          position: "absolute",
                          left: "20px",
                          top: "150px",
                          height: "200px",
                          width: "290px",
                          resize: "none",
                          }}> Write grocery list here
                        </textarea>
                        <button onClick={handleClick} style={{position: "absolute",
                          left: "255px",
                          top: "360px",
                          height: "30px",
                          width: "60px",}}>Submit</button>
                          <div style={
                            {
                              position: "absolute",
                              // padding: "200px"
                            }
                          }>
                          </div>
                          {testDivs}
                          {bigDiv}

                        
      </div>
            </div>
              <iframe style = {{float: "right", width: "1100px", height: "745px"}}src="https://my.atlistmaps.com/map/29e4bf78-1973-4f74-98ec-20c1d91e85b7?share=true" allow="geolocation" width="100%" height="400px" frameborder="0" scrolling="no" allowfullscreen></iframe>
            </div>
  );
}


export default App;


