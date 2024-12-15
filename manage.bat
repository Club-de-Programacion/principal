@echo off
setlocal enabledelayedexpansion

REM Crear un listado de subcarpetas y mostrarlas al usuario
set "count=0"
for /D %%d in (*) do (
    set /a count+=1
    set "folder[!count!]=%%d"
    echo !count!: %%d
)

REM Preguntar al usuario por la subcarpeta
set /p "choice=Seleccione la subcarpeta deseada: "

REM Validar la elección y ejecutar el script start.py en la subcarpeta
if defined folder[%choice%] (
    set "selected_folder=!folder[%choice%]!"
    set "script_path=%cd%\!selected_folder!\start.py"
    if exist "!script_path!" (
        echo Ejecutando !script_path! en una nueva terminal...
	cd !selected_folder!
        start cmd /c python "!script_path!" && exit
    ) else (
        echo No existe "start.py" en !selected_folder!.
        echo Abriendo !selected_folder! en Visual Studio Code...
        code "!cd!\!selected_folder!" && exit
    )
) else (
    echo Opción no válida.
)

pause