/*
Main File for the constituent systems:
Author:Hariharan Ramshankar
*/
#ifndef SYSTEM_H
#define SYSTEM_H
#include <vector>
#include <iostream>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string>
#include <thread>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui.hpp>

namespace DeepSLAM
{
class System
{
    public:
    bool Initialize();

    private:
    void DisplayVideo();
    
};

} // namespace DeepSLAM

#endif // SYSTEM_H