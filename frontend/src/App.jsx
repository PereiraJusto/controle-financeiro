import { useEffect, useState } from 'react'

function App() {
  const [status, setStatus] = useState('carregando...')

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/health/')
      .then(response => response.json())
      .then(data => {
        setStatus(data.status)
      })
      .catch(error => {
        console.error(error)
        setStatus('erro')
      })
  }, [])

  return (
    <div>
      <h1>Controle Financeiro</h1>
      <p>Status do backend: {status}</p>
    </div>
  )
}

export default App
