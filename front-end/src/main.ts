import {createApp} from 'vue'
import './style.css'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import App from './App.vue'
import axios from "axios";

axios.defaults.baseURL = `${import.meta.env.VITE_API_HOST}:${import.meta.env.VITE_API_PORT}`;

createApp(App).mount('#app')
