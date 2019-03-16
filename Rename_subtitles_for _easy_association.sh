for file in *.vtt
do
  
  v=${file::-10}
  b=$(ls| grep "$v" |grep mp4)
#  echo $b
  mv "$b" "$(basename "$b" .mp4).vtt"
done
