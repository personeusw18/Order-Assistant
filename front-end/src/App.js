import axios from 'axios';
import React, { Component } from 'react';
import AudioReactRecorder, { RecordState } from 'audio-react-recorder'

const API = "http://localhost:8000/"

export default class App extends Component{
    constructor(props){
        super(props)

        this.state = {
            recordState: null
        }
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

    onStop = (audioData) => {
      console.log(audioData)
      const data = new FormData();
      data.append("order_audio", audioData.blob.stream())
      axios.post(API+'order/audio?restaurant_id=1', data, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      .then((res) => console.log(res.data));
    }

    handleAudio(event) {
        event.preventDefault();
        
    }
    

    render() {
        const { recordState } = this.state

        return(
            <div>
            <h1> Order Assistant </h1> 
            <h3> Submit an audio recording. </h3> 
            <AudioReactRecorder state={recordState} onStop={this.onStop} />
            <button onClick={this.start}>Start</button>
            <button onClick={this.stop}>Stop</button>
            </div>
        )
    }
    
}