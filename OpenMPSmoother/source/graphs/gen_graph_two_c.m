
log_axis_label = [1,2,4,8,16,32,64,128]

filt_len = dlmread('bench_data/thread_count.txt',',')
filt = dlmread('bench_data/filter.txt',',')
data = dlmread('bench_data/data.txt',',')

x = filt_len
y = [filt;data]

plot(x,y)

set(gca, 'Xscale', 'log')
set(gca, 'Xtick', log_axis_label)
set(gca, 'Xticklabel', log_axis_label)
xlabel('Scaleup Factor (Scaleup Factor = # Threads and DATA LEN = Scaleup Factor * Starting DATA LEN)')

ylabel('Runtime in Seconds (log scale)')
set(gca, 'Yscale', 'log')
set(gca, 'Ytick', log_axis_label)
set(gca, 'Yticklabel', log_axis_label)
title('2c: Scaleup, or Runtime as a Function of Number of Threads and Data Length')

legend('filter first','data first');

print -dpng graphs/2c.png

