# 🛠️ Guía de Desarrollo – Grupo 10

Para que el proyecto avance sin errores, sin conflictos y sin que nadie **"se pise la manguera"**, seguiremos estas **reglas de oro**. Léelas con atención antes de escribir una sola línea de código.

---

## 1. 🔀 Flujo de Trabajo (Git)

### 🌳 Estructura de Ramas

* **`main` es sagrado 🛐**

  * Nunca se sube nada directamente a `main`.
  * Es la rama de **entrega final** y está protegida.

* **`test` es el laboratorio 🧪**

  * Todos los cambios se integran **primero** en `test`.
  * Aquí se prueban y validan las funcionalidades antes de pasar a `main`.

* **Subramas por tarea 🧩**

  * ❌ No trabajes directamente en `test`.
  * Cada tarea debe tener su propia rama.

### 🧭 Flujo correcto paso a paso

```bash
git checkout test
git pull origin test
git checkout -b feat-nombre-de-tu-tarea
```

1. Desarrolla tu funcionalidad en tu rama.
2. Al terminar:

```bash
git push origin feat-nombre-de-tu-tarea
```

3. Avisa al líder del equipo para revisar el **Pull Request hacia `test`**.

---

## 2. 🏗️ Arquitectura del Código

### 🚫 Prohibido Hardcodear

* No se permite escribir valores fijos directamente en la lógica:

  * ❌ Velocidades
  * ❌ Tiempos
  * ❌ Radios
  * ❌ Multiplicadores

👉 **Todo valor configurable debe venir de `config`.**

---

### ⚙️ Uso Obligatorio de Config

* **Todo valor de dificultad** debe leerse desde:

```text
src/config/game_modes.py
```

* Los valores base del juego viven en:

```text
src/config/settings.py
```

---

### 🎨 Componentes de UI

* Cualquier botón o elemento visual debe ir en:

```text
src/ui/components/
```

* **Todos los componentes deben implementar obligatoriamente:**

  * `update(dt)`
  * `draw(screen)`

---

## 3. 🤝 Reglas de Convivencia Técnica

### ⏱️ Delta Time (`dt`)

* **Todo movimiento o temporizador debe multiplicarse por `dt`.**
* Esto garantiza que el juego corra igual en cualquier PC.

Ejemplo conceptual:

```python
posicion += velocidad * dt
```

---

### 📝 Comentarios y Trabajo Incompleto

* Si dejas algo a medias, usa siempre:

```python
# TODO: descripción clara de lo que falta
```

---

### 🔄 Sincronización del Equipo

* **Antes de empezar a programar**, siempre ejecuta:

```bash
git pull origin test
```

* Esto evita conflictos y trabajo duplicado.

---

## 4. ⚙️ Funcionamiento Profundo de Configuraciones

### 🧠 A. `src/config/settings.py` — *La Clase `Settings`*

Este archivo **centraliza todos los parámetros técnicos** del juego.

#### 📌 Contiene:

* **Metadata del proyecto**

  * Título del juego
  * Autores
  * Versión

* **Parámetros base del juego**

  * Ejemplos:

    * `FLASHLIGHT_RADIUS_BASE`
    * `FISH_SIZE`
    * Velocidades base
    * Tiempos base

* **Gestión de Assets**

  * Mapas como:

    * `IMAGES_MAP`
    * `SOUNDS_MAP`
    * `FONTS_MAP`
  * Para añadir un recurso, solo se agrega el nombre del archivo en el mapa correspondiente.

#### 🧪 Uso

```python
from src.config.settings import Settings

radius = Settings.FLASHLIGHT_RADIUS_BASE
```

---

### 🎮 B. `src/config/game_modes.py` — *Dificultad Dinámica*

Este archivo es el **"cerebro"** que escala la dificultad del juego.

#### 📌 Incluye variables como:

* `time`
* `spawn_rate`
* `fish_speed`
* Multiplicadores de dificultad

#### ⚙️ Implementación

* El código **debe consultar el modo activo**.
* Los valores se aplican como **multiplicadores** sobre los valores base definidos en `Settings`.

---

### 🔊 C. `src/managers/sound_player.py` — *Gestor de Audio*

Centraliza **todo el manejo de audio** del juego.

🚫 **Prohibido crear objetos de sonido de Pygame fuera de este manager.**

#### 🎧 Métodos disponibles

* **Efectos de sonido (SFX):**

```python
sound_player.play_sfx("clave")
```

* **Música de fondo:**

```python
sound_player.play_music("clave")
```

---

## 5. 🚀 Pasos para Implementar una Nueva Funcionalidad

1. **⚙️ Configurar**

   * Si tu tarea usa un asset, añade su nombre al mapa correspondiente en `Settings`.

2. **🎮 Definir Dificultad**

   * Si afecta el balance del juego, añade la variable en `game_modes.py`.

3. **🧠 Desarrollar**

   * Escribe la lógica en la carpeta correspondiente.
   * Consume siempre los valores desde `config`, nunca desde números hardcodeados.

---

✅ **Siguiendo estas reglas, el proyecto será mantenible, escalable y libre de caos.**