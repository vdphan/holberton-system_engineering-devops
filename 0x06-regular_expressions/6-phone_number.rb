#!/usr/bin/env ruby
#Bash script that find the correct regular expression
puts ARGV[0].scan(/\A\d{10}/).join