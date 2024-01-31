#!/usr/bin/env ruby

def match_school(arg)
  puts arg.match(/School\z/) ? "School$" : "$"
end

if ARGV.length == 1
  match_school(ARGV[0])
else
  puts "Usage: #{$PROGRAM_NAME} <string>"
end
