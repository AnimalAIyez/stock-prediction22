import React from 'react'
import Button from './Button'
import Header from './Header'
import Footer from './Footer'

const Main = () => {
  return (
    <>
   
    <div className='container'>
        <div className='p-5 text-center bg-light-dark rounded' >
            <h1 className='text-light'>Stock Prediction Site</h1>
            <p className='text-light lead'>A stock prediction site using machine learning</p>
           <Button text="Login" class="btn-outline-info"/>

        </div>

    </div>
   
    
    </>
  )
}

export default Main