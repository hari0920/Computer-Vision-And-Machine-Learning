//Basic cartoonifier application for desktop and webcam
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <iostream>
#include <opencv2\imgproc\imgproc.hpp>
#include "opencv2/opencv.hpp"
Mat smallImg;
Size smallSize;
using namespace std;
using namespace cv;
//function that returns the cartoonified image taking 2 arguments
void cartoonifyImage(Mat srcColor, Mat dst, char evil)
{
	Mat gray;
	Mat mask;
	cvtColor(srcColor, gray, CV_BGR2GRAY);//convert to grayscale
	const int MEDIAN_BLUR_FILTER_SIZE = 7;
	medianBlur(gray, gray, MEDIAN_BLUR_FILTER_SIZE);//apply median filter
	Mat edges, edges2;
	if ((evil == 'y') || (evil == 'Y'))
	{//evil mask
		Scharr(gray, edges, CV_8U, 1, 0);
		Scharr(gray, edges2, CV_8U, 1, 0, -1);
		edges += edges2;     // Combine the x & y edges together.
		const int EVIL_EDGE_THRESHOLD = 12;
		threshold(edges, mask, EVIL_EDGE_THRESHOLD, 255, THRESH_BINARY_INV);
		medianBlur(mask, mask, 3);
		Mat bigImg=Mat(srcColor.size(),CV_8UC3);
		dst.setTo(0);
		bigImg.copyTo(dst, mask);
		//
	}
	else
	{
	const int LAPLACIAN_FILTER_SIZE = 5;
	Laplacian(gray, edges, CV_8U, LAPLACIAN_FILTER_SIZE);//Laplacian filter
	
	const int EDGES_THRESHOLD = 80;
	threshold(edges, mask, EDGES_THRESHOLD, 255, THRESH_BINARY_INV);
	
		Size size = srcColor.size();
		
		smallSize.width = size.width / 2;
		smallSize.height = size.height / 2;
		Mat smallImg = Mat(smallSize, CV_8UC3);
		resize(srcColor, smallImg, smallSize, 0, 0, INTER_LINEAR);
		Mat tmp = Mat(smallSize, CV_8UC3);
		int repetitions = 7;  // Repetitions for strong cartoon effect.
		for (int i = 0; i < repetitions; i++)
		{
			int ksize = 9;     // Filter size. Has a large effect on speed.
			double sigmaColor = 9;    // Filter color strength.
			double sigmaSpace = 7;    // Spatial strength. Affects speed.
			bilateralFilter(smallImg, tmp, ksize, sigmaColor, sigmaSpace);
			bilateralFilter(tmp, smallImg, ksize, sigmaColor, sigmaSpace);
		}
		Mat bigImg;
		resize(smallImg, bigImg, size, 0, 0, INTER_LINEAR);
		dst.setTo(0);
		bigImg.copyTo(dst, mask);
	}
}
void main()
{
	// Get access to the camera.
	cv::VideoCapture camera;
	camera.open(0);
	if (!camera.isOpened()) 
	{
		cout<< "ERROR: Could not access the camera or video!" <<endl;
		exit(1);
	}

	// Try to set the camera resolution.
	//camera.set(CV_CAP_PROP_FRAME_WIDTH, 320);
	//camera.set(CV_CAP_PROP_FRAME_HEIGHT, 240);

	//Now grab frames in a Mat container
	char evil;
	cout << "Evil needed??" << endl;
	cin >> evil;
	while (true)
	{
		Mat frame;
		camera >> frame;
		if (frame.empty())
		{
			cout << "Frame couldn't be captured :(" << endl;
			break;
		}
		Mat displayedframe(frame.size(), CV_8UC3);
		// Draw the color face onto a black background.
		Size size=frame.size();
		Mat faceOutline = Mat::zeros(size, CV_8UC3);
		Scalar color = CV_RGB(255, 255, 0);    // Yellow.
		int thickness = 4;
		// Use 70% of the screen height as the face height.
		int sw = size.width;
		int sh = size.height;
		int faceH = sh / 2 * 70 / 100;  // "faceH" is the radius of the ellipse.
		// Scale the width to be the same shape for any screen width. 
		int faceW = faceH * 72/100;
		// Draw the face outline.
		ellipse(faceOutline, Point(sw / 2, sh / 2), Size(faceW, faceH),	0, 0, 360, color, thickness, CV_AA);
		// Draw the eye outlines, as 2 arcs per eye.
		int eyeW = faceW * 23 / 100;
		int eyeH = faceH * 11 / 100;
		int eyeX = faceW * 48 / 100;
		int eyeY = faceH * 13 / 100;
		Size eyeSize = Size(eyeW, eyeH);
		// Set the angle and shift for the eye half ellipses.
		int eyeA = 15; // angle in degrees.
		int eyeYshift = 11;
		// Draw the top of the right eye.
		ellipse(faceOutline, Point(sw / 2 - eyeX, (sh / 2)-eyeY),eyeSize, 0, 180 + eyeA, 360 - eyeA, color, thickness, CV_AA);
		// Draw the bottom of the right eye.
		ellipse(faceOutline, Point(sw / 2 - eyeX, (sh / 2) - eyeY - eyeYshift),eyeSize, 0, 0 + eyeA, 180 - eyeA, color, thickness, CV_AA);
		// Draw the top of the left eye.
		ellipse(faceOutline, Point(sw / 2 + eyeX, sh / 2 - eyeY),eyeSize, 0, 180 + eyeA, 360 - eyeA, color, thickness, CV_AA);
		// Draw the bottom of the left eye.
		ellipse(faceOutline, Point(sw / 2 + eyeX, sh / 2 - eyeY - eyeYshift),eyeSize, 0, 0 + eyeA, 180 - eyeA, color, thickness, CV_AA);
		// Draw the bottom lip of the mouth.
		int mouthY = faceH * 48 / 100;
		int mouthW = faceW * 45 / 100;
		int mouthH = faceH * 6 / 100;
		ellipse(faceOutline, Point(sw / 2, sh / 2 + mouthY), Size(mouthW,mouthH), 0, 0, 180, color, thickness, CV_AA);
		// Draw anti-aliased text.
		int fontFace = FONT_HERSHEY_COMPLEX;
		float fontScale = 1.0f;
		int fontThickness = 2;
		char *szMsg = "Put your face here";
		cartoonifyImage(frame, displayedframe, evil);
		putText(faceOutline, szMsg, Point(sw * 23 / 100, sh * 10 / 100),fontFace, fontScale, color, fontThickness, CV_AA);
		addWeighted(displayedframe, 1.0, faceOutline, 0.7, 0, displayedframe, CV_8UC3);
		//for skin detection, converting colour space from RGB to YCbCr
		Mat yuv = Mat(smallSize, CV_8UC3);
		cvtColor(smallImg, yuv, CV_BGR2YCrCb);
		int sw = smallSize.width;
		int sh = smallSize.height;
		Mat mask, maskPlusBorder;
		maskPlusBorder = Mat::zeros(sh + 2, sw + 2, CV_8UC1);
		mask = maskPlusBorder(Rect(1, 1, sw, sh)); // mask is in maskPlusBorder.
		resize(edge, mask, smallSize);         // Put edges in both of them.
		const int EDGES_THRESHOLD = 80;
		threshold(mask, mask, EDGES_THRESHOLD, 255, THRESH_BINARY);
		dilate(mask, mask, Mat());
		erode(mask, mask, Mat());
		int const NUM_SKIN_POINTS = 6;
		Point skinPts[NUM_SKIN_POINTS];
		skinPts[0] = Point(sw / 2, sh / 2 - sh / 6);
		skinPts[1] = Point(sw / 2 - sw / 11, sh / 2 - sh / 6);
		skinPts[2] = Point(sw / 2 + sw / 11, sh / 2 - sh / 6);
		skinPts[3] = Point(sw / 2, sh / 2 + sh / 16);
		skinPts[4] = Point(sw / 2 - sw / 9, sh / 2 + sh / 16);
		skinPts[5] = Point(sw / 2 + sw / 9, sh / 2 + sh / 16);
		const int LOWER_Y = 60;
		const int UPPER_Y = 80;
		const int LOWER_Cr = 25;
		const int UPPER_Cr = 15;
		const int LOWER_Cb = 20;
		const int UPPER_Cb = 15;
		Scalar lowerDiff = Scalar(LOWER_Y, LOWER_Cr, LOWER_Cb);
		Scalar upperDiff = Scalar(UPPER_Y, UPPER_Cr, UPPER_Cb);
		const int CONNECTED_COMPONENTS = 4;  // To fill diagonally, use 8.
		const int flags = CONNECTED_COMPONENTS | FLOODFILL_FIXED_RANGE | FLOODFILL_MASK_ONLY;
		Mat edgeMask = mask.clone();    // Keep a copy of the edge mask.
		// "maskPlusBorder" is initialized with edges to block floodFill().
		for (int i = 0; i< NUM_SKIN_POINTS; i++) {
			floodFill(yuv, maskPlusBorder, skinPts[i], Scalar(), NULL,lowerDiff, upperDiff, flags);
		}
		mask -= edgeMask;
		Mat smallImgBGR;
		int Red = 0;
		int Green = 70;
		int Blue = 0;
		add(smallImgBGR, Scalar(Blue, Green, Red), smallImgBGR, mask);
		imshow("Cartoonifier!", displayedframe);
		char keypress = waitKey(20);
		if (keypress == 27){ break; }
	}
}
	

