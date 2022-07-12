import React, { useEffect, useState } from 'react'
import { api } from '../api'
import ListSquare from './ListSquare'

const Categories = () => {

  const [ categories, setCategories ] = useState([])

  useEffect(() => {
    api.get("get_categories")
      .then(res => {
        setCategories(res.data.names)
      }).catch(function(error) {
        console.log(error)
        setCategories([error.toJSON().message])
      })
  }, [])
    
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