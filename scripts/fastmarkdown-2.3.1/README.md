Este lenguaje de programación está diseñado para estandarizar el uso de MarkDown y hacer más fácil la redacción de contenido.

Para instalar la extensión en VSC, abre la paleta de comandos con Ctrl+Shift+P y escribe "Developer: Install Extension from Location", selecciona la carpeta "fastmarkdown-2.3.1" y dale a continuar.

Ya tienes instalada la extensión. Para poder usarla, necesitarás copiar este argumento en tu archivo settings.json:

    "editor.tokenColorCustomizations": {
        "textMateRules": [
            {
                "scope": "fmd.bold.fmd",
                "settings": {
                    "foreground": "#94eb52", // Color para texto en negrita
                    "fontStyle": "bold" // Añadir estilo de negrita
                }
            },
            {
                "scope": "fmd.italic.fmd",
                "settings": {
                    "foreground": "#09acb5", // Color para texto en cursiva
                    "fontStyle": "italic" // Añadir estilo de cursiva
                }
            },
            {
                "scope": "fmd.strikethrough.fmd",
                "settings": {
                    "foreground": "#ff3c00", // Color para texto tachado
                    "fontStyle": "strikethrough" // Añadir estilo de tachado
                }
            },
            {
                "scope": "fmd.subscript.fmd",
                "settings": {
                    "foreground": "#ff0000" // Color para subíndices
                }
            },
            {
                "scope": "fmd.superscript.fmd",
                "settings": {
                    "foreground": "#00ff00" // Color para superíndices
                }
            },
            {
                "scope": "fmd.python.fmd",
                "settings": {
                    "foreground": "#9494ff" // Color para bloques de código
                }
            },
            {
                "scope": "fmd.ipy.fmd",
                "settings": {
                    "foreground": "#9494ff" // Color para bloques de código
                }
            },
            {
                "scope": "fmd.comment.fmd",
                "settings": {
                    "foreground": "#6b6b6b" // Color para comentarios
                }
            },
            {
                "scope": "fmd.h1.fmd",
                "settings": {
                    "foreground": "#00ff00", // Color para encabezados de nivel 1
                    "fontStyle": "bold"
                }
            },
            {
                "scope": "fmd.h2.fmd",
                "settings": {
                    "foreground": "#00ffff", // Color para encabezados de nivel 2
                    "fontStyle": "bold"
                }
            },
                        {
                "scope": "fmd.h3.fmd",
                "settings": {
                    "foreground": "#ffff00", // Color para encabezados de nivel 2
                    "fontStyle": "bold"
                }
            },
            {
                "scope": "fmd.img.fmd",
                "settings": {
                    "foreground": "#ff00ff", // Color para imágenes
                    "fontStyle": "underline"
                }
            },
            {
                "scope": "fmd.def.fmd",
                "settings": {
                    "foreground": "#aaa" // Color para definiciones
                }
            },
            {
                "scope": "fmd.void.fmd",
                "settings": {
                    "foreground": "#05acb5" // Color para void
                }
            },
            {
                "scope": "fmd.done.fmd",
                "settings": {
                    "foreground": "#02e9f5" // Color para done
                }
            },
            {
                "scope": "fmd.numbered.fmd",
                "settings": {
                    "foreground": "#ffff00" // Color para numerados
                }
            },
            {
                "scope": "fmd.pointed.fmd",
                "settings": {
                    "foreground": "#ffff00" // Color para apuntados
                }
            },
            {
                "scope": "fmd.brochet.fmd", // Color para brochet
                "settings": {
                    "foreground": "#ffff00",
                }
            },
            {
                "scope": "fmd.imath.fmd", // Color para matemáticas en linea
                "settings": {
                    "foreground": "#ffffaa",
                }
            },
            {
                "scope": "fmd.math.fmd", // Color para matemáticas
                "settings": {
                    "foreground": "#ffffaa",
                }
            },
            {
                "scope": "fmd.new.fmd", // Color para nuevo párrafo
                "settings": {
                    "foreground": "#6b6b6b" // Color para nuevo párrafo
                }
            }
        ]
    },