**The xenial-kinetic branch is currently being restructured to make it easier to adapt to custom InMoov designs.**  

Please check the xenial-kinetic milestones to see the direction we're heading and our status
https://github.com/alansrobotlab/inmoov_ros/milestones/xenial_kinetic

These are massive changes to the framework, but once it's all in, it will be alot easier to set up ROS with your specific robot.  Stay tuned!

Until then, once you have the packages installed, the following commands should work:
 - roslaunch inmoov_description display.launch (to pull up the rviz urdf model)
 - (the rest is currently hard coded to one robot, we're working on that)

## Alan's InMoov ROS Introduction
![enter image description here](http://i.imgur.com/bweApZH.png)


---------

### What Is It?
This is a ROS software stack that connects a dedicated PC to an InMoov robot.  
It currently implements the following:

 - a fully articulated URDF model of InMoov
 - inmoov firmware that integrates rossserial_arduino for communication
 - inmoov_msgs that define communication between host pc and arduino
 - trainer module to set arduino eeprom values and calibrate each servo

### What You Need To Get Started
> This works with a specific technology stack.  It can be run natively on a PC, or in VMWare Player.  Everything is tied to compatibility with MoveIt!.  
>  
> MoveIt! is currently available for ROS Kinetic, and Kinetic is tied to Ubuntu 16.04 LTS, so everything fits together from there.  
>   
> Follow Install Instrucktions they help alot

#### What you'll need:

 - VMWare Player (optional)
 (https://my.vmware.com/en/web/vmware/free#desktop_end_user_computing/vmware_workstation_player/12_0)
 - Ubuntu 16.04 LTS (http://www.ubuntu.com/download/alternative-downloads) 
 - ROS Kinetic (http://wiki.ros.org/indigo/Installation/Ubuntu)
 - MoveIt! (http://moveit.ros.org/install/)

### How to Install It:
Copy these packages into your {inmoov_ros}/src folder
Run the following commands from the root of your {inmoov_ros} folder:
  
    catkin_make              #build/rebuild all projects
    source devel/setup.bash  #let ROS know about all of your new packages you can also use . instead of source

### How to use it:
Run the following commands:

    rosrun inmoov_tools setup_parameters.py        #loads parameters into server
    roslaunch inmoov_tools servobus.launch       #launches arduino interfaces
    roslaunch inmoov_description display.launch  #launches rviz
    rosrun inmoov_tools trainer.py               #launches trainer module


### Next Steps (todo list)
 - urdf:  fix right shoulder out rotation
 - urdf:  fix right wrist rotation
 - trainer:  move all arduino communication to service calls
 - trainer:  only publish joint commands to joint_command topic
 - node:  write node that sends joint commands to arduino through service calls
 - pose:  migrate pose module to pyqt4
 - headdemo:  migrate headdemo module to pyqt4
### Package list:
These are the packages that have been installed on my PC most should 
be installed during the setup guides and tutorials for installing Moveit, ROS-Kinetic.

apt-get:

 arduino 
 dkms
 qt5-default 
 qtcreator
 clang-format-3.8 
 ros-kinetic-desktop-full
 ros-kinetic-rqt
 ros-kinetic-rqt-common-plugins
 ros-kinetic-moveit
 ros-kinetic-rosserial-arduino
 ros-kinetic-rosserial
 ros-kinetic-xarco
 ros-kinetic-opencv3
 ros-kinetic-cv-bridge
 ros-kinetic-compressed-depth-image-tansport
 ros-kinetic-compressed-image-transport
 ros-kinetic-usb-cam 
 ros-kinetic-pyros
 liburdfdom-tools
 python-wstool
 python-catkin-tools
 python-pip
 
pip:

 pip install qdarkstyle
 
 ### Usefull Links:
 https://github.com/ubi-agni/dexterous-manipulation-tutorial/wiki
 https://github.com/guihomework/dexterous-manipulation-tutorial/wiki/tuto-prep-part1