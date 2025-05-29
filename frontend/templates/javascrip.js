console.log("Hello")


document.getElementById("city_form").addEventListener("submit", function(event){
        event.preventDefault();
        let city = document.getElementById("city").value
        console.log(city)
        fetch(`http://127.0.0.1:8000/temperature/${city}`)
            .then(response => response.json())
            .then(data => document.getElementById("weather").textContent = JSON.stringify(data)
        )
    })