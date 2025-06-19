const apiKey="0816c7fc83803336c46424d250dac9ce";
const apiURL="https://api.openweathermap.org/data/2.5/weather?units=metric"
var searchBox=document.querySelector("#search");
const srcButton=document.querySelector(".button");
async function GetData(city){
    const response= await fetch(apiURL +`&q=${city}&appid=${apiKey}`);
    var data=await response.json();
    console.log(data);

    document.querySelector(".temperature").innerHTML = Math.round(data.main.temp);
    document.querySelector(".city").innerHTML = data.name;
    document.querySelector(".humidity").innerHTML = data.main.humidity +"%";
    document.querySelector(".wind").innerHTML = data.wind.speed + "km/h";
}

srcButton.addEventListener("click",()=>{
    GetData(searchBox.value)
})


