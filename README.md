# ROS-Navigation
These packages use the move base package for navigation. AMCL for localization and gmapping for mapping.
Codes written in python and simulations were done in gazebo. 
Husky robot was used in navigation from scratch. The following procedures are map creation, localization and path planning

### husky in it's environment


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



