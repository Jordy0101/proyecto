import React, { Component } from 'react';
import Webcam from "react-webcam";

export default class Camara extends Component {
    setRef = webcam => {
        this.webcam = webcam;
    }

    state = {
        imagen: null
    }

    foto = () => {
        var captura = this.webcam.getScreenshot(); // Tomar la captura
        console.log(captura); // Ver la captura en consola

        // Convertir la imagen a base64
        const base64Image = captura.split(',')[1]; // Eliminar la parte de la cabecera del base64

        this.setState({
            imagen: captura
        });

        // Enviar la imagen al servidor
        this.enviarImagen(base64Image);
    };
    enviarImagen = async (base64Image) => {
        try {
            // Hacer una petición POST al servidor para guardar la imagen
            const response = await fetch('http://127.0.0.1:8000/camera/guardar', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ image: base64Image }), // Enviar la imagen en formato base64
            });
    
            // Verificar respuesta del servidor
            const data = await response.json();
            console.log('Respuesta del servidor:', data);
    
            if (data.message) {
                alert('Imagen guardada correctamente');
            } else {
                alert('Error al guardar la imagen');
            }
        } catch (error) {
            console.error('Error al enviar la imagen:', error);
            alert('Hubo un error al enviar la imagen');
        }
    };
    
    render() {
        return (
            <div className='App'>
                <Webcam audio={false} height={350} ref={this.setRef} screenshotFormat="image/jpeg" width={350} />
                <br />
                <button onClick={this.foto}>Hacer captura</button>
                <hr />
                <img src={this.state.imagen} alt="Captura" />
                {/* No se incluye el enlace de descarga */}
            </div>
        );
    }
}
