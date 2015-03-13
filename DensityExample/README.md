# Density of Air Pollution
This application creates a hex density map of [Albuquerque Air Pollution Sources](http://coagisweb.cabq.gov/arcgis/rest/services/public/environmentalissues/MapServer/1). 
##How it works
The application creates a hexgrid. You can modify the size of the hexagons to alter the results. It then grabs all the pollution sources in Albuquerque from the Open Data and runs a point in polygon - using Turf - to get a count for each hexagon. It then adds the hexagons to the map and colors them based on count. You can also change the color ramp values.
The application takes some time to run. Be patient. Also, there are other URLs included in the code. Crime incidents would be an excellent one to use - just make sure to remove incidents that do not have an x,y value or the application will crash.
If you change the data source, be sure to change the hexgrid sizes and color ramp values to fit the data.
