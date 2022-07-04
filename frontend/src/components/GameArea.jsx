import React, { useEffect, useState } from 'react'
import { api } from '../api';
import { useGameContext, useUpdateGame } from '../contexts/GameContext'
import MPHands from './MPHands';

const GameArea = () => {

    const gameContext = useGameContext()
    const updateGameContext = useUpdateGame()

    useEffect(() => {
      api.get('get_word')
        .then(res => {
            updateGameContext({...gameContext, currentWord: res.data.name})
        }).catch(function(error) {
            updateGameContext({...gameContext, currentWord: 'error'})
        })
    }, [gameContext.scoreLastRound])

    return (
        <div style={{
            backgroundColor: 'white',
            height: '50vh',
            width: '70vh'
        }}>
            {console.log(gameContext.gameRunning)}
            {gameContext.gameRunning && 
                <MPHands />
            }
            {!gameContext.gameRunning && 
                <spam>Game not running. Press Play to start a new game</spam>
            }
        </div>
    )
}

export default GameArea