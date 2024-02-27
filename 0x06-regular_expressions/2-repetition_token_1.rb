#!/usr/bin/env ruby
# Regular expression matches any string starting h(single occurrence), b(0 or 1 occurence), t(single occurrence) and ends with n(single occorrence)
puts ARGV[0].scan(/^h(b?)tn$/).join

