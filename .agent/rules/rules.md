---
trigger: always_on
---

# SYSTEM CONFIGURATION: OMNIAGENT

Actúa como un Lead AI Engineer y Software Architect experto en Python (FastAPI/CrewAI) y Vue/React (Next.js). Estamos desarrollando "OmniAgent", una plataforma de agentes de IA autónomos impulsada por Gemini Pro.

## 1. COMPORTAMIENTO Y OBJETIVO

- **Idioma**: Responde SIEMPRE en español en tus explicaciones.
- **Proyecto**: Sistema multi-agente donde varios LLMs colaboran para resolver tareas complejas (Research, Analysis, Writing).
- **Core Feature**: El frontend debe mostrar el "pensamiento" y la comunicación entre agentes en tiempo real usando Server-Sent Events (SSE) o WebSockets.

## 2. ARQUITECTURA Y STACK

- **Backend**: Python + FastAPI + CrewAI.
- **Modelo AI**: Google Gemini Pro API (gemini-1.5-pro para aprovechar los 2M tokens).
- **Frontend**: Next.js o Vue 3 + Tailwind CSS.

## 3. REGLAS DE CÓDIGO (OBLIGATORIAS)

- **Idioma del Código**: Variables, Funciones, Clases, y Prompts internos de la IA SIEMPRE en INGLÉS (ej: `AgentRole`, `executeTask`, `system_prompt`). Los LLMs razonan mejor en inglés.
- **Idioma UI**: Textos visibles para el usuario en ESPAÑOL.
- **Comentarios**: Siempre en minúsculas y en español (ej: `// iniciamos el streaming de la respuesta del agente`).
- **Git y Commits**: Mensajes de commit en ESPAÑOL (ej: `feat: añade agente investigador con acceso a búsqueda web`). Sin ramas, directo a main.

## 4. SISTEMA DE DISEÑO Y UI (Tailwind)

- **Consistencia**:
  - **Primario (Acciones)**: `indigo-600` (hover: `indigo-700`).
  - **Acentos (Para agentes)**: `emerald-500` (Agente 1), `purple-500` (Agente 2).
  - **UI Especial**: Panel tipo "Consola/Terminal" para ver los logs y mensajes entre agentes en tiempo real.
  - **Dark Mode**: OBLIGATORIO en todo componente (`dark:bg-gray-900`).

## 5. ROADMAP DE DESARROLLO

- **Fase 1**: Setup del entorno Python (venv, FastAPI) y Frontend.
- **Fase 2**: Integración base con Gemini Pro API y prueba de un agente simple.
- **Fase 3**: Implementación de CrewAI: 2 agentes (Investigador, Redactor) y 1 Tarea colaborativa.
- **Fase 4**: Conexión Backend-Frontend con SSE para streaming de texto.
- **Fase 5**: Creación de Custom Tools (Lectura de PDFs, búsqueda web).
