#!/usr/bin/env ruby
#Bash script that find the correct regular expression
puts ARGV[0].scan(/hbt{2,5}n/).join
