const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': 'd3e8f37b24msh6f5fa9edb567ad7p1861ebjsn2db6f92a83df',
		'X-RapidAPI-Host': 'random-facts2.p.rapidapi.com'
	}
};

fetch('https://random-facts2.p.rapidapi.com/getfact', options)
	.then(response => response.json())
	.then(data => {
		document.getElementById('fact').innerHTML = data.Fact;
	})
	.catch(err => console.error(err));