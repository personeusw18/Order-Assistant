import axios from 'axios';

const API = "http://localhost:8000/"

function getRestaurants() {
  return axios.get(API + 'restaurant')
}

function getRestaurant(id) {
  return axios.get(API + `restaurant/${id}`)
}

function makeAudioOrder(restaurantId, audioData) {
  const data = new FormData();
  data.append("order_audio", audioData.blob)
  return axios.post(API + `order/audio/${restaurantId}`, data, {
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  })
}

function makeTextOrder(restaurantId, orderText) {
  return axios.post(API + `order/text/${restaurantId}?order_text=${orderText}`)
}

const api = {
  getRestaurants,
  getRestaurant,
  makeAudioOrder,
  makeTextOrder,
}

export default api;