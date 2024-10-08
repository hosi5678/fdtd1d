#include <iostream>
using namespace std;

#include <vector>
#include <numeric>
#include <sstream>
#include <iomanip>
#include <time.h>

#include "sub_dir/include/vec1d.hpp"
#include "sub_dir/include/parameter.hpp"
#include "sub_dir/include/set_coef_1d.hpp"
#include "sub_dir/include/fttd_1d.hpp"
#include "sub_dir/include/fft.hpp"

#include "matplotlib-cpp/matplotlibcpp.h"

namespace plt=matplotlibcpp;

int main(void){

    time_t _start,_end;

    _start=clock();

    // 励起波形の選択とsin波形の角周波数の選択
    // int excite_mode=gaussian_pulse;
    int excite_mode=sinwave;

    int _freq_num=192;

    fdtd_1d fdtd(excite_mode,_freq_num);

    if (excite_mode==gaussian_pulse) {
        std::vector<double> _wave=fdtd.get_vector();

        vec1d wave=_wave;

        wave.createFile(20,"csv_files","pre_fft_wave.csv");

        fft fft(_wave);

        std::vector<double> peak=fft.fft_get_peak();

        std::cout << "(in main) get_peak() :" << std::endl;
        vec1d _peak=peak;
        _peak.show(0);

        _peak.createFile(0,"csv_files","gaussian_fft_peak_number.txt");

    }

    _end=clock();

    std::cout << "clock:" << (_end - _start) << std::endl;
    std::cout << "processing time: " << 1000*(double)(_end - _start)/(double)CLOCKS_PER_SEC << " [msec]. " << std::endl;

    return 0;

}

    // vector<double> x{ 1, 2, 3, 4 };
    // vector<double> y{ 3, 4, 6, 8 };

    // x.push_back(5.0);
    // y.push_back(9.0);

    // plt::title("Plot Test");
    // plt::suptitle("timestep=5");

    // plt::plot(x,y);
    // plt::save("./pngs/test.png");

    // plt::clf();
    // plt::close();
