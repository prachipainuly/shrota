import React from 'react'
import { useGameContext } from '../contexts/GameContext'
import MPHands from './MPHands';

const GameArea = () => {

    const gameContext = useGameContext()

    return (
        <div style={{
            backgroundColor: 'white',
            height: '50vh',
            width: '70vh'
            
        }}>
            {gameContext.gameRunning && <MPHands />}
            {!gameContext.gameRunning && 
                <spam>Game not running. Press Play to start a new game</spam>
            }
        </div>
    )
}

export default GameArea


// Game start: gamestate ia true
//     gameRunning true
//     for 10 times:
//         3 seconds to show whats the word  timwe 1 : state time is up true
//         5 seconds with camera timer 2 : state time is up true
//         Loading result
//         3 seconds with result timer 3
//     gameRunning false