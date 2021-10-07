mkdir ../edgelists/randomized
cd ../edgelists

for file in *; 
do
   printf 'Processing %s\n' "$file"
   [ -f "$file" ] && shuf "$file" > "./randomized/$file"
done
