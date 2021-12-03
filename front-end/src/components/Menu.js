import React, { useEffect, useState } from 'react';
import api from '../helpers/api';

function Menu(props) {

  const [restaurant, setRestaurant] = useState(null);

  useEffect(() => {
    api.getRestaurant(props.restaurantId)
    .then(res => {
      setRestaurant(res.data);
    })
    .catch(err => {
      console.log(err);
    });
  }, [props.restaurantId]);
  

  return restaurant ? (
    <div>
      <h1>{restaurant.name}</h1>
      <img src={restaurant.img} alt={restaurant.name}  style={{ width: '25%' }}/>
      {
        restaurant.menu_items.map(menuItem => (
          <div key={menuItem.id}>
            <h5>{menuItem.name}</h5>
            <small>{menuItem.desc}</small>
          </div>
        ))
      }
    </div>
  ) : 
  (
    <div>Loading...</div>
  );

}

export default Menu;