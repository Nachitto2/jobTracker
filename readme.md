# jobtracker

La idea de este proyecto es demostrar, aprender y solidificar mis conocimientos, sobre automatización de tareas, webscraping, herramientas como playwright y mas.

El proyecto va a estar separado en distintas fases o versiones. 

## primera version

El programa abre firefox, busca QA tester y trae los titulos de las primeras ofertas que aparecen en la web.

## segunda version

Ahora no solo trae los titulos, tambien trae la empresa y el sueldo que ofrece. Tambien hay manejo de errores y se corrigió un problema de tiempos relacionado a playwright.

## Idea (dada por chat gpt para practicar)

- [x] **Fase 1: MVP (Navegación y Extracción Básica)**
  - Apertura automática del navegador (Firefox).
  - Interacción con la barra de búsqueda (Input & Clic).
  - Extracción de títulos de las primeras ofertas.
- [x] **Fase 2: Persistencia y Limpieza de Datos**
  - Exportación de resultados a formato CSV/Excel.
  - Uso de **Regex** para limpiar salarios y fechas de publicación.
- [ ] **Fase 3: Filtrado Inteligente**
  - Lógica para descartar puestos "Senior" o "Lead" (si se busca Junior).
  - Detección de palabras clave (Python, Selenium, Remoto).
- [ ] **Fase 4: Robustez**
  - Manejo de paginación (Scrapear múltiples páginas).
  - Manejo de errores y Pop-ups de publicidad.
