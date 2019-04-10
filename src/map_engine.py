import rospy
import numpy as np
import os
import sys
import cv2
from cv_bridge import CvBridge
from std_msgs.msg import String
from sensor_msgs.msg import Image
from sensor_msgs.msg import PointCloud, ChannelFloat32
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')

'''
Real time semantic map generator engine, including publisher and subscriper port for ros.
Haven't tested yet.
'''
class map_engine:
    def __init__(self):
        self._cv_bridge = CvBridge()
        self._sub = rospy.Subscriber('categorymap', Image, self.callback, queue_size = 1000)
        self._sub1 = rospy.Subscriber('KeyPoints', PointCloud, self.callback1, queue_size = 1000)
        self._sub2 = rospy.Subscriber('MapPoints', PointCloud, self.callback2, queue_size = 1000)
        self._pub = rospy.Publisher('Semantic_Map', PointCloud, queue_size=1)
        self._currentframe = Image()
        self._mp = PointCloud()
        self._kp = PointCloud()
        self.smp = PointCloud()
        self.smp.channels = [ChannelFloat32()]
        self.smp.channels[0].name = 'rgb8'

    def callback(self, image_msg):
        self._currentframe = image_msg

    def callback1(self, pointcloud_msg):
        self._kp = pointcloud_msg
        cv_image = self._cv_bridge.imgmsg_to_cv2(self._currentframe)
        print("keypoints size", np.shape(self._kp.points))
        print("mappoints size", np.shape(self._mp.points))
        for i in self._kp.points:
            '''
            a = int(i.x)
            b = int(i.y)
            c = int(i.z)
            '''
            cate = cv_image[int(i.y),int(i.x)]
            ii = self.sorting(self._mp.channels[0].values, int(i.z))
            if ii!=-1:
                self.smp.channels[0].values[ii] = cate * 100
            '''
            if cv_image[b,a] == 2:
                index = self.sorting(self._mp.channels[0].values, c)
                self.smp.points.append(self._mp.points[index])'''
        self.smp.header = self._mp.header
        self._pub.publish(self.smp)
    
    def callback2(self, pointcloud_msg):
        self._mp = pointcloud_msg
        self.smp.channels[0].values += [0]*(np.size(self._mp.channels[0].values)-np.size(self.smp.channels[0].values))
        self.smp.points = self._mp.points
    
    def sorting(self, msg, value):
        if msg.index(value):
            return msg.index(value)
        else:
            return -1
    
    def main(self):
        rospy.spin()
    
if __name__ == '__main__':
    rospy.init_node('map_engine')
    engine = map_engine()
    engine.main()
    
