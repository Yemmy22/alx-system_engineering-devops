#!/usr/bin/env ruby
# Regular expression matches a specified string with a single or more occurrences of 't'.
puts ARGV[0].scan(/^hbt+n$/).join
