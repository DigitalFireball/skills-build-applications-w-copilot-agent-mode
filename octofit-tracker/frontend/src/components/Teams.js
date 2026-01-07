import React, { useEffect, useState } from 'react';
const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;

function Teams() {
  const [data, setData] = useState([]);
  useEffect(() => {
    console.log('Fetching from:', apiUrl);
    fetch(apiUrl)
      .then(res => res.json())
      .then(json => {
        const results = json.results || json;
        setData(results);
        console.log('Fetched teams:', results);
      });
  }, []);
  return (
    <div>
      <h2>Teams</h2>
      <ul>{Array.isArray(data) && data.map((t, i) => <li key={i}>{t.name}</li>)}</ul>
    </div>
  );
}
export default Teams;
