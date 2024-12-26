import {
PasswordInput,
PasswordStrengthMeter,
} from "@/components/ui/password-input"
import { useState } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
      <PasswordInput />
      
      <h1 className="text-3xl font-bold underline">
      Hello world!
    </h1>
      <PasswordStrengthMeter />
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
