// dashboard/assets/js/realtime.js
const socket = new WebSocket('wss://yourdomain.co.za/live');
socket.onmessage = (event) => {
    updateSalesCounter(JSON.parse(event.data).sales);
};
