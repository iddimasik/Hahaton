import './App.css';
import Head from "./main/Head";
import React from "react";
import AddProblem from "./main/AddProblem";
import LeftPanel from "./main/LeftPanel";
import Queue from "./main/Queue";
import Working from "./main/Working";
import End from "./main/End";
import  "./main/login.css";

function App() {
  return (
      <div className="App ">
          <header>
              <Head/>
          </header>


          <div className="h-[92vh] w-screen bg-cover justify-between bg-center bg-no-repeat object-cover"
               style={{backgroundImage: `url(${require("./img/back.png")})`}} >
              <div className="flex flex-row gap-[3rem] items-center justify-center ">
                  <AddProblem/>
                  <div className="flex flex-row gap-1 items-center justify-center">
                  <Queue/>
                  <Working/>
                  <End/>
                  <LeftPanel/>
                  </div>
              </div>

          </div>



      </div>
  );
}

export default App;
// bg-cover w-screen h-[92.5vh]