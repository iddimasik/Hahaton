import React from "react";
import Problem from "./Problem";

function End(){
    return (
        <div>
            <div className="pt-[0.5rem]">
                <div className="mt-[1rem]   w-[19rem] h-[38rem] rounded-lg flex  justify-center"
                     style={{backgroundColor: '#151F7E'}}>
                    <div className="flex flex-col">
                        <h1 className="text-white mt-2 text-2xl">Завершено</h1>
                        <div className="Problems flex flex-col mt-2 items-center mb-2 overflow-x-hidden overflow-auto">
                            <Problem/>
                            <Problem/>
                            <Problem/>
                            <Problem/>
                            <Problem/>
                            <Problem/>

                        </div>
                    </div>

                </div>

            </div>
        </div>
    );
}

export default End;