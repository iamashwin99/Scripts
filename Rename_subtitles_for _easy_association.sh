for file in *.vtt
do
  
  v=${file::-10}
  b=$(ls .. | grep "$v" |grep mp4)
  c=${b::-2}
  echo $b
  echo $c
  mv "$file" "$c"
  mv "$c" "$(basename "$c" .m).vtt"
done
