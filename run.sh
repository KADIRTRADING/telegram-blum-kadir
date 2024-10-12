#!/bin/bash

# Проверка на наличие папки venv
if [ ! -d "venv" ]; then
    echo "Virtual muhit yaratilmoqda..."
    python3 -m venv venv
fi

echo "Virtual muhit faollashmoqda..."
source venv/bin/activate

# Проверка на наличие установленного флага в виртуальном окружении
if [ ! -f "venv/installed" ]; then
    if [ -f "requirements.txt" ]; then
        echo "Bogʻlanmalar oʻrnatilmoqda..."
        pip3 install -r requirements.txt
        touch venv/installed
    else
        echo "requirements.txt topilmadi, qaramlikni o'rnatish o'tkazib yuborildi."
    fi
else
    echo "Bogʻlanmalar oʻrnatilgan! Oʻtkazib yuborilmoqda..."
fi

echo "bot ishga tushurilmoqda..."
python3 main.py

echo "Muvaffaqiyatli!"
