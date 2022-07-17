import React, { useState } from 'react'
import ListSquare from './ListSquare';

const Ranking = () => {

    const [state, setState] = useState({
        list: [{key: "xyrex123", value: "300 pts."}, {key: "profitpainuly", value: "289 pts."}, {key: "dexamps", value: "113 pts."}],
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