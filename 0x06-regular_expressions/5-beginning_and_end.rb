#!/usr/bin/env ruby
# Regular expression matches any string beginning with a single 'h', followed by any single character and ends with a single 'n'
puts ARGV[0].scan(/^h(.)n$/).join

