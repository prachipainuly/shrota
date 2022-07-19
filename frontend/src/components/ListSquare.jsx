import React, { useEffect, useState } from 'react'

const ListSquare = (props) => {

    const [state, setState] = useState({});
    const [ list, setList ] = useState({})

    useEffect(() => {
        setState({
            color: props.color,
            borderColor: props.borderColor,
            title: props.title,
            list: props.list,
            width: props.width,
            heigth: props.heigth
        })
    }, [ props ])

    return (
        <div style={{
            backgroundColor: `${state.color}`,
            border: `5px solid ${state.borderColor}`,
            width: state.width,
            height: state.heigth
        }}>
            <div style={{margin: '5%'}}>
                <p style={{fontSize: '2rem', fontWeight: 'bold', marginBottom: '5%'}}>{state.title}</p>
                {state.list && state.list.map(s => 
                    <div style={{display: 'flex', justifyContent: 'space-between'}}>
                        <p key={s.key} style={{margin: '3% 0%', fontSize: '1.2rem'}}>{s.key}</p>
                        <p key={s.key} style={{margin: '3% 0%', fontSize: '1.2rem'}}>{s.value}</p>
                    </div>
                )}
            </div>
        </div>
    )
}

export default ListSquare