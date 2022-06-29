import React, { useEffect, useState } from 'react'
import ListSquare from './ListSquare';

const Ranking = () => {

    const [state, setState] = useState({
        list: ["xyrex123 : 300 pts.", "profitpainuly : 289 pts.", "dexamps : 113 pts."],
        title: "Ranking",
        color: "#"
    });

    // useEffect(() => {
    //     /** TODO: request ranking from backend */
    // }, [])
    

    return (
        <ListSquare 
            title="Ranking"
            color="#ffd7d7"
            borderColor="#c76c6c"
            list={state.list}
            width="30vh"
            heigth="50vh"
        />
    )
}

export default Ranking