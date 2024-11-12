import logo from './logo.svg';
import './App.css';
import Camara from './components/CamaraComponent/camara';
import BotonesControl from './components/BotonesComponent/botones';  // Importa el componente

function App() {
  return (
    <div className="App">
       <Camara />
       <BotonesControl/>
    </div>
  );
}

export default App;
