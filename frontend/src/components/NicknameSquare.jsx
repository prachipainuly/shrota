import React, { useState } from 'react'

const NicknameSquare = () => {

    const [nickname, setNickname] = useState("");

    return (
        <div style={{
            backgroundColor: '#dad9cf',
            border: `5px solid #b3af87`,
            width: '99%',
            height: '18vh'
        }}>
            <div className="content-wrapper" style={{margin: '5%'}}>
                <p style={{fontSize: '2rem', fontWeight: 'bold'}}>Enter your nick name to begin:</p>
                
            </div>
        </div>
    )
}

export default NicknameSquare