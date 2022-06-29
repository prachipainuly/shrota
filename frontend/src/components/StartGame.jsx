import React from 'react'

const StartGame = () => {
  return (
    <div style={{
        backgroundColor: '#ffee00',
        border: `5px solid #000000`,
        width: '97%',
        height: '18vh',
        cursor: 'pointer',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center'
    }}>
        <p style={{fontSize: '2rem', fontWeight: 'bold', margin: '0 2% 2% 0'}}>Play</p>
    </div>
  )
}

export default StartGame