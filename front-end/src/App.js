import axios from 'axios';
import React,{Component} from 'react'; 

const API = "http://localhost:8000/"

class App extends Component { 

    state = { 
      // Initially, no file is selected 
      audioFile: null
    }; 
     
    // On file select (from the pop up) 
    onFileChange = event => { 
      // Update the state 
      this.setState({ audioFile: event.target.files[0] }); 
    }; 
     
    // On file upload (click the upload button) 
    onFileUpload = () => { 
      // Create an object of formData 
      const formData = new FormData(); 
     
      // Update the formData object 
      formData.append( 
        "myFile", 
        this.state.audioFile, 
        this.state.audioFile.name 
      ); 
     
      // Details of the uploaded file 
      console.log(this.state.audioFile); 
     
      // Request made to the backend api 
      // Send formData object 

      axios.post(API + "dummy_order", {})
      .then(
        res => {
          const order = res.data;
          console.log(order);
        }
      );
    }; 
     
    // File content to be displayed after 
    // file upload is complete 
    fileData = () => { 
      if (this.state.audioFile) { 
          
        return ( 
          <div> 
            {/* <h2>File Details:</h2> 
            <p>File Name: {this.state.audioFile.name}</p> 
            <p>File Type: {this.state.audioFile.type}</p> 
            <p> 
              Last Modified:{" "} 
              {this.state.audioFile.lastModifiedDate.toDateString()} 
            </p>  */}
          </div> 
        ); 
      } else { 
        return ( 
          <div> 
            <h4>To make your order, upload an audio file.</h4> 
          </div> 
        ); 
      } 
    }; 
     
    render() { 
      return ( 
        <div> 
            <h1> 
              Order Assistant 
            </h1> 
            <h3> 
              Submit an audio recording. 
            </h3> 
            <div> 
                <input type="file" onChange={this.onFileChange} /> 
                <button onClick={this.onFileUpload}> 
                  Upload! 
                </button> 
            </div> 
          {this.fileData()} 
        </div> 
      ); 
    } 
  } 
  
  export default App; 