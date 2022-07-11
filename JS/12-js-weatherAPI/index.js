
async function get_weather() {

    let url = `http://api.weatherapi.com/v1/forecast.json?key=3dde6d1aa776460f8e8164408222406&q=Dunaivtsi&days=5&aqi=yes&alerts=no`;
    let response = await fetch(url);

    if (response.ok) {
        let json = await response.json();
        document.getElementById("city").innerHTML = json.location.name + ", " + json.location.country;
        document.getElementById("time").innerHTML = json.current.last_updated;
        document.getElementById("pict").src = json.current.condition.icon;
        document.getElementById("condition").innerHTML = json.current.condition.text;
        document.getElementById("temperature").innerHTML = json.current.temp_c + " &#176C";
        document.getElementById("Wind").innerHTML = "Wind: " + json.current.wind_kph + " kph";
        document.getElementById("Precip").innerHTML = "Precip: " + json.current.precip_mm + " mm";
        document.getElementById("Pressure").innerHTML = "Pressure: " + json.current.pressure_mb + " mb";

        for (let index = 0; index < json.forecast.forecastday.length; index++) {
            let date = json.forecast.forecastday[index].date.split('-');
            let dayOfWeek = new Date(date[0], date[1], date[2]).toLocaleDateString('en-US', { weekday: 'short', });

            document.getElementById("day" + index).innerHTML =
            `<span style="font-weight: bold;">${dayOfWeek}</span>
            <br>
            <span>${json.forecast.forecastday[index].date}</span>
            <br>
            <img src="${json.forecast.forecastday[index].day.condition.icon}" alt="">
            <span style="font-weight: bold; font-size: 20px;">${json.forecast.forecastday[index].day.avgtemp_c + " &#176C"}</span>`;

        }


        console.log(json);


    } else {
        alert("Ошибка HTTP: " + response.status);
    }
}
window.onload = get_weather;
