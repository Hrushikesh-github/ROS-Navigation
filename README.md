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

RTAB-Map (Real-Time Appearance-Based Mapping) is a RGB-D SLAM approach based on a loop closure detector. The loop closure detector uses a bag-of-words approach in order to determinate if a new image detected by an RGB-D sensor is from a new location or from a location that it has been already visited.The rtabmap_ros package is an implementation in ROS of the RTAB-Map approach.
Requirements for RTAB are: 
A 2D laser which provides sensor_msgs/LaserScan messages.
Odometry (IMU, wheel encoders, ...) which provides a nav_msgs/Odometry message.
A calibrated Kinect-like sensor compatible with openni_launch, openni2_launch or freenect_launch ros packages.

### Turtlebot in a environment
<img width="910" alt="sensors_rviz" src="https://user-images.githubusercontent.com/56476887/85308567-f7178d80-b4ce-11ea-80ff-4dedc0059bf2.png">
![RTAB_gazebo](https://user-images.githubusercontent.com/56476887/85308563-f67ef700-b4ce-11ea-86e4-24026a1fb5b7.png)

overlapping yellow disks are marking/highlightning the key features of each image.This visual features used by RTAB-Map are using some popular techniques from computer vision including like SIFT, SURF, BRIEF, FAST, BRISK, ORB or FREAK. 
pink discs indicate visual features that two images have in common

![rtab_database](https://user-images.githubusercontent.com/56476887/85308559-f67ef700-b4ce-11ea-97cc-1adae002dd85.png)
<img width="912" alt="database1" src="https://user-images.githubusercontent.com/56476887/85310014-17e0e280-b4d1-11ea-8bdd-b2860b2f3b4e.png">

### Autonomous localization with RTAB
![map_rtab2](https://user-images.githubusercontent.com/56476887/85308553-f41c9d00-b4ce-11ea-8501-8b949a51f639.png)
![rtab_map](https://user-images.githubusercontent.com/56476887/85308556-f5e66080-b4ce-11ea-9316-92a3f3301f28.png)


More content on RTAB can be found in one of my forked repositories
