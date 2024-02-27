#!/usr/bin/env ruby
# Regular expression matches sender phone number or name (including country code if present), receiver phone number or name (including country code if present) and flags used in a log file.

sender = ARGV[0].match(/\[from:([^\]]+)\]/)&.captures&.first
recepient = ARGV[0].match(/\[to:([^\]]+)\]/)&.captures&.first
flag = ARGV[0].match(/\[flags:([^\]]+)\]/)&.captures&.first

puts "#{sender},#{recepient},#{flag}"
