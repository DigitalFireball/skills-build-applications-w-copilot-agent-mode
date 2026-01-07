import React, { useEffect, useState } from 'react';
const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;

function Users() {
  const [data, setData] = useState([]);
  useEffect(() => {
    console.log('Fetching from:', apiUrl);
    fetch(apiUrl)
      .then(res => res.json())
      .then(json => {
        const results = json.results || json;
        setData(results);
        console.log('Fetched users:', results);
      });
  }, []);
  return (
    <div>
      <h2>Users</h2>
      <ul>{Array.isArray(data) && data.map((u, i) => <li key={i}>{u.username} ({u.email})</li>)}</ul>
    </div>
  );
}
export default Users;
