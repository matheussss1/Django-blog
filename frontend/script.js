const fetchAPI = async (url, options={}) => {
    const response = await fetch(url, options);
    const data = await response.json();
    return data
}

const options = {
    method: 'POST',
    mode: 'no-cors',
    body: {"username": 'matheus', "password": 1},
    ContentType: 'application/json'
}

const data = fetchAPI('http://127.0.0.1:8000/api-login/', options)
    .then(data => data)