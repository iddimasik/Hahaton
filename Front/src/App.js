import './App.css';
import Head from "./main/Head";
import React from "react";
import AddProblem from "./main/AddProblem";
import LeftPanel from "./main/LeftPanel";

function App() {
  return (
      <div className="App ">
          <header>
              <Head/>
          </header>

          <body>

          <div className="h-[92vh] w-screen bg-cover bg-center bg-no-repeat object-cover"
               style={{backgroundImage: `url(${require("./img/back.png")})`}} >
              <div className="flex flex-row gap-1 ">
                  <AddProblem/>
                  <LeftPanel/>
              </div>

          </div>

          </body>

      </div>
  );
}

export default App;
// bg-cover w-screen h-[92.5vh]