
log_axis_label = [1,2,4,8,16]

filt_len = dlmread('bench_data/thread_count.txt',',')
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
title('2a: Speedup, or Runtime as a Function of Thread Count')

legend('filter first','data first');

print -dpng graphs/2a.png

