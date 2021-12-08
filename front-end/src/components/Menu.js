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
            <div className="p-3" key={menuItem.id}>
              <div key={menuItem.id} className="card">
                <img src={menuItem.img} className="card-img-top" alt="..."></img>
                <div className="card-body">
                  <h5 className="card-title">{menuItem.name}</h5>
                  <p className="card-text">{menuItem.desc}</p>
                  <small className="text-muted">{menuItem.price}</small>
                </div>
              </div>
            </div>
          ))
        }
      </div>
    </div>
  ) : 
  (
    <div className="spinner-border" role="status">
      <span className="visually-hidden">Loading...</span>
    </div>
  );

}

export default Menu;