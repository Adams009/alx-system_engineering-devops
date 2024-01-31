#!/usr/bin/env ruby

def match_repetition_token_0(arg)
  puts arg.match(/hb{0,}tn/) ? arg : ""
end

if ARGV.length == 1
  match_repetition_token_0(ARGV[0])
else
  puts "Usage: #{$PROGRAM_NAME} <string>"
end
