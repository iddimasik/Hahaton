import React from "react";

function AddProblem(){
    return(
        <div className="pt-[0.5rem]" >
            <div className="mt-[1rem] ml-[1rem]  w-[14rem] h-[34rem] rounded-lg flex items-center justify-center" style={{ backgroundColor: '#151F7E' }}>
                <button>
                    <img className="w-[5rem] h-[5rem] " src={require("../img/add.png")} alt="icon"/>
                    <span className="flex items-center justify-center text-2xl w-[5rem] mt-[0.5rem] text-white">Добавить проблему</span>
                </button>
            </div>

        </div>
    );

}

export default AddProblem;
