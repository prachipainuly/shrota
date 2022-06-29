import React from 'react'
import ListSquare from './ListSquare'

const Categories = () => {

    const categories = [
        "Fruits",
        "Nature",
        "Food",
        "Greetings",
        "Animals",
        "Sports",
        "Drinks",
        "Country Names",
    ]
    
  return (
    <ListSquare 
        list={categories} 
        title="Pick category!" 
        color="#ddc7ff"
        borderColor="#7b6492"
        width="18%"
        heigth="70vh"
        />
  )
}

export default Categories