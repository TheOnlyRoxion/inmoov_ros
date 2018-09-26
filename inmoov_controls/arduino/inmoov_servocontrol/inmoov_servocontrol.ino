



/*
   rosserial Servo Control Example

   This sketch demonstrates the control of hobby R/C servos
   using ROS and the arduiono

   For the full tutorial write up, visit
   www.ros.org/wiki/rosserial_arduino_demos

   For more information on the Arduino Servo Library
   Checkout :
   http://www.arduino.cc/en/Reference/Servo
*/

//#if (ARDUINO >= 100)
#include <Arduino.h>
//#else
// #include <WProgram.h>
//#endif


#include <ros.h>
//#include <sensor_msgs/JointState.h>
#include <inmoov_msgs/MotorCommand.h>
#include <Servo.h>
//#include "InmoovTranslator.h"

ros::NodeHandle  nh;

//using inmoov_controls::InmoovTranslator;

//declaring Service
//ros::ServiceClient<InmoovTranslator::Request, InmoovTranslator::Response> client("inmoov_translator");
//InmoovTranslator::Request req;
//InmoovTranslator::Response res;

const int maxServoCount = 13;
Servo _servo[maxServoCount];


//funktion which is called after joint state message is recived
void servo_cb( const inmoov_msgs::MotorCommand& cmd_msg) {

  _servo[cmd_msg.id].write(cmd_msg.value);

  digitalWrite(13, HIGH - digitalRead(13)); //toggle led #
  //nh.loginfo("Message recived");
}

//declaring subsriber to joint states
ros::Subscriber<inmoov_msgs::MotorCommand> sub("joint_states_r", servo_cb);

void setup() {
  pinMode(13, OUTPUT);

  for (int i = 0; i < maxServoCount; ++i)
    _servo[i].attach(i);



  nh.initNode();
  nh.subscribe(sub);
  nh.loginfo("Startup complete");

}


void loop() {
  nh.spinOnce();
  //delay(1);
}
