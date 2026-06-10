#!/bin/bash
# Script de construccion que Vercel ejecuta para preparar los archivos estaticos.
pip install -r requirements.txt
python3 manage.py collectstatic --noinput
