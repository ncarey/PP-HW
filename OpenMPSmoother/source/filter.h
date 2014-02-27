#ifndef _h_filter
#define _h_filter

#include<stdint.h>

int timeval_subtract (struct timeval * result, struct timeval * x, struct timeval * y);
void serialFilterFirst ( int data_len, unsigned int* input_array, unsigned int* output_array, int filter_len, unsigned int* filter_list );
void serialDataFirst ( int data_len, unsigned int* input_array, unsigned int* output_array, int filter_len, unsigned int* filter_list );
void parallelFilterFirst ( int data_len, unsigned int* input_array, unsigned int* output_array, int filter_len, unsigned int* filter_list, int num_threads );
void parallelDataFirst ( int data_len, unsigned int* input_array, unsigned int* output_array, int filter_len, unsigned int* filter_list, int num_threads );
void checkData ( unsigned int * serialarray, unsigned int * parallelarray );
int posix_memalign (void **, size_t, size_t);
void parallelDataFirstOptimized ( int data_len, unsigned int* input_array, unsigned int* output_array, int filter_len, unsigned int* filter_list, int num_threads );

#endif
