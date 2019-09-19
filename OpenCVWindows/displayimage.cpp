#include <opencv2/opencv.hpp>
#include <stdio.h>

int main(void)
{
	std::cout << "Simple Program to display an image" << std::endl;
	cv::Mat inputImage = cv::imread("..\\..\\..\\modifiedtower2.jpg");
	cv::imshow("inputImage", inputImage);
	cv::waitKey(100);
	std::getchar();
	return 0;
}