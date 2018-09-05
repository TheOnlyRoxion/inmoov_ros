



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
#include <sensor_msgs/JointState.h>
#include <Servo.h>
//#include "InmoovTranslator.h"

ros::NodeHandle  nh;

//using inmoov_controls::InmoovTranslator;

//declaring Service
//ros::ServiceClient<InmoovTranslator::Request, InmoovTranslator::Response> client("inmoov_translator");
//InmoovTranslator::Request req;
//InmoovTranslator::Response res;


Servo servo;
//funktion which is called after joint state message is recived
void servo_cb( const sensor_msgs::JointState& cmd_msg) {
  servo.attach(3);
  servo.write(30); //set servo angle, should be from 0-180
  digitalWrite(13, HIGH - digitalRead(13)); //toggle led #

}

//declaring subsriber to joint states
ros::Subscriber<sensor_msgs::JointState> sub("joint_states", servo_cb);

void setup() {
  pinMode(13, OUTPUT);

  nh.initNode();
  nh.subscribe(sub);
  //nh.serviceClient(client);
  
  //req.joint = "fetch_all";
  //client.call(req, res);
  //int h = res.pin;


   servo.attach(3);//attach it to pin 3

  servo.write(30);
  nh.loginfo("Test 30");
  delay(1000);
  servo.write(160);
  nh.loginfo("Test 160");
  delay(1000);
  nh.loginfo("Startup complete");
}


void loop() {
  nh.spinOnce();
  delay(1);
}
