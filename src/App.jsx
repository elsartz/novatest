import { useState } from 'react'
import Notes from './components/Notes'
import AddNote from './components/AddNote'

import './App.css'

function App() {
  

  return (
    <div className="App">
      <div>
        
      </div>
      <h1>Welcome</h1>
      <div className="card">
        <AddNote/>
        <Notes/>

      </div>
      
    </div>
  )
}

export default App
