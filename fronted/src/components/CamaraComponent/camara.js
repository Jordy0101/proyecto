import React from 'react';

function CameraControl() {
  const abrirCamara = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/abrir-camara");
      if (response.ok) {
        console.log("La interfaz de cámara se ha abierto correctamente.");
      } else {
        console.error("Error al abrir la interfaz de cámara:", response.statusText);
      }
    } catch (error) {
      console.error("Hubo un problema al conectar con el servidor:", error);
    }
  };

  return (
    <div>
      <h1>Control de Cámara</h1>
      <button onClick={abrirCamara}>Abrir Cámara</button>
    </div>
  );
}

export default CameraControl;
