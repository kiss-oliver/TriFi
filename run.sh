file = $1

printf 'Processing %s\n' "$file"
python3 separate.py "$file"
sort -u ordered.csv > sorted.csv
cut -d, -f1 sorted.csv | uniq > vertex.csv
python3 TriFi.py
rm sorted.csv
rm ordered.csv
