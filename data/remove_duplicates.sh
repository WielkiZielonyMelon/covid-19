#!/bin/bash
# https://superuser.com/questions/386199/how-to-remove-duplicated-files-in-a-directory/386209#386209
declare -A arr
shopt -s globstar

for file in **; do
    [[ -f "$file" ]] || continue

    read cksm _ < <(md5sum "$file")
    if ((arr[$cksm]++)); then 
        rm $file
    fi
done
