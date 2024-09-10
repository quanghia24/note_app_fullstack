import React from "react"
import {BrowserRouter, Routes, Route, Navigate} from 'react-router-dom'
import Login from "./pages/Login"
import Home from "./pages/Home"
import NotFound from "./pages/NotFound"
import Register from "./pages/Register"
import ProtectedRoute from './components/ProtectedRoute'

function Logout(){
  localStorage.clear()
  return <Navigate to='/login'/>
}

function RegisterAndLogout(){  
  // clear local storage before submitting another accesstoken to the register root
  localStorage.clear()
  return <Register/>
}

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={ // only able to access Home when youre authenticated
          <ProtectedRoute children={<Home/>}/>
        }/>
        <Route path="/login" element={<Login/>}/>
        <Route path="/logout" element={<Logout/>}/>
        <Route path="/register" element={<RegisterAndLogout/>}/>
        <Route path="*" element={<NotFound/>}/> 
      </Routes>
    </BrowserRouter>
  )
}

export default App
