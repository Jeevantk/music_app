#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <iostream>
#include <stdio.h>

using namespace std;
using namespace cv;

int main()
{
  Mat img=imread("images.jpeg",0);
  Mat thresh;
  adaptiveThreshold(img,thresh, 255,CV_ADAPTIVE_THRESH_MEAN_C,CV_THRESH_BINARY,13, 1 );
  imshow("Thresholded Image",thresh);
  waitKey(0);
}
