import React from "react";


function Head() {
    return (
        <div className="flex flex-row justify-between px-[2rem] " style={{ backgroundColor: '#151F7E' }}>
        <h1 className="text-3xl font-bold text-white p-[0.5rem] ">
            TeamSeal
        </h1>
<div className="flex ">
    <div className="flex flex-row  items-center gap-[2rem] ">
        <button>
            <img className="w-[1.5rem] h-[1.5rem] " src={require("../img/ex.png")} alt="icon"/>
        </button>
        <button>
            <img className="w-[1.5rem] h-[1.5rem] " src={require("../img/exit.png")} alt="icon"/>
        </button>

    </div>
</div>
        </div>
);
}

export default Head;