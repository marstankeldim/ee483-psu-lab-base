#!/usr/bin/env python3

import rospy
from duckietown_msgs.msg import WheelsCmdStamped


class MMDriverNode:
    def __init__(self):
        vehicle_name = rospy.get_param("~veh")
        topic = f"/{vehicle_name}/wheels_driver_node/wheels_cmd"
        self.pub = rospy.Publisher(topic, WheelsCmdStamped, queue_size=1)
        self.rate = rospy.Rate(rospy.get_param("~rate", 10))
        self.vel_left = rospy.get_param("~vel_left", 0.25)
        self.vel_right = rospy.get_param("~vel_right", 0.25)

    def run(self):
        rospy.loginfo("Publishing wheel commands")
        while not rospy.is_shutdown():
            msg = WheelsCmdStamped()
            msg.header.stamp = rospy.Time.now()
            msg.vel_left = self.vel_left
            msg.vel_right = self.vel_right
            self.pub.publish(msg)
            self.rate.sleep()


if __name__ == "__main__":
    rospy.init_node("driver_node", anonymous=False)
    node = MMDriverNode()
    node.run()
