import React from "react";
import Problem from "./Problem";
function LeftPanel(){
    return(
        <div className="">
            <div className=" ml-[2rem]  w-[15rem] h-[34rem] rounded-lg flex items-center justify-center" style={{ backgroundColor: '#151F7E' }}>
                <div>
                    <h2 className="text-2xl ml-2 text-white">Личный кабинет</h2>

                    <div className="mt-4 ml-2 ">
                        <div className="flex flex-col text-white mb-2">
                            <span className="text-[1.3rem]">ФИО:</span>
                            <span>Иванов И.И.</span>
                        </div>
                        <div className="flex flex-col text-white mb-2 ">
                            <span className="text-[1.3rem]">Контакты:</span>
                            <span>+79515288888</span>
                        </div>
                        <div className="flex flex-col text-white mb-2">
                            <span className="text-[1.3rem]">Статус:</span>
                            <span>Активист</span>
                        </div>
                        <div className="Problems flex flex-col ">
                        <span className="text-[1.3rem] text-white mb-2">Решенные проблем:</span>
                            <div className="Problems overflow-auto overflow-x-hidden h-[15rem]">
                            <Problem/>
                            <Problem/>
                            <Problem/>
                            </div>
                            </div>
                    </div>

                </div>
            </div>

        </div>
    );

}

export default LeftPanel;
