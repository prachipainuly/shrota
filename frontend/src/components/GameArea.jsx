import React, { useState } from 'react'

const GameArea = () => {

    const [state, setState] = useState({
        gameStarted: false
    });

    return (
        <div style={{
            backgroundColor: 'white',
            height: '50vh',
            width: '100vh'
        }}>
        </div>
    )
}

export default GameArea