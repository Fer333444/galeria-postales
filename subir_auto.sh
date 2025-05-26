#!/bin/bash
cd /ruta/a/FOTOS_QR_CLEAN_2
git add .
git commit -m "Postal automática $(date)"
git push origin main
