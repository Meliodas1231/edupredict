# edupredict

Sistema de gestión para el proyecto edupredict.

## Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/Meliodas1231/edupredict.git
   cd edupredict
   ```

2. **Crear el entorno virtual**:
   ```bash
   python -m venv .venv
   ```

3. **Activar el entorno virtual**:
   - **Windows (PowerShell)**:
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
     Si aparece error de permisos, ejecuta una vez: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`
   - **Windows (CMD)**:
     ```cmd
     .venv\Scripts\activate.bat
     ```
   - **Linux/macOS**:
     ```bash
     source .venv/bin/activate
     ```

   > La carpeta se llama **`.venv`** (con punto al inicio), no `venv`. Si el comando falla, verifica que exista: debe haberse creado en el paso 2.

4. **Instalar dependencias** (desde `requirements.txt`):
   ```bash
   pip install -r requirements.txt
   ```

   Esto instala Django y el resto de paquetes del proyecto con las versiones indicadas en el archivo.

## Cómo ejecutar el proyecto

1. Asegúrate de tener el entorno virtual activo.
2. Ejecuta las migraciones (si es la primera vez):
   ```bash
   python manage.py migrate
   ```
3. Inicia el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```
4. Accede a `http://127.0.0.1:8000` en tu navegador.
