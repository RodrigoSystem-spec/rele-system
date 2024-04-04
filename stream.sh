#!/bin/bash
dia=$(date +%A)
case $dia in
  Monday)
     diaact=Lunes
  ;;
  Tuesday)
     diaact=Martes
  ;;
  Wednesday)
     diaact=Miercoles
  ;;
  Thursday)
     diaact=Jueves
  ;;
  Friday)
     diaact=Viernes
  ;;
  Saturday)
     diaact=Sabado
  ;;
  Sunday)
    diaact=Domingo
  ;;
esac

ffmpeg -v quiet -rtsp_transport tcp -i "rtsp://user:pass@ip:puerto/cam/realmonitor?channel=1&subtype=0" -c copy -an "/home/pi/R-System/Videos/$diaact/video_$(date +"%Y%m%d%H%M%S").mp4"
