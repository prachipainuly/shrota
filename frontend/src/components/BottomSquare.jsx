import { Button, TextField } from '@mui/material';
import React, { } from 'react'
import { useState } from 'react';
import { api } from '../api';
import { useGameContext, useUpdateGame } from '../contexts/GameContext';

const BottomSquare = () => {

    const gameContext = useGameContext()
    const updateGameContext = useUpdateGame()
    const [name, setName] = useState('')

    const handleSendResults = () => {
        const body = {name, score: gameContext.totalScore}
        api.post('add_user/', body).then(
            updateGameContext({...gameContext, askNickname: false, totalScore: 0})
        ).catch(function(error){
            updateGameContext({...gameContext, askNickname: false, totalScore: 0})
        })
    }
    
    const handleSkipClick = () => {
        updateGameContext({...gameContext, askNickname: false, totalScore: 0})
    }

    const handleChange = (event) => {
        setName(event.target.value)
    }

    return (
        <div style={{
            backgroundColor: '#dad9cf',
            border: `5px solid #b3af87`,
            width: '99%',
            height: '18vh',
            display: 'flex',
            justifyContent: 'space-evenly',
            fontSize: '2rem', 
            fontWeight: 'bold'
        }}>
                {gameContext.gameRunning &&
                    <div style={{
                        display: 'flex',
                        flexDirection: 'column',
                        alignItems: 'center',
                        justifyContent: 'space-evenly'
                    }}>
                        <p style={{textDecoration: 'underline'}}>{gameContext.bottomText}</p>
                    </div>}
                {gameContext.askNickname ? 
                    <div style={{
                        fontSize: '1.5rem', 
                        textAlign: 'center', 
                        display: 'flex', 
                        flexDirection: 'column', 
                        justifyContent: 'space-around',
                        margin: '0%'
                        }}>
                        <p>Your final score: {gameContext.totalScore}</p>
                        <div>
                            <p>To join the leaderboard, fill in a nickname below</p>
                        </div>
                        <div style={{display: 'flex', justifyContent: 'space-around'}}>
                            <TextField id='name' value={name} onChange={handleChange} variant='standard' autoComplete='off' />
                            <Button variant='contained' color='warning' onClick={handleSendResults}>Send Results</Button>
                            <Button variant='outlined' color='inherit' onClick={handleSkipClick}>No, thanks</Button>
                        </div>
                    </div>
                :   
                    !gameContext.gameRunning && <p style={{alignSelf: 'center'}}>Press Play to start the game!</p>}
        </div>
    )
}

export default BottomSquare