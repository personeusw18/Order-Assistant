import React, { Component } from 'react';
import AudioReactRecorder, { RecordState } from 'audio-react-recorder'
import Menu from './components/Menu';
import Order from './components/Order';
import api from './helpers/api';

export default class App extends Component{
    constructor(props){
        super(props)

        this.state = {
            recordState: null,
            restaurants : [],
            restaurantId: null,
            orderMode: 'TEXT',
            orderText: '',
            order: null,
        }
    }

    componentDidMount() {
        api.getRestaurants()
        .then(response => {
            this.setState({
                restaurants: response.data
            })
        })
        .catch(error => {
            console.log(error);
        })
    }

    start = () => {
        this.setState({
            recordState: RecordState.START
        })
    }

    stop = () => {
        this.setState({
            recordState: RecordState.STOP
        })
    }

    makeAudioOrder = (audioData) => {
        api.makeAudioOrder(this.state.restaurantId, audioData)
        .then((res) => {
            this.setState({
                order: res.data
            })
        });
    }

    makeTextOrder = () => {
        api.makeTextOrder(this.state.restaurantId, this.state.orderText)
        .then((res) => {
            this.setState({
                order: res.data
            })
        });
    }

    handleAudio(event) {
        event.preventDefault();
    }

    changeRestaurant = (event) => {
        this.setState({
            restaurantId: event.target.value
        })
    }

    changeOrderMode = (mode) => {
        this.setState({
            orderMode: mode
        })
    }

    onOrderTextChange = (event) => {
        this.setState({
            orderText: event.target.value
        })
    }

    render() {
        const { recordState } = this.state;

        return(
            <div>
                <nav className="navbar navbar-light bg-light">
                    <div className="container">
                        <a className="navbar-brand text-primary" href="#">
                            <img src="https://www.chatbot.com/favicon.ico" width="30" height="30" class="d-inline-block align-top me-2"></img>
                            Order Assistant
                        </a>
                    </div>
                </nav>

                <div className="container">
                    <div className="mt-3">
                        <label htmlFor="restaurant">Which restaurant would you like to order from?</label>
                        <select id="restaurant" className="form-select" onChange={this.changeRestaurant}>
                            <option defaultValue value="">--- choose a restaurant ---</option>
                            {
                                this.state.restaurants.map(restaurant => {
                                    return <option key={restaurant.id} value={restaurant.id}>{restaurant.name}</option>
                                })
                            }
                        </select>
                    </div>

                    { this.state.restaurantId && <Menu restaurantId={this.state.restaurantId} /> }

                    { this.state.restaurantId && <button type="button"  data-bs-toggle="modal" data-bs-target="#orderModal" className="btn btn-success mb-5">Ready to order</button> }

                    <div className="modal fade" id="orderModal" aria-hidden="true" tabindex="-1">
                        <div className="modal-dialog modal-dialog-centered">
                            <div className="modal-content">
                                <div className="modal-header">
                                    <h5 className="modal-title" id="exampleModalToggleLabel">Create an Order</h5>
                                    <button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                </div>
                                <div className="modal-body">
                                    <div style={{ textAlign: "center" }} className="p-2">
                                        <div className="btn-group" role="group">
                                            <input onClick={() => this.changeOrderMode("TEXT")} type="radio" className="btn-check" name="btnradio" id="btnradio1" autocomplete="off" checked={this.state.orderMode==="TEXT"}></input>
                                            <label className="btn btn-outline-primary" for="btnradio1">Make text order</label>
                                            <input onClick={() => this.changeOrderMode("AUDIO")} type="radio" className="btn-check" name="btnradio" id="btnradio2" autocomplete="off" checked={this.state.orderMode==="AUDIO"}></input>
                                            <label className="btn btn-outline-primary" for="btnradio2">Make audio order</label>
                                        </div>
                                    </div>
                                    {
                                        this.state.orderMode === 'AUDIO' && (
                                            <div className="p-2">
                                                <AudioReactRecorder state={recordState} onStop={this.makeAudioOrder} canvasWidth="400%"/>
                                                <button className="btn btn-primary" onClick={this.start}>Start Order</button>
                                                { recordState === RecordState.START && <button data-bs-toggle="modal" data-bs-target="#receiptModal" className="btn btn-primary" onClick={this.stop}>Make Order</button> }
                                            </div>
                                        )
                                    }
                                    {
                                        this.state.orderMode === 'TEXT' && (
                                            <div className="p-2">
                                                <textarea className="form-control" placeholder="Can I get a..." onChange={this.onOrderTextChange} value={this.state.orderText}></textarea>
                                                <button data-bs-toggle="modal" data-bs-target="#receiptModal" class="btn btn-primary" onClick={this.makeTextOrder}>Make Order</button>
                                            </div>
                                        )
                                    }
                                </div>
                            </div>
                        </div>
                    </div>


                    <div className="modal fade" id="receiptModal" aria-hidden="true" tabindex="-1">
                        <div className="modal-dialog modal-dialog-centered">
                            <div className="modal-content">
                                <div className="modal-header">
                                    <h5 className="modal-title" id="exampleModalToggleLabel">Receipt</h5>
                                    <button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                </div>
                                <div className="modal-body">
                                    <Order order={this.state.order} />
                                </div>
                                <div className="modal-footer">
                                    <button type="button" className="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                    <button type="button" className="btn btn-primary">Proceed to Checkout</button>
                                </div>
                            </div>
                        </div>
                    </div>


                </div>
            </div>
        )
    }
    
}