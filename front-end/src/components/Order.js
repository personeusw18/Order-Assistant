import React from 'react';

function Order(props) {
  return props.order ? (
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
  ) : (
    <p>loading...</p>
  )
}

export default Order;