echo запоминаем рабочую директорию
pushd %CD%
echo переходим в директорию виртуального окружения
cd ..
echo активируем вирутальное окружение
call "venv\scripts\activate.bat"
echo возвращаемся обратно
popd
python manage.py runserver
pause