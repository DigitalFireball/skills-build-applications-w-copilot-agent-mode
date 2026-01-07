import React, { useEffect, useState } from 'react';
const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;

function Workouts() {
  const [data, setData] = useState([]);
  useEffect(() => {
    console.log('Fetching from:', apiUrl);
    fetch(apiUrl)
      .then(res => res.json())
      .then(json => {
        const results = json.results || json;
        setData(results);
        console.log('Fetched workouts:', results);
      });
  }, []);
  return (
    <div>
      <h2>Workouts</h2>
      <ul>{Array.isArray(data) && data.map((w, i) => <li key={i}>{w.name}: {w.description}</li>)}</ul>
    </div>
  );
}
export default Workouts;
