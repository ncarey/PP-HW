import subprocess
from optparse import OptionParser


def make_clean_make():

  cmd = 'make clean'
  output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()
  print output
  cmd = 'make'
  output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()
  print output


def run_two():

  #map thread count to runtime
  data_first = {1:0, 2:0, 4:0, 8:0, 16:0}
  filter_first = {1:0, 2:0, 4:0, 8:0, 16:0}
  
  iterations = 20
  
  for i in range(0, iterations):
    print "Iteration {0}".format(i)
    run_two_helper(data_first, filter_first)


  for filt_len in data_first:
    data_first[filt_len] = data_first[filt_len] / iterations
  for filt_len in filter_first:
    filter_first[filt_len] = filter_first[filt_len] / iterations

  print data_first
  print filter_first

  t_w = ""
  d_w = ""
  f_w = ""
  for thread_c in data_first:
    if(data_first[thread_c] != 0):
      t_w += "{0},".format(thread_c)
      d_w += "{0},".format(data_first[thread_c])
      f_w += "{0},".format(filter_first[thread_c])

  
  with open('bench_data/thread_count.txt', 'w') as thread_file, open('bench_data/data.txt', 'w') as data_file, open('bench_data/filter.txt', 'w') as filt_file:
    thread_file.write(t_w[:-1])
    data_file.write(d_w[:-1])
    filt_file.write(f_w[:-1])


def run_one():

  #map filter length to runtime
  data_first = {1:0, 2:0, 4:0, 8:0, 16:0, 32:0, 64:0, 128:0, 256:0, 512:0, 1024:0, 2048:0, 4096:0}
  filter_first = {1:0, 2:0, 4:0, 8:0, 16:0, 32:0, 64:0, 128:0, 256:0, 512:0, 1024:0, 2048:0, 4096:0}

  iterations = 20

  for i in range(0, iterations):
    print "Iteration {0}".format(i)
    run_one_helper(data_first, filter_first)


  for filt_len in data_first:
    data_first[filt_len] = data_first[filt_len] / iterations
  for filt_len in filter_first:
    filter_first[filt_len] = filter_first[filt_len] / iterations

  print data_first
  print filter_first

  fl_w = ""
  d_w = ""
  f_w = ""
  for filt_len in data_first:
    if(data_first[filt_len] != 0):
      fl_w += "{0},".format(filt_len)
      d_w += "{0},".format(data_first[filt_len])
      f_w += "{0},".format(filter_first[filt_len])

  
  with open('bench_data/filt_len.txt', 'w') as filtlen_file, open('bench_data/data.txt', 'w') as data_file, open('bench_data/filter.txt', 'w') as filt_file:
    filtlen_file.write(fl_w[:-1])
    data_file.write(d_w[:-1])
    filt_file.write(f_w[:-1])

  #call_octave('gen_graph_one.m')

def call_octave(script_fn):
  cmd = 'octave graphs/{0}'.format(script_fn)
  subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()


def run_two_helper(data_first, filter_first):

  cmd = 'make run'
  output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()
  print output

  output_lines = output.split("\n")  
  #get rid of './filter' line
  del output_lines[0]

  for line in output_lines:
    split_line = line.split();
    if len(split_line) > 15 and not split_line[0] == "Serial":
      if split_line[1] == "data":
        data_first[int(split_line[15])] += float(split_line[4]) + (float(split_line[7]) / 1000000)
      elif split_line[1] == "filter":
        filter_first[int(split_line[15])] += float(split_line[4]) + (float(split_line[7]) / 1000000)
      else:
        print "Error: neither data nor filter..."
#    else:
#      print "Error, line does not conform to expectations: "
#      print line



def run_one_helper(data_first, filter_first):

  cmd = 'make run'
  output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()
  print output

  output_lines = output.split("\n")  
  #get rid of './filter' line
  del output_lines[0]

  for line in output_lines:
    split_line = line.split();
    if len(split_line) > 12:
      if split_line[1] == "data":
        data_first[int(split_line[12])] += float(split_line[4]) + (float(split_line[7]) / 1000000)
      elif split_line[1] == "filter":
        filter_first[int(split_line[12])] += float(split_line[4]) + (float(split_line[7]) / 1000000)
      else:
        print "Error: neither data nor filter..."
#    else:
#      print "Error, line does not conform to expectations: "
#      print line


if __name__ =='__main__':

  usage = "Usage: %prog [options]"
  parser = OptionParser(usage=usage)

  parser.add_option("-p", "--problem", type="string", dest="problem",
                     default="one", help="Select which problem to answer",
                     metavar="#PROB")


  (options, args) = parser.parse_args()

  make_clean_make()

  if options.problem == "one":
    run_one()
  elif options.problem == "two":
    run_two()

