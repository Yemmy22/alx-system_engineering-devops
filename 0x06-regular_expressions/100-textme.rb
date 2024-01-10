#!/usr/bin/env ruby
# Matches token with a repeated character

input_line = ARGV[0]

sender = input_line.match(/\[from:([^\]]+)\]/)&.captures&.first
receiver = input_line.match(/\[to:([^\]]+)\]/)&.captures&.first
flags = input_line.match(/\[flags:([^\]]+)\]/)&.captures&.first

puts "#{sender},#{receiver},#{flags}" if sender && receiver && flags
