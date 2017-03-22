### Lab 4: Web Mapping

##### Christina Chappell

I used the data that I scraped from the last lab for this one as well. That data was locations that 8 movies were filmed at in Washington State. 
I addressed how the geoparser.io was not that effective in getting all the correct geospatial data in the last lab.
For this lab, that data I used was put into mapbox with a layer for each movie to change the zoom and visual for the map. 

Another layer I used for a choropleth map underneath was data at the county level of how many days a year there is precipitation. I chose this because Seattle/ Washington is well known for being a very wet area, so showing what places were chosen to film in with precipitation sounded very interesting to me. The difference between western Washington and Eastern washington is noticeable with the drop in precipitation on the eastern side. Finding the precipitation data was difficult, I could not find one table with all the counties, instead I found separate pages for each county from the Sperling's website (link below), I added a field to my county shapefile and typed in all the information. 

The data I was originally using was simple film locations, so I had a difficult time trying to conceptualize an effect I wanted to seek. I struggled with precipitation so I tried doing other topics like population, but it seemed to random to me to use that with film locations. I think I achieved a simple version of what I wanted to seek, which was why were locations chosen for the film. Personally I found this very interesting because I knew that The Ring (2002) was shot in Stanwood (my hometown) because there was a farm that had a well on a hill near a cabin. 

As the user zooms out, the titles disappear one at a time to make room so there is not overlap between titles. I did not want the map to get too busy with a lot of titles covering the whole of WA. When the user is zoomed out, each movie has it's own color, so just the colored dots are visible. Once zoomed in the user can see the titles for the movies as well.

The map could be improved by adding popups for each movie instead of having all the titles on the map at once. There are a couple dots that have multiple movies for the same location, this could be fixed by having the dots be slightly offset and all visible at the same time.

I had help from Professor Bergmann, Olivia, and the mapbox tutorials/documentation. 

##### Map Link: http://students.washington.edu/chappchr/moviefilmloc.html



Sources:

1. http://www.bestplaces.net/

2. http://www.onlyinyourstate.com/washington/washington-movies/
