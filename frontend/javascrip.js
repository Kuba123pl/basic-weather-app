console.log("Hello")


document.getElementById("city_form").addEventListener("submit", function(event){
        event.preventDefault();
        let city = document.getElementById("city").value
        console.log(city)
        fetch(`http://127.0.0.1:8000/temperature/${city}`)
            .then(
                response =>
                    response.json())
            .then(data => {
                console.log(data);
                if(data['current']['temperature_2m']>=25){
                    console.log("I got in")
                    let img = document.createElement('img');
                    img.src = "../images/warm-weather-summer.gif";
                    //document.getElementById("weather").textContent = JSON.stringify(data['latitude'])
                    const weatherImageDiv = document.getElementById('weather');
                    weatherImageDiv.innerHTML = '';
                    weatherImageDiv.appendChild(img);
                    document.getElementById('weather_info').textContent = 'Sunny Day \u{2600}\uFE0F';
                    let temperature = data['current']['temperature_2m'] + "°C"
                    document.getElementById('temperature').textContent = temperature
                }
                else{
                    let img = document.createElement('img');
                    img.src = "../images/storm-world-meteorological-day.gif";
                    //document.getElementById("weather").textContent = JSON.stringify(data['latitude'])
                    const weatherImageDiv = document.getElementById('weather');
                    weatherImageDiv.innerHTML = '';
                    weatherImageDiv.appendChild(img);
                    const text = document.getElementById('weather_info');
                    text.textContent = 'Cloudy Day \u{2601}\uFE0F';
                    text.style.fontSize = "24px"
                    let temperature = data['current']['temperature_2m'] + "°C"
                    document.getElementById('temperature').textContent = temperature
                }
                    
            }
        )
    }
)