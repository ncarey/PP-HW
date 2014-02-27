
log_axis_label = [.0625,.125,.25,.5,1,2,4,8,16,32,64,128,256,512,1024,2048,4096]

filt_len = dlmread('bench_data/filt_len.txt',',')
filt = dlmread('bench_data/filter.txt',',')
data = dlmread('bench_data/data.txt',',')

x = filt_len
y = [filt;data]

plot(x,y)

set(gca, 'Xscale', 'log')
set(gca, 'Xtick', log_axis_label)
set(gca, 'Xticklabel', log_axis_label)
xlabel('Filter Length (log scale)')

ylabel('Runtime in Seconds (log scale)')
set(gca, 'Yscale', 'log')
set(gca, 'Ytick', log_axis_label)
set(gca, 'Yticklabel', log_axis_label)
title('1a: Runtime as a Function of Filter Size')

legend('filter first','data first');

print -dpng graphs/1a.png


data_len = 512*512*128
norm_filt = (filt_len * data_len) ./ filt
norm_data = (filt_len * data_len) ./ data

x = filt_len
y = [norm_filt;norm_data]

plot(x,y)

set(gca, 'Xscale', 'log')
set(gca, 'Xtick', log_axis_label)
set(gca, 'Xticklabel', log_axis_label)
xlabel('Filter Length (log scale)')

ylabel('Operations per Second (filter length * data length / runtime)')
title('1b: Operations per Second as a Function of Filter Size')

legend('filter first','data first');


print -dpng graphs/1b.png

