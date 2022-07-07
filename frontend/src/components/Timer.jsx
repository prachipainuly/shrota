import { CircularProgressbar } from 'react-circular-progressbar';
import 'react-circular-progressbar/dist/styles.css';
import React from 'react';
import { useGameContext, useUpdateGame } from '../contexts/GameContext'

function Timer(){
    const gameContext = useGameContext();
    const updateGameContext = useUpdateGame();
    const starttime=5
    const [seconds, setSeconds] = React.useState(starttime);
    React.useEffect(() => {

        if (gameContext.gameRunning==false) {    
        setSeconds('5')
        
    }

        if(seconds==1){
            setSeconds('cheese');
        }
        if ((seconds > 0)&&(gameContext.gameRunning==true)) {
          setTimeout(() => setSeconds(seconds - 1), 1000);
        } else if(seconds==0)  {
          setSeconds('timeupp!');
        }});
    return(
<div>
 
<CircularProgressbar seconds={seconds} 
maxValue={seconds}
value= {seconds}
text={`${seconds }`}
 />;
</div> 

    )
}
export default Timer;