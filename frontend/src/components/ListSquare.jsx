import React, { useEffect, useState } from 'react'

const ListSquare = (props) => {

    const [state, setState] = useState({});

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
        <div className="content-wrapper" style={{margin: '5%'}}>
            <p style={{fontSize: '2rem', fontWeight: 'bold'}}>{state.title}</p>
            {state.list && state.list.map(s => <p key={s} style={{margin: '3% 0%', fontSize: '1.2rem'}} >{s}</p>)}
        </div>
    </div>
  )
}

export default ListSquare