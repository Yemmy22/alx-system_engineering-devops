#!/usr/bin/env ruby
# Regular Expression matches any string of 10 digit numbers
puts ARGV[0].scan(/^\d{10,10}$/).join

