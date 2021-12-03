import React from 'react';

function Order(props) {
  return (
    <div>
      <h2>Order</h2>
      {
        props.order.order.map((item, index) => {
          return (
            <div key={index}>
              <p>{item.name}</p>
              <small>{item.price}</small>
            </div>
          )
        })
      }
    </div>
  )
}

export default Order;