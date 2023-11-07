document.addEventListener('DOMContentLoaded', function() {
    const searchForm = document.getElementById('search-form');
    const searchInput = document.getElementById('search-input');
    const errorDisplay = document.getElementById('error-message');

    const fetchData = (city) => {
        fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=80fd590be088300616be1e164aa6d67e`)
            .then((response) => {
                if (!response.ok) {
                    throw new Error('City not found');
                }
                return response.json();
            })
            .then((jsonData) => {
                errorDisplay.style.display = 'none';

                fetch(`https://openweathermap.org/img/wn/${jsonData.weather[0].icon}@2x.png`)
                    .then((res) => res.blob())
                    .then((result) => {
                        document.getElementById("text_location").innerHTML = jsonData.name;
                        document.getElementById("text_location_country").innerHTML = jsonData.sys.country;
                        document.getElementById("text_temp").innerHTML = jsonData.main.temp;
                        document.getElementById("text_feelslike").innerHTML = jsonData.main.feels_like;
                        document.getElementById("text_desc").innerHTML = jsonData.weather[0].description;

                        const imageObjectURL = URL.createObjectURL(result);
                        document.getElementById("icon").src = imageObjectURL;
                    })
                    .catch((error) => {
                        console.error('Error loading image:', error);
                        errorDisplay.textContent = 'Error loading weather icon. Please try again.';
                        errorDisplay.style.display = 'block';
                    });
            })
            .catch((error) => {
                errorDisplay.textContent = 'Invalid city name. Please try again.';
                errorDisplay.style.display = 'block';
            });
    };

    const handleUserInput = () => {
        const city = searchInput.value;
        fetchData(city);
    };

    searchForm.addEventListener('submit', function(event) {
        event.preventDefault(); 
        handleUserInput();
    });

    fetchData('Maranello');
});
