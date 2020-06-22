# ROS-Navigation
These packages use the move base package for navigation. AMCL for localization and gmapping for mapping.
Codes written in python and simulations were done in gazebo. 
Husky robot was used in navigation from scratch. The following procedures are map creation, localization and path planning

### husky in it's environment
![husky_in_room](https://user-images.githubusercontent.com/56476887/85301984-2d044400-b4c6-11ea-940b-04bb1cee70e1.png)

### map creation
<img width="965" alt="turtlebot_maxurange_2" src="https://user-images.githubusercontent.com/56476887/85300974-e3672980-b4c4-11ea-8bdb-a4bc0cf307df.png">

### initally particleclouds dispersed, achieved using /global_localization service
<img width="966" alt="rviz_particles_dispersed" src="https://user-images.githubusercontent.com/56476887/85300994-e7934700-b4c4-11ea-962e-8770ff84d0c1.png">

### AMCL node for localization
<img width="965" alt="husky_localization2" src="https://user-images.githubusercontent.com/56476887/85300991-e6621a00-b4c4-11ea-9ffd-8f22bb5ca8b7.png">

### The global costmap
<img width="967" alt="rviz_global_costmap" src="https://user-images.githubusercontent.com/56476887/85301008-ec57fb00-b4c4-11ea-80f5-c9765127737c.png">
### The local costmap
<img width="964" alt="rviz_local_costmap" src="https://user-images.githubusercontent.com/56476887/85301007-eb26ce00-b4c4-11ea-9835-b622e528e608.png">

### The global map changes when new object is introduced 
But for this to work, proper configuration must be done
<img width="548" alt="nav_object_detected2" src="https://user-images.githubusercontent.com/56476887/85300999-e8c47400-b4c4-11ea-870b-6bc2a61e5d1b.png">

### SummitXL in a room
![summit_xl](https://user-images.githubusercontent.com/56476887/85306318-efa2b500-b4cb-11ea-854b-02c2e7dd0413.png)

### Creating map
<img width="963" alt="max_urange_7" src="https://user-images.githubusercontent.com/56476887/85306339-f29da580-b4cb-11ea-9a5e-23e5ca6ed035.png">

### Map of the room
![fetch_map](https://user-images.githubusercontent.com/56476887/85306337-f29da580-b4cb-11ea-99de-a81cbeed5e07.png)

### AMCL localization
<img width="964" alt="summit_localization3" src="https://user-images.githubusercontent.com/56476887/85306334-f2050f00-b4cb-11ea-8c1d-475eca59dbbe.png">

### Green line shows the local plan
<img width="964" alt="summit_planning1" src="https://user-images.githubusercontent.com/56476887/85306326-f0d3e200-b4cb-11ea-8f2b-9bb34de76904.png">



