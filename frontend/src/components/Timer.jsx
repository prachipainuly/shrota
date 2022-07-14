import { CircularProgressbar } from 'react-circular-progressbar';
import 'react-circular-progressbar/dist/styles.css';
import React from 'react'
import { api } from '../api';
import { useGameContext, useUpdateGame } from '../contexts/GameContext'
function Timer(){
    const gameContext = useGameContext();
    const updateGameContext = useUpdateGame();
    const [seconds, setSeconds] = React.useState(10);
    React.useEffect(() => {
            
            if (gameContext.gameRunning==false) {    
                setSeconds(10)
            }
            if((seconds===1)&&(gameContext.gameRunning==true)){
                setSeconds(gameContext.message1);
            }
            if ((seconds > 0)&&(gameContext.gameRunning===true)) {
              setTimeout(() => setSeconds(seconds - 1), 1000);
            } else if(seconds==0)  {
              updateGameContext({...gameContext, currentWord: gameContext.currentWord+1})
              setSeconds(10);

            }
        if(gameContext.words.length<gameContext.currentWord){
            gameContext.gameRunning=false;
        }
            
            
        }
          );
    return(
<div>
 
<CircularProgressbar seconds={seconds} 
maxValue={seconds}
value= {seconds}
text={`${seconds }`} />;
</div> 

    )
}
export default Timer;
