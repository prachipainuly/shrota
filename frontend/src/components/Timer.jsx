import { CircularProgressbar } from 'react-circular-progressbar';
import 'react-circular-progressbar/dist/styles.css';
import React from 'react';
import { useGameContext } from '../contexts/GameContext'
function Timer(props){
    const gameContext = useGameContext();
    const [seconds, setSeconds] = React.useState();
    
    const [onFinish, setOnFinish] = React.useState();

    React.useEffect(() => {
        setSeconds(props.duration)
        setOnFinish(props.onFinish)

        if (seconds > 0) { // CHECK THIS PART
          setTimeout(() => setSeconds(seconds - 1), 1000);
        } else if(seconds===0)  {
          onFinish()
        }}
    );
    
    return(
        <div>
            <CircularProgressbar
                seconds={seconds} 
                maxValue={seconds}
                value= {seconds}
                text={`${seconds }`}
            />
        </div> 

    )
}
export default Timer;