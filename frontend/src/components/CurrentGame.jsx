import React, { useEffect, useState } from 'react'
import { useGameContext } from '../contexts/GameContext'

const CurrentGame = () => {

  const [ words, setWords ] = useState()
  const gameContext = useGameContext()

  useEffect(() => {
    if(!words && gameContext.words.length > 0){
      const w = []
      gameContext.words.map(word => {
        w.push(
          <div style={{display: 'flex', justifyContent: 'space-between'}}>
            <p style={{margin: '3% 0%', fontSize: '1.2rem'}}>{word}</p>
            <p style={{margin: '3% 0%', fontSize: '1.2rem'}}>Not played</p>
          </div>
        )
      })

      setWords(w)
    }

  }, [gameContext.words])

  useEffect(() => {
    if(gameContext.showScore){
      const temp = words
      temp[gameContext.currentWord] = 
        <div style={{display: 'flex', justifyContent: 'space-between'}}>
          <p style={{margin: '3% 0%'}}>{gameContext.words[gameContext.currentWord]}</p>
          <p style={{margin: '3% 0%', color: gameContext.scoreLastRound > 0 ? '#008000' : '#FF0000'}}>
            {gameContext.scoreLastRound > 0 ? `MATCHED (${gameContext.scoreLastRound})` : 'NOT MATCHED'}
          </p>
        </div>
      setWords(temp)
    } 
  }, [gameContext.showScore])
  

  useEffect(() => {
    if(!gameContext.gameRunning){
      setWords()
    }
  }, [gameContext.gameRunning])
  
    
  return (
    <div style={{
      backgroundColor: `#ddc7ff`,
      border: `5px solid #7b6492`,
        width:"18%",
        heigth:"70vh"
    }}>
        <div style={{margin: '5%'}}>
            <p style={{fontSize: '2rem', fontWeight: 'bold', marginBottom: '5%'}}>Current game</p>
                <div style={{display: 'flex', flexDirection: 'column', justifyContent: 'space-between', fontSize: '1.2rem'}}>
                    {words ? words : 'The information about your game will be here!'}
                </div>
        </div>
    </div>
  )
}

export default CurrentGame