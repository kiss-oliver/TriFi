mkdir ../edgelists/resorted
cd ../edgelists/randomized

for file in *;
do
   printf 'Processing %s\n' "$file"
   echo "$file " >> ../../experiments/sort_times.txt
   [ -f "$file" ] && ts=$(date +%s%N); sort "$file" > "../resorted/$file"; echo $((($(date +%s%N) - $ts)/1000)) >> ../../experiments/sort_times.txt
done
