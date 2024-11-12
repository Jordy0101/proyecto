import React, { Component } from 'react';

export default class BotonesControl extends Component {

    // Función genérica para enviar un evento a cualquier endpoint
    handleButtonPress = async (buttonName) => {
        try {
            const response = await fetch(`http://127.0.0.1:8000/button/${buttonName}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
            });

            const data = await response.json();
            console.log(data.message);
            alert(data.message);  // Mostrar el mensaje de respuesta
        } catch (error) {
            console.error(`Error al presionar el botón ${buttonName}:`, error);
            alert(`Error al presionar el botón ${buttonName}`);
        }
    };

    // Función para manejar las teclas presionadas
    handleKeyPress = async (event) => {
        const eventKey = event.key;
        try {
            const response = await fetch('http://127.0.0.1:8000/button/handle_key_press', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ event_key: eventKey }),
            });

            const data = await response.json();
            console.log(data.message);
            alert(data.message);  // Mostrar el mensaje de respuesta
        } catch (error) {
            console.error('Error al procesar el evento de tecla:', error);
            alert('Error al procesar el evento de tecla');
        }
    };

    render() {
        return (
            <div className="botones-control">
                <button onClick={() => this.handleButtonPress('button_star')}>Botón *</button>
                <button onClick={() => this.handleButtonPress('button_slash')}>Botón /</button>
                <hr />
                <button onClick={() => this.handleButtonPress('button1')}>Botón 1</button>
                <button onClick={() => this.handleButtonPress('button2')}>Botón 2</button>
                <button onClick={() => this.handleButtonPress('button3')}>Botón 3</button>
                <button onClick={() => this.handleButtonPress('button4')}>Botón 4</button>
                <button onClick={() => this.handleButtonPress('button5')}>Botón 5</button>
                <button onClick={() => this.handleButtonPress('button6')}>Botón 6</button>
                <button onClick={() => this.handleButtonPress('button7')}>Botón 7</button>
                <button onClick={() => this.handleButtonPress('button8')}>Botón 8</button>
                <button onClick={() => this.handleButtonPress('button9')}>Botón 9</button>
                <hr />
                <input 
                    type="text" 
                    placeholder="Presiona una tecla..." 
                    onKeyDown={this.handleKeyPress}  // Llama al backend cuando una tecla es presionada
                />
            </div>
        );
    }
}
