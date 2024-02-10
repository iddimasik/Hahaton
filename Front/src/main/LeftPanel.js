import React from "react";

function LeftPanel(){
    return(
        <div className="pt-[2rem]" >
            <div className="mt-[1rem] ml-[1rem]  w-[17rem] h-[34rem] rounded-lg flex items-center justify-center" style={{ backgroundColor: '#151F7E' }}>
                <div >
                    <h2 className="text-2xl text-white">Личный кабинет</h2>

                    <div className="mt-4 ">
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
                    </div>

                </div>
            </div>

        </div>
    );

}

export default LeftPanel;
