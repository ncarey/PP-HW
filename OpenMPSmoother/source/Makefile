all: filterOpt

filter:
	gcc -o filter filter.c -std=c99 -fopenmp

filterOpt:
	gcc -o filter filter.c -std=c99 -fopenmp -O3

run:
	./filter

clean:
	rm -rf *o filter
