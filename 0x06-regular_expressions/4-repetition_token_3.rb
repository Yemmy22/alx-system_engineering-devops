#!/usr/bin/env ruby
# Regular Expression matches any string starting with single occurrence of 'h' and 'b' followed by 0 or more occurrences of 't' and ends with a single occurrence of 'n'.
puts ARGV[0].scan(/^hbt*n$/).join
