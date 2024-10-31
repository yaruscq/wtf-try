document.addEventListener('DOMContentLoaded', () => {

    const socket = io();

    // Setup a pre-defined event bucket called 'connect' at the server side in JSds
    
    //For testing
    socket.on('connect', () => { // client connected, and send 'connected' to the server
        // since 'send()' is used here, the msg will be sent to the server into a pre-defined bucket 'message'
        socket.send("我連上了！");
    });

    // 來自 server 的 message event 給 client，告訴他(client)，已經收到他傳來的 "我連上了！"
    socket.on('message', data => {

        console.log(`Server 已經收到你傳來的 ${data}`)
    })

    socket.on('some-event', data => {

        console.log(data);
    })

})