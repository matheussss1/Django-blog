const fetchAPI = async (url, options={}) => {
    const response = await fetch(url, options);
    const data = await response.json();
    return data;
}

const options = {
    method: 'GET',
    ContentType: 'application/json',
}

const data = fetchAPI('http://localhost:8000/api/posts/', options)
    .then(data => {
        console.log(data)
        data.map(e => {
            const status = e.status == 'R'? 'Rascunho' : 'Postado'
            document.querySelector('.post').innerHTML += 
            `
                <tr>
                    <td><a href="${e.slug}">${e.titulo}</a></td>
                    <td>${e.autor['first_name']}</td>
                    <td>${e.criado}</td>
                    <td>${e.atualizado}</td>
                    <td>${status}</td>
                </tr>
            `
        })
    });

    
