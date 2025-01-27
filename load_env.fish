#!/usr/bin/env fish

if not test -f .env
    echo ".env file not found!"
    exit 1
end

for line in (cat .env | grep -v '^#')
    set --local key_value (string split "=" $line)
    set --export $key_value[1] $key_value[2]
end