#include"System.h"
using namespace std;
namespace DeepSLAM
{
bool System::Initialize()
{
    cout<<"Initializing System"<<endl;
    DisplayVideo();
    return true;
}
void System::DisplayVideo()
{
    //Open Webcam,Display Video frames
    cv::VideoCapture cap(0);
    if(!cap.isOpened())
    {
        cout<<"Unable to read video!"<<endl;
        exit(1);
    }
    cv::Mat frame;
    cv::namedWindow("Frames");
    while(cap.read(frame))
    {
        cv::imshow("Frames",frame);
        if (cv::waitKey(25) == 'q')
        {
                break;
        }
    }
}

}//end DeepSLAM