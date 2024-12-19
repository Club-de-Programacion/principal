#!/bin/bash

# Cambiar el directorio actual al del script
cd "$(dirname "$0")" || exit

# Crear un listado de subcarpetas (incluyendo ocultas) y mostrarlas al usuario
count=0
declare -A folders

# Listar tanto carpetas normales como ocultas
for dir in */ .*/; do
    # Ignorar el directorio actual '.' y el directorio padre '..'
    if [[ "$dir" != "./" && "$dir" != "../" ]]; then
        ((count++))
        folders[$count]="$dir"
        echo "$count: $dir"
    fi
done

# Preguntar al usuario por la subcarpeta
echo ""
read -p "Seleccione la subcarpeta deseada: " choice

# Validar la elección y ejecutar el script start.py en la subcarpeta
if [[ -n "${folders[$choice]}" ]]; then
    selected_folder="${folders[$choice]}"
    script_path="$selected_folder/start.py"
    
    if [[ -f "$script_path" ]]; then
        echo "Ejecutando $script_path..."
        cd "$selected_folder" || exit
        python3 "$script_path" && exit
    else
        echo "No existe 'start.py' en $selected_folder."
        echo "Abriendo $selected_folder en Visual Studio Code..."
        code "$selected_folder" && exit
    fi
else
    echo "Opción no válida."
fi
