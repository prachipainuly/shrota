import { CircularProgress } from '@mui/material';
import React, { useEffect, useState } from 'react'
import { api } from '../api';
import { useGameContext, useUpdateGame } from '../contexts/GameContext'
import MPHands from './MPHands';
import Timer from './Timer';

const GameArea = () => {

    const gameContext = useGameContext()
    const updateGameContext = useUpdateGame()
    const [ state, setState ] = useState({
        loadingResults: false,
        newWordTimerRunning: false,
        // resultsTimerRunning: false,
    })

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
            <MPHands />
            {gameContext.gameRunning && state.loadingResults &&
                <CircularProgress />
            }
            {gameContext.gameRunning && state.newWordTimerRunning && 
                <spam>Next word: {gameContext.words[gameContext.currentWord]}</spam>
            }
            {gameContext.gameRunning && 
                !state.newWordTimerRunning &&
                    <>
                        {updateGameContext({...gameContext, runCamera: true})}
                        <Timer duration={5} onFinish={() => {
                            updateGameContext({...gameContext, runCamera: false})
                            setState({...state, newWordTimerRunning: true})
                        }} />
                    </>
            }
            {!gameContext.gameRunning && 
                <spam>Game not running. Press Play to start a new game</spam>
            }
        </div>
    )
}

export default GameArea