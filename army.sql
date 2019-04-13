CREATE database army_database;
USE army_database;

/*show table creation*/

select * from base_locations;

/* sum quantities filtered by type */

select sum(Quantity)
from base_locations
where Type = "Air RVCT";

select * from base_locations
where Type = "Air RVCT";

select sum(Quantity)
from base_locations
where Type = "Ground RVCT";

select Name, State, Latitude, Longitude, Type, Quantity from base_locations
where Type = "Ground RVCT";

/* sum quantities filtered by region */

select Name, State, Latitude, Longitude, Type, Quantity from base_locations
where Region = "CONUS";

select sum(Quantity)
from base_locations
where Region = "CONUS";


select Name, State, Latitude, Longitude, Type, Quantity from base_locations
where Region = "OCONUS";

show create table base_locations;

CREATE TABLE 'base_locations'(
'Name' text,
'State' text
'Command' text,
'Region' text,
'Latitude' double DEFAULT NULL,
'Longitude' text,
'Type' text,
'Quantity' int(11) DEFAULT NULL
) ENGINE= InnoDB DEFAULT CHARSET =latin1;

select sum(Quantity)
from base_locations
where Region = "OCONUS"; 

select Name, State, Latitude, Longitude, Type, Quantity
from base_locations;

select Name, State, Latitude, Longitude, Type, Quantity
from base_locations
where Command = "FORSCOM";

select sum(Quantity)
from base_locations
where Command = "FORSCOM";

select Name, State, Latitude, Longitude, Type, Quantity
from base_locations
where Command = "USAPAC";

select sum(Quantity)
from base_locations
where Command = "USPSAC";

select Name, State, Latitude, Longitude, Type, Quantity
from base_locations
where Command = "TRADOC";

select sum(Quantity)
from base_locations
where Command = "TRADOC";

select Name, State, Latitude, Longitude, Type, Quantity
from base_locations
where Command = "Training";

select sum(Quantity)
from base_locations
where Command = "Training";

select Name, State, Latitude, Longitude, Type, Quantity
from base_locations
where Command = "ARNG";

select sum(Quantity)
from base_locations
where Command = "ARNG";





