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
      <div style={{ textAlign: 'center' }} className="p-4">
        <img src={restaurant.img} alt={restaurant.name}  style={{ height: '8rem' }}/>
      </div>
      <div className="row row-cols-3">
        {
          restaurant.menu_items.map(menuItem => (
            <div className="p-3">
              <div key={menuItem.id} className="card p-2">
                <img src={menuItem.img} className="card-img-top" alt="..."></img>
                <div className="card-body">
                  <h5 className="card-title">{menuItem.name}</h5>
                  <p className="card-text">{menuItem.desc}</p>
                </div>
              </div>
            </div>
          ))
        }
      </div>
    </div>
  ) : 
  (
    <div class="spinner-border" role="status">
      <span class="visually-hidden">Loading...</span>
    </div>
  );

}

export default Menu;