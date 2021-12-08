import React from 'react';

function Order(props) {
  return props.order ? (
    <div>
      <div className="list-group list-group-flush">
        {
          props.order.order.map((item, index) => {
            return (
              <div className="list-group-item list-group-item-action" key={item.name}>
                <div className="d-flex w-100 justify-content-between">
                  <p className="mb-1">{item.name}</p>
                  <small>${item.price}</small>
                </div>
              </div>
            )
          })
        }
        <div className="list-group-item list-group-item-action">
          <div className="d-flex w-100 justify-content-between">
            <p className="mb-1 fw-bold">Subtotal</p>
            <small>${props.order.subtotal.toFixed(2)}</small>
          </div>
        </div>
        <div className="list-group-item list-group-item-action">
          <div className="d-flex w-100 justify-content-between">
            <p className="mb-1 fw-bold">Taxes</p>
            <small>${props.order.taxes.toFixed(2)}</small>
          </div>
        </div>
        <div className="list-group-item list-group-item-action">
          <div className="d-flex w-100 justify-content-between">
            <p className="mb-1 fw-bold">Total</p>
            <small>${props.order.total.toFixed(2)}</small>
          </div>
        </div>

      </div>

    </div>
  ) : (
    <div className="spinner-border" role="status">
      <span className="visually-hidden">Loading...</span>
    </div>
  )
}

export default Order;