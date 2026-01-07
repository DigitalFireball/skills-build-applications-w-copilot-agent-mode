import React, { useEffect, useState } from 'react';
const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;

function Activities() {
  const [data, setData] = useState([]);
  useEffect(() => {
    console.log('Fetching from:', apiUrl);
    fetch(apiUrl)
      .then(res => res.json())
      .then(json => {
        const results = json.results || json;
        setData(results);
        console.log('Fetched activities:', results);
      });
  }, []);
  return (
    <div>
      <h2>Activities</h2>
      <ul>{Array.isArray(data) && data.map((a, i) => <li key={i}>{a.activity_type} ({a.duration_minutes} min)</li>)}</ul>
    </div>
  );
}
export default Activities;
