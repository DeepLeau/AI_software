import React from 'react';
import { RiMenu3Line, RiCloseLin } from 'react-icons/ri'
import './navbar.css'
import logo from '../../assets/logo.png'

const Navbar = () => {
  return (
    <div className='nvemo__navbar'>
        <div className='nvemo__navbar-links'>
          <div className='nvemo__navbar-links_logo'>
            <img src={logo} alt="logo" />
          </div>
        </div>
    </div>
  )
}

export default Navbar