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

    changeOrderMode = (event) => {
        this.setState({
            orderMode: event.target.value
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
                <h1> Order Assistant </h1>

                <p>Which restaurant would you like to order from?</p>
                <select className="form-select" onChange={this.changeRestaurant}>
                    <option value="">--- choose a restaurant ---</option>
                    {
                        this.state.restaurants.map(restaurant => {
                            return <option key={restaurant.id} value={restaurant.id}>{restaurant.name}</option>
                        })
                    }
                </select>

                { this.state.restaurantId && <Menu restaurantId={this.state.restaurantId} /> }

                <p>How would you like to order?</p>
                <select className="form-select" onChange={this.changeOrderMode}>
                    <option value="TEXT">Text</option>
                    <option value="AUDIO">Audio</option>
                </select>

                {
                    this.state.orderMode === 'AUDIO' && (
                        <div>
                            <AudioReactRecorder state={recordState} onStop={this.makeAudioOrder} />
                            <button onClick={this.start}>Start Order</button>
                            <button onClick={this.stop}>Make Order</button>
                        </div>
                    )
                }
                {
                    this.state.orderMode === 'TEXT' && (
                        <div>
                            <textarea onChange={this.onOrderTextChange} value={this.state.orderText}></textarea>
                            <button onClick={this.makeTextOrder}>Make Order</button>
                        </div>
                    )
                }

                { this.state.order && <Order order={this.state.order} /> }

            </div>
        )
    }
    
}