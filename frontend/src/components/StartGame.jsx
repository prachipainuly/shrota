import React from 'react'
import { api } from '../api';
import { useGameContext, useUpdateGame } from '../contexts/GameContext'
import Timer from './Timer';
const StartGame = () => {

  const gameContext = useGameContext();
  const updateGameContext = useUpdateGame();

  const handleOnClick = () => {
    gameContext.gameRunning ? 
      updateGameContext({gameRunning: false})
      :
      (
        api.get('get_random_alphabets')
          .then(res => {
            updateGameContext({...gameContext, words: res.data, gameRunning: true, currentWord: 0})
          })
          .catch(function(error) {
            console.log('Error getting the list of words. Hardcoded list applied.')
            updateGameContext({...gameContext, words: ['A', 'B', 'C'], gameRunning: true, currentWord: 0})
          })
      )
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
    </div>
  )
}

export default StartGame