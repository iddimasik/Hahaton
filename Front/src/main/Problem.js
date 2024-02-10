import React from "react";

function Problem(){
    return(
        <div>
            <div className="flex flex-col text-white mb-2">
                <div className="h-[6rem] rounded-[1rem] w-[13rem] flex justify-center" style={{backgroundColor: '#D3EEFF'}}>
                    <div>
                        <span className="Heading  text-black">Заголовок</span>
                        <div>
                            <button className="flex flex-row gap-[1rem] ">
                                <img className="w-[1.5rem] h-[1.5rem] " src={require("../img/map.png")} alt="icon"/>
                                <span className="Region text-black ">Регион</span>
                            </button>
                            <div className="flex flex-row gap-2">
                                <div className="Date text-black"> 22.01.2024</div>
                                <div className="Name text-black"> Иванов И.И.</div>
                            </div>
                        </div>
                        <div className="Status text-black"> Статус</div>

                    </div>

                </div>
            </div>
        </div>
    );
}

export default Problem;