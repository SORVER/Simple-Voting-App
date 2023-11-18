document.addEventListener('DOMContentLoaded', () => {
        
        // standerd line to use sockets
        var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
          
        // config buttons, "connect" here is standerd
        socket.on('connect', () => {
            
        document.querySelectorAll('button').forEach(button => {
            
            button.onclick = () => {

                const selection = button.dataset.vote ; // geeting data-vote value for the clicked one
                socket.emit('submit vote', {'selection': selection}); // sending to the server
            }

        })

        });

        // "annouce vote" is taken from the emit done in the web server
        socket.on('annouce vote', data => {
   
              let allco = data["yes"] + data["maybe"] +data["no"];
              console.log(allco);
              document.getElementById('no-container').style.width = `${data["no"]*100/allco}%`; // in JS you can't data['selection'] but data.selecton
              document.getElementById('yes-container').style.width = `${data["yes"]*100/allco}%`; 
              document.getElementById('maybe-container').style.width = `${data["maybe"]*100/allco}%`; 


        });
   }
);