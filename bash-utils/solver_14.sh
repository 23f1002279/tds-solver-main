#! /bin/sh

old="$1"
new="$2"
dir_path="$3"

echo old: "$old" new: "$new" dir_path: "$dir_path"

for file in "$dir_path/*"
do
    if [ -f "$file" ]; then
    sed -i "" "s/$old/$new/Ig" $file;
    fi
done