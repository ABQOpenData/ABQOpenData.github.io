# Elevation Profile
This application creates an elevation profile from a line on the map using [Albuquerque Elevation Data](http://coagisweb.cabq.gov/arcgis/rest/services/public/contours/MapServer/0). 
##How it works
The application allows the user to draw a line.  For each point in the line, a buffer is created and the elevation endpoint queried for the nearest contour line value. Using Chart.js, a bar chart is drawn showing the profile. The more points you add when drawing the line the better - do not draw a line, rather, draw a polyline with lots of segments.
