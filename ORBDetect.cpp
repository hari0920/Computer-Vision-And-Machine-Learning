/*
Author: Hariharan Ramshankar
*/
#include "opencv2/video/tracking.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/features2d/features2d.hpp"
#include "opencv2/calib3d/calib3d.hpp"
#include "opencv2/opencv.hpp"
#include <iostream>
#include <vector>
using namespace cv;
using namespace std;
int main() {
	VideoCapture cap(0);   //webcam typically device ID 0.

	if (!cap.isOpened())
	{ //check if video device has been initialised
		std::cout << "cannot open device";
	}
	namedWindow("MyVideo", CV_WINDOW_AUTOSIZE); //named window creation.

	while (1)
	{
		Mat frame,greyscale, greyscale2,gr,nframe;

		bool bSuccess = cap.read(frame); // read a new frame from video

		if (!bSuccess) //if not success, break loop
		{
			std::cout << "Cannot read the frame from video file" << std::endl;
			break;
		}
		//if frame read is successful.
		cap >> nframe;
		cvtColor(frame, greyscale, CV_BGR2GRAY);
		cvtColor(nframe, greyscale2, CV_BGR2GRAY);

		vector<KeyPoint> keypoints_initial;
		cv::Ptr<Feature2D> detector = ORB::create();
		Mat descriptor_initial;
		detector->detect(greyscale, keypoints_initial);
		detector->compute(greyscale, keypoints_initial, descriptor_initial);
		Mat im2;
		drawKeypoints(greyscale, keypoints_initial, greyscale, cv::Scalar(0, 255, 255));
		imshow("MyVideo", greyscale); //show the frame in "MyVideo" window
		if (waitKey(30) == 27) //wait for 'esc' key press for 30 ms. If 'esc' key is pressed, break loop
		{
			std::cout << "esc key is pressed by user" << std::endl;
			break;
		}
	}

	return 0;

}
