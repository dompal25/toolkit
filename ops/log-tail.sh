#!/usr/bin/env bash
# Pretty-tail ndjson logs: highlights level=error and groups by req_id
jq -Rc 'try fromjson catch {{msg:., level:"raw"}} | [.ts, .level, .req_id, .msg] | @tsv' | awk 'BEGIN{FS="\t"}{lvl=$2; if(lvl=="error"){print "\033[31m" $0 "\033[0m"} else {print}}'
