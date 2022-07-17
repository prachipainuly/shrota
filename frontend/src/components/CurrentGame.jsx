import React, { useEffect, useState } from 'react'
import { api } from '../api'
import { useGameContext } from '../contexts/GameContext'
import ListSquare from './ListSquare'

const CurrentGame = () => {

  const [ words, setWords ] = useState()
  const gameContext = useGameContext()

  useEffect(() => {
    if(!words && gameContext.words.length > 0){
      const w = []
      gameContext.words.map(word => {
        w.push({key: word, value: 'Not played'})
      })

      setWords(w)
    }

    if(gameContext.scoreLoading){
      // setWords()
    }
  }, [gameContext.words, gameContext.scoreLoading])

  useEffect(() => {
    if(!gameContext.gameRunning){
      setWords()
    }
  }, [gameContext.gameRunning])
  
    
  return (
    <ListSquare 
        list={words ? words : [{key: 'The information about your game will be here!'}]}
        title="Current game" 
        color="#ddc7ff"
        borderColor="#7b6492"
        width="18%"
        heigth="70vh"
        />
  )
}

export default CurrentGame