import React, { useEffect, useState } from 'react';
const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;

function Leaderboard() {
  const [data, setData] = useState([]);
  useEffect(() => {
    console.log('Fetching from:', apiUrl);
    fetch(apiUrl)
      .then(res => res.json())
      .then(json => {
        const results = json.results || json;
        setData(results);
        console.log('Fetched leaderboard:', results);
      });
  }, []);
  return (
    <div>
      <h2>Leaderboard</h2>
      <ul>{Array.isArray(data) && data.map((l, i) => <li key={i}>{l.team}: {l.points} pts</li>)}</ul>
    </div>
  );
}
export default Leaderboard;
