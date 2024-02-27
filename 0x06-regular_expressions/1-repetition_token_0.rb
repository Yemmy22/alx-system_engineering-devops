#!/usr/bin/env ruby
# The regular expression matches any string starting with a single occurence of 'h' followed by a single occurence of 'b'; two - five occurrence of 't' and ends with an 'n'. 
puts ARGV[0].scan(/^hbt{2,5}n$/).join

