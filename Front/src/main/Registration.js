import React from "react";

function LogIn(){
    return(
        <div>

            <div className="content">
                <form name="f" method="post" action="/process_login"   style={{color: '#D3EEFF'}} >
                    <input type="hidden"  />
                    <h1 className="text-2xl">Регистрация </h1>

                    <div className="container">
                        <label htmlFor="username" className="form-label">Имя пользователя: </label>
                        <input type="text" name="username" id="username" className="form-input"/>
                    </div>
                    <br/>
                    <div className="container">
                        <label htmlFor="password" className="form-label">Пароль: </label>
                        <input type="password" name="password" id="password" className="form-input"/>
                        <br/>
                    </div>

                    <div className="login-button">
                        <input type="submit" value="Login" className="log"/>
                    </div>

                    <div  style={{color: 'red'}}>
                        Имя или пароль уже существует
                    </div>
                </form>

            </div>
        </div>
    );
}

export default LogIn;