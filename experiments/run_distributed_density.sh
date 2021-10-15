cd ../edgelists/randomized/
cores="c10_"

for file in n65536_d*_s1?.csv n65536_d*_s2?.csv;
do
   printf 'Processing %s\n' "$file"
   echo "$cores$file " >> ../../experiments/separate_times.txt
   echo "$cores$file " >> ../../experiments/mergesort_times.txt
   echo "$cores$file " >> ../../experiments/vertex_times.txt
   echo "$cores$file " >> ../../experiments/search_times.txt
   [ -f "$file" ] && ts=$(date +%s%N); python3 ../../experiments/separate.py "$file"; echo $((($(date +%s%N) - $ts)/1000)) >> ../../experiments/separate_times.txt
   ts=$(date +%s%N); sort -u ../../ordered.csv > ../../sorted.csv; echo $((($(date +%s%N) - $ts)/1000)) >> ../../experiments/mergesort_times.txt
   ts=$(date +%s%N); cut -d, -f1 ../../sorted.csv | uniq > ../../vertex.csv; echo $((($(date +%s%N) - $ts)/1000)) >> ../../experiments/vertex_times.txt
   ts=$(date +%s%N); python3 ../../experiments/TriFi.py; echo $((($(date +%s%N) - $ts)/1000)) >> ../../experiments/search_times.txt
done
