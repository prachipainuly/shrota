import React from 'react'
import { useGameContext, useUpdateGame } from '../contexts/GameContext'
import Timer from './Timer';
const StartGame = () => {

  const gameContext = useGameContext();
  const updateGameContext = useUpdateGame();

  const handleOnClick = () => {
    gameContext.gameRunning ? 
      updateGameContext({gameRunning: false})
      :
      updateGameContext({gameRunning: true, currentWord: 'Banana'})
  }

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
    }} onClick={handleOnClick}>
      {!gameContext.gameRunning && 
        <p style={{fontSize: '2rem', fontWeight: 'bold', margin: '0 2% 2% 0'}}>Play</p>
      }
      {gameContext.gameRunning && 
        <p style={{fontSize: '2rem', fontWeight: 'bold', margin: '0 2% 2% 0'}}>Exit</p>
      }
      <div style={{
        width:"100px"
      }}> 
        <Timer></Timer>
      </div>
    </div>
  )
}

export default StartGame