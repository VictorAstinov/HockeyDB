import React from "react"
import { useState } from "react"
import { useNavigate, Link } from "react-router-dom"
import { proxyPrefix, userCookieName, adminCookieName } from "./constant"

export function SignInPageView() {
    const navigate = useNavigate()
    var [usernameTextState, setUserame] = useState("")
    var [passTextState, setPassword] = useState("")
    const handleSubmit = event => {
        event.preventDefault();
        fetch(`${proxyPrefix}api/users/login?username=${usernameTextState}&password=${passTextState}`)
        .then(response => response.json())
        .then(data => {
            if (data['status'] === "OK") {
                fetch(`${proxyPrefix}api/users/${data['id']}`)
                .then(response => response.json())
                .then(userData => {
                    
                    if (userData["is_admin"]) {
                        sessionStorage.setItem(userCookieName, null)
                        sessionStorage.setItem(adminCookieName, data['id'])
                        navigate("/admin-main")
                    } else {
                        sessionStorage.setItem(userCookieName, data['id'])
                        sessionStorage.setItem(adminCookieName, null)
                        navigate("/search-menu")
                    }
                })
            } else {
                alert("Wrong Username or Password")
                console.log(data)
            }
        })
        .catch(err => {
            console.error(err)
        })
    }
    const handlePassChange = (event) => { setPassword(event.target.value) }
    const handleUsernameChange = (event) => { setUserame(event.target.value) }
    
    return (
        <div className="vbox secondaryColor signInBox">
            <form onSubmit={handleSubmit}>
                <input placeholder="User Name" className="signInItem" onChange={handleUsernameChange}/>
                <input type="password" placeholder="Password" className="signInItem" onChange={handlePassChange}/>
                <button type="submit" className="signInItem"> Sign in</button>
            </form>
                <label className="primaryColor signInItem"> Don't have a account  Yet? create one:</label>
            <Link to="/signup">
                <button className="signInItem">
                    Sign up
                </button>
            </Link>
        </div>
    )
}
