LOL Statium
===
Tu fuente de estadísticas de League Of Legends
## Información
- Titulo:  `LOL STATIUM`
- Autor:  `Jaime de la Fuente`

## Dependencias
- python
- pandas
- panel
- tqdm
- matplotlib
- numpy

## Uso
- Para obtener datos y guardarlos en la base de datos
  ```
  python .\Model\main.py
  ```
- Para iniciar la página
  ```
  .\View\index.html
  ```

## Directory Hierarchy
```
|—— Controller
|    |—— Index.js
|—— Docs
|    |—— conf.py
|    |—— db.rst
|    |—— db.sqlite
|    |—— index.rst
|    |—— make.bat
|    |—— Makefile
|    |—— MatchHistory.rst
|    |—— Metadata.rst
|    |—— modules.rst
|    |—— PicksBans.rst
|    |—— Positions.rst
|    |—— Web_scrap.rst
|    |—— _build
|    |—— _static
|    |—— _templates
|—— Model
|    |—— DataBase
|        |—— db.sqlite
|    |—— db.py
|    |—— Download
|    |—— main.py
|    |—— MatchHistory.py
|    |—— Metadata.py
|    |—— PicksBans.py
|    |—— Positions.py
|    |—— Web_scrap.py
|—— Tests
|    |—— Tests.py
|—— venv
|    |—— etc
|    |—— Include
|    |—— Lib
|—— View
|    |—— 404.html
|    |—— heatmap.html
|    |—— Img
|        |—— comp.gif
|        |—— heatmap.png
|        |—— index_image.png
|        |—— metrics.png
|        |—— picksBans.png
|        |—— summoners-rift.jpg
|    |—— index.html
|    |—— login.html
|    |—— matchHistory.html
|    |—— metrics.html
|    |—— Picksbans.html
|    |—— Styles
|        |—— login.css
|        |—— style.css
|        |—— style_index.css
```