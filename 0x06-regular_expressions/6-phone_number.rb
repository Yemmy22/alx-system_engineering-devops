#!/usr/bin/env ruby
# Matches match a 10 digit token with repeated characters
puts ARGV[0].scan(/^\d{10,10}$/).join
