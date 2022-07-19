import { CircularProgressbar } from 'react-circular-progressbar';
import 'react-circular-progressbar/dist/styles.css';
import React from 'react'
import { useGameContext, useUpdateGame } from '../contexts/GameContext'
function Timer(){
    const gameContext = useGameContext();
    const updateGameContext = useUpdateGame();
    const [seconds, setSeconds] = React.useState(3);

    React.useEffect(() => {
        if(gameContext.gameRunning===true){

            /**
             * MPHands is responsible for managing the 'scoreLoading', since it accesses the backend
             * When the MPHands finishes loading the score from the backend, it sets scoreLoading to false and showScore to true.
             */
            if(gameContext.scoreLoading){
                console.log("Entrou no results loading")
                updateGameContext({...gameContext, bottomText: "Loading results..."})
            }

            /**
             * When the showScore variable is true, the timer waits in this stage for 3 seconds.
             * Once 3 seconds passed, it sets showScore to false and showNextWord to true, in order to continue the game flow.
             */
            if(gameContext.showScore){
                console.log("Entrou no show score")
                setTimeout(() => {
                    updateGameContext({...gameContext, showScore: false, showNextWord: true})
                }, 3000);
            }
            
            /**
             * When the showNextWord variable is true, it checks if all the words were already played.
             * If yes, it will update the game running for false, since there are no more words.
             * If no, the next word will be displayed.
             */
            if(gameContext.showNextWord){
                console.log("Entrou no show next word")
                if(gameContext.words && gameContext.words.length===gameContext.currentWord+1){
                    updateGameContext({...gameContext, gameRunning:false, currentWord: 0});
                } else {
                    updateGameContext({...gameContext, bottomText: `The next word will be ${gameContext.words[gameContext.currentWord+1]}`})
                    setTimeout(() => {
                        updateGameContext({...gameContext, showNextWord: false, currentWord: gameContext.currentWord+1})
                        setSeconds(5)
                    }, 3000);
                }
            }

            if(!gameContext.scoreLoading && !gameContext.showScore && !gameContext.showNextWord){
                console.log(seconds)
                if (seconds > 0) {
                    updateGameContext({
                        ...gameContext, 
                        bottomText: `The current word is ${gameContext.words[gameContext.currentWord]}.\nSeconds remaining: ${seconds}`,
                        catchFrame: seconds===1
                    })
                    setTimeout(() => setSeconds(seconds - 1), 1000);
                } else {
                    console.log("send frame true")
                    updateGameContext({...gameContext, catchFrame: false, sendFrame: true})
                }
            }
        }
    }, [seconds, updateGameContext.scoreLoading, gameContext.showScore, gameContext.gameRunning, gameContext.showNextWord]);

    React.useEffect(() => {
        if(gameContext.gameRunning===false){
            setSeconds(3)
        }
    }, [ gameContext.gameRunning ])

    return(
        <div>
            {/* <CircularProgressbar
            maxValue={gameContext.showNextWord === true ? 3 : 5}
            value= {seconds}
            text={`${seconds}`} /> */}
        </div> 
    )
}
export default Timer;
