import axios from 'axios';
import React, { useEffect, useState } from 'react';
import Homepage from './components/Homepage.js';
function App() {
  const [heading, setHeading] = useState('');
  const [error, setError] = useState(null);

  useEffect(() => {
  
    axios.get('http://127.0.0.1:5000/homepage')
      .then(response => {
        console.log('Response data:', response.data); 
        setHeading(response.data.heading);
      })
      .catch(error => {
        console.error('There was an error fetching the heading data!', error);
        setError(error.message); 
      });
  }, []);

  return (
    <div>
      <h1>{heading}</h1>
      <Homepage head={heading}/>
    </div>
  );
}

export default App;
