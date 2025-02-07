fetch('articles.json')
    .then(response => response.json())
    .then(data => {
        const list = document.getElementById('article-list');
        data.sort((a, b) => new Date(b.date) - new Date(a.date)); // Sort by latest first
        data.forEach(article => {
            let li = document.createElement('li');
            li.innerHTML = `<a href="${article.link}" target="_blank">${article.title}</a>`;
            list.appendChild(li);
        });
    })
    .catch(error => console.error('Error loading articles:', error));
