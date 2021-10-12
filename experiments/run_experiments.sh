cd ../edgelists/randomized/

for file in *;
do
   printf 'Processing %s\n' "$file"
   echo "$file " >> ../../experiments/separate_times.txt
   echo "$file " >> ../../experiments/mergesort_times.txt
   echo "$file " >> ../../experiments/vertex_times.txt
   echo "$file " >> ../../experiments/search_times.txt
   [ -f "$file" ] && ts=$(date +%s%N); python3 ../../experiments/separate.py "$file"; echo $((($(date +%s%N) - $ts)/1000)) >> ../../experiments/separate_times.txt
   ts=$(date +%s%N); sort -u ../../ordered.csv > ../../sorted.csv; echo $((($(date +%s%N) - $ts)/1000)) >> ../../experiments/mergesort_times.txt
   ts=$(date +%s%N); cut -d, -f1 ../../sorted.csv | uniq > ../../vertex.csv; echo $((($(date +%s%N) - $ts)/1000)) >> ../../experiments/vertex_times.txt
   ts=$(date +%s%N); python3 ../../experiments/TriFi.py; echo $((($(date +%s%N) - $ts)/1000)) >> ../../experiments/search_times.txt
done
