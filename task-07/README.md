# task-07

This was quite challenging at first as I didn't know exactly what all files where required to make the extension. Then I went on to Youtube to find a video of the creator making a similar weather extension. But the issue there was that it used manifest version 2. For changing that I found another youtube video using the latest manifest version 3. 

Coding the html and css files were fairly simple as most of it I learned from the first Youtube video. So most of the features of my extension's appearance is similar to the one in the video like the City Name, City Tag, Feels like etc... Some of the features of the extension can still be improved as in like the relative alignment of each element. For the logo I downloaded an image from GoogleImages and for the search-button-icon I basically inspected the amFOSSWeather extension and downloaded that search_icon. After styling all that was left was a bit of backend.

Coding javascript took a little practice. Despite Java and Javascript sounding similar, I found each having very different syntaxes and semantics. 
I used an OpenWeather API key for creating the link to access the weather related real-time features and information about an entered city. Most of the programming includes just error handling for 'wrong city names' and loading icons etc...

Finally I put the default city name to 'Maranello' for loading a weather data on default.