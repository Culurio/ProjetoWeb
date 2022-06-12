function showTime() {
    var dateTime = new Date();
    var hours = dateTime.getHours();
    var minutes = dateTime.getMinutes();
    var seconds = dateTime.getSeconds();
    var session = document.getElementById('session');
    var min = '0';

    if (hours < 10)
        hours = min.concat(hours);

    if (minutes < 10)
        minutes = min.concat(minutes);

    if (seconds < 10)
        seconds = min.concat(seconds);

    if (hours >= 12) {
        session.innerHTML = 'PM';
    } else {
        session.innerHTML = 'AM';
    }

    if (hours > 12) {
        hours = hours - 12;
    }

    document.getElementById('hours').innerHTML = hours;
    document.getElementById('minutes').innerHTML = minutes;
    document.getElementById('seconds').innerHTML = seconds;
}

setInterval(showTime, 10);