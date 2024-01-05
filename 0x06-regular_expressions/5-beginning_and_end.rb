#!/usr/bin/env ruby
# Matches token starting wth h, and any single charcater and ends with n
puts ARGV[0].scan(/h.n/).join
