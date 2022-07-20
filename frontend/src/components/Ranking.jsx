import React, { useEffect, useState } from 'react'
import { api } from '../api';

const Ranking = () => {

    const [state, setState] = useState({
        list: [],
    });

    useEffect(() => {
        api.get('get_leaderboard/').then(res => setState(state => ({...state, list: res.data})))
    }, [])

    return (
        <div style={{
            backgroundColor: "#ffd7d7",
            border: `5px solid #c76c6c`,
            width: "30vh",
            height: "50vh"
        }}>
            <div style={{margin: '5%'}}>
                <p style={{fontSize: '2rem', fontWeight: 'bold', marginBottom: '5%'}}>Leaderboard</p>
                {state.list && state.list.map(item => 
                    <div style={{display: 'flex', justifyContent: 'space-between'}}>
                        <p style={{margin: '3% 0%', fontSize: '1.2rem'}}>{item.name}</p>
                        <p style={{margin: '3% 0%', fontSize: '1.2rem'}}>{item.score}</p>
                    </div>
                )}
            </div>
        </div>
    )
}

export default Ranking