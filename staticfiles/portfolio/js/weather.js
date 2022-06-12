document.addEventListener('DOMContentLoaded', function () {
    fetch('https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json')
        .then(response => response.json())
        .then(data => {
            const max_temp = data.data[0].tMax;
            const min_temp = data.data[0].tMin;

            document.getElementById('max_temp').innerHTML = max_temp + '°C';
            document.getElementById('min_temp').innerHTML = min_temp + '°C';
        });
});
