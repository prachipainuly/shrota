import React, { useContext, useState } from 'react'

const GameContext = React.createContext()
const UpdateGameContext = React.createContext()

export function useGameContext() {
    return useContext(GameContext)
}

export function useUpdateGame() {
    return useContext(UpdateGameContext)
}

export function GameProvider({ children }){
    const [state, setState] = useState({
        gameRunning: false,
        currentWord: 0,
        scoreLastRound: {},
        catchFrame: false,
        sendFrame: false,
        scoreLoading: false,
        showScore: false,
        showNextWord: false,
        bottomText: ""
    })

    function updateGame(state){
        setState(state)
    }

    return(
        <GameContext.Provider value={state}>
            <UpdateGameContext.Provider value={updateGame}>
                {children}
            </UpdateGameContext.Provider>
        </GameContext.Provider>
    )
}