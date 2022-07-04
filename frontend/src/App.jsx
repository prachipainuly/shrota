import './App.css';
import { Divider } from '@mui/material';
import { TopBar } from './components/TopBar';
import Categories from './components/Categories';
import GameArea from './components/GameArea';
import BottomSquare from './components/BottomSquare';
import Ranking from './components/Ranking';
import StartGame from './components/StartGame';

function App() {
    return (
      <div className='app'>
          <TopBar/>
          <Divider style={{backgroundColor: 'black'}} />
          <Divider style={{backgroundColor: '#2c5977', width: '91.5%', height: '8vh', margin: '1% auto'}} />
          <div className="main">
              <Categories />
              <div className="vertical-flexbox">
                  <GameArea />
                  <BottomSquare />
              </div>
              <div className="vertical-flexbox">
                  <Ranking />
                  <StartGame />
              </div>
          </div>
      </div>
    );
}

export default App;
