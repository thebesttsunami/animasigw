#!/bin/bash

clear

for ((i=0; i<10; i++)); do
    echo -e "\033[2J\033[;H"  # Membersihkan layar
    echo "Frame $i"
    sleep 0.5  # Menunda selama 0.5 detik
done
