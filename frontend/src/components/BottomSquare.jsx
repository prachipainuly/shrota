import React, { useEffect, useState } from 'react'
import { useGameContext } from '../contexts/GameContext';

const BottomSquare = () => {

    const [score, setScore] = useState(0)
    const gameContext = useGameContext()

    useEffect(() => {
        setScore(score => score + gameContext.scoreLastRound)
    }, [gameContext.scoreLastRound])
    

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
                {gameContext.gameRunning ? 
                    <div style={{
                        display: 'flex',
                        flexDirection: 'column',
                        alignItems: 'center',
                        justifyContent: 'space-evenly'
                    }}>
                        <p style={{textDecoration: 'underline'}}>Word: {gameContext.currentWord}</p>
                        <p>Your current score: {score}</p>
                    </div> :
                    <p style={{alignSelf: 'center'}}>Press Play to start the game!</p>
                }
        </div>
    )
}

export default BottomSquare