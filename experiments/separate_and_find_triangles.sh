cd ../edgelists/resorted

for file in *;
do
   printf 'Processing %s\n' "$file"
   echo "$file " >> ../../experiments/separate_times.txt
   echo "$file " >> ../../experiments/search_times.txt
   [ -f "$file" ] && ts=$(date +%s%N); python3 ../../experiments/separate.py "$file"; echo $((($(date +%s%N) - $ts)/1000)) >> ../../experiments/separate_times.txt
   [ -f "$file" ] && ts=$(date +%s%N); python3 ../../experiments/TriFiParsed.py "$file"; echo $((($(date +%s%N) - $ts)/1000)) >> ../../experiments/search_times.txt
done
