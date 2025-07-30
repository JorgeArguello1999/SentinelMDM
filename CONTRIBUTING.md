# 👷‍♀️ CONTRIBUTING

# Directrices para la Contribución a Educhain

¡Gracias por tu interés en contribuir a Educhain! Valoramos enormemente tu apoyo para mejorar la plataforma de certificación y verificación de la PUCE-Ambato. Este documento establece las directrices para el proceso de contribución, asegurando que todas las aportaciones se integren de manera eficiente y mantengan la calidad y consistencia del proyecto.

Al contribuir a Educhain, aceptas regirte por el código de conducta y las licencias de este proyecto.

## 1\. Código de Conducta

Nos comprometemos a hacer de la participación en este proyecto una experiencia libre de acoso para todos. Al contribuir a Educhain, se espera que sigas nuestro Código de Conducta. Esto incluye ser respetuoso, abierto y amable con todos los miembros de la comunidad.

## 2\. Cómo Reportar un Bug

Si encuentras un error o un comportamiento inesperado en Educhain, por favor, ayúdanos reportándolo. Sigue estos pasos para crear un reporte de bug efectivo:

1.  **Verifica los Issues Existentes:** Antes de crear un nuevo issue, busca en los issues existentes en GitHub para asegurarte de que el bug no haya sido ya reportado.
2.  **Abre un Nuevo Issue:** Si no encuentras un reporte existente, abre un nuevo issue en el repositorio de GitHub.
3.  **Usa la Plantilla de Bug:** Proporciona la información solicitada en la siguiente plantilla para tu reporte de bug:Markdown
    
    ````
    ### 🐞 Reporte de Bug: [Título conciso del bug]
    
    **ID del Issue:** #[Número de Issue Asignado por GitHub]
    
    **Descripción del Bug:**
    Una descripción clara y concisa de lo que es el bug y cómo te afecta.
    
    **Pasos para Reproducir:**
    Pasos claros y numerados para reproducir el comportamiento inesperado.
    Ej:
    1. Ir a '...'
    2. Click en '....'
    3. Ver '....'
    
    **Comportamiento Esperado:**
    Describe lo que esperabas que sucediera.
    
    **Comportamiento Actual:**
    Describe lo que realmente sucedió, incluyendo cualquier mensaje de error.
    
    **Capturas de Pantalla / Logs:**
    Si es posible, adjunta capturas de pantalla, grabaciones de pantalla o fragmentos de logs del servidor/navegador que ilustren el problema.
    
    ```bash
    # Pegar aquí los logs de error relevantes
    ````
    
    **Entorno:**
    
    - **Versión de Educhain:** (Ej. `main` branch, v1.0.0-beta)
    - **Sistema Operativo:** (Ej. Windows 10, macOS Ventura, Ubuntu 22.04)
    - **Navegador:** (Ej. Chrome 120, Firefox 120, Edge 120)
    - **Versión de .NET:** (Ej. .NET SDK 8.0.100)
    - **Configuración de la Blockchain:** (Ej. Ganache, Sepolia Testnet)
    
    **Prioridad Sugerida:** (Ej. Crítico, Mayor, Menor)
    
    ```
    
    ```
    

## 3\. Cómo Sugerir una Característica

Si tienes una idea para una nueva característica o una mejora en Educhain, te animamos a proponerla. Sigue estos pasos:

1.  **Verifica los Issues Existentes:** Busca en los issues existentes para ver si la característica ya ha sido sugerida.
2.  **Abre un Nuevo Issue:** Si no, abre un nuevo issue en GitHub.
3.  **Usa la Plantilla de Característica:** Proporciona la información solicitada en la siguiente plantilla:Markdown
    
    ```
    ### ✨ Sugerencia de Característica: [Título conciso de la característica]
    
    **ID del Issue:** #[Número de Issue Asignado por GitHub]
    
    **Problema a Resolver:**
    Describe el problema actual o la necesidad que esta nueva característica resolvería.
    
    **Solución Propuesta:**
    Describe detalladamente la característica que te gustaría ver implementada. Incluye cómo crees que debería funcionar y cualquier interacción de usuario relevante.
    
    **Casos de Uso / Escenarios:**
    Describe cómo los usuarios (ej. secretaría, empleadores, verificadores) interactuarían con esta característica.
    
    **Beneficio para Educhain:**
    Explica cómo esta característica beneficiaría a Educhain, a la PUCE-Ambato o a sus usuarios.
    (Ej. "Mejoraría la eficiencia del proceso de X", "Añadiría una capa de seguridad para Y", "Facilitaría la verificación para Z").
    
    **Referencias / Ejemplos (Opcional):**
    Si hay sistemas o ejemplos similares que ilustren tu idea, inclúyelos aquí.
    
    **Impacto Potencial (Opcional):**
    ¿Consideras que esta característica podría afectar a otros componentes del sistema?
    ```
    

El equipo de desarrollo de Educhain revisará las sugerencias de características periódicamente para discutir su viabilidad y priorizarlas.

## 4\. Proceso de Desarrollo y Pull Requests

Seguimos un flujo de trabajo basado en **GitHub Flow** para todas las contribuciones de código.

### 4.1. Flujo de Trabajo

1.  **Bifurca (Fork) el Repositorio:** Crea tu propia copia del repositorio de Educhain en tu cuenta de GitHub.
2.  **Clona tu Bifurcación:** Clona tu bifurcación localmente.
3.  **Crea una Rama:** Crea una nueva rama para tu característica o corrección de bug.
4.  **Desarrolla:** Realiza tus cambios.
5.  **Prueba:** Asegúrate de que tus cambios pasen todas las pruebas existentes y escribe nuevas pruebas si es necesario.
6.  **Commit:** Realiza tus commits siguiendo las directrices de mensajes de commit.
7.  **Push:** Sube tus cambios a tu bifurcación en GitHub.
8.  **Crea un Pull Request (PR):** Abre un Pull Request desde tu rama hacia la rama `main` del repositorio original de Educhain.

### 4.2. Nomenclatura de Ramas

Mantén las ramas limpias y con nombres descriptivos. Se recomienda la siguiente convención:

- **Para características:** `feature/<issue-id>-descripcion-corta` (ej. `feature/#123-implementar-verificacion-api`)
- **Para correcciones de bugs:** `bugfix/<issue-id>-descripcion-corta` (ej. `bugfix/#456-error-al-emitir-certificado`)
- **Para hotfixes (correcciones urgentes en producción):** `hotfix/<issue-id>-descripcion-corta`

Asegúrate de reemplazar `<issue-id>` con el número real del issue en GitHub al que te refieres.

### 4.3. Mensajes de Commits

Utilizamos el estándar [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) para nuestros mensajes de commit, lo que facilita la comprensión del historial del proyecto y la generación automatizada del `CHANGELOG.md`.

El formato general es: `<tipo>(<ámbito>): <descripción>`

- **Tipos comunes:**
    - `feat`: Nueva característica.
    - `fix`: Corrección de un bug.
    - `docs`: Cambios en la documentación.
    - `style`: Cambios que no afectan el significado del código (espacios en blanco, formato, puntos y comas).
    - `refactor`: Cambio de código que no añade características ni corrige bugs.
    - `test`: Añadiendo pruebas faltantes o corrigiendo pruebas existentes.
    - `chore`: Cambios en el proceso de construcción, herramientas auxiliares, bibliotecas externas, etc.
    - `perf`: Cambio de código que mejora el rendimiento.
    - `build`: Cambios que afectan el sistema de construcción o dependencias externas.
    - `ci`: Cambios en nuestros archivos y scripts de configuración de CI.
- **Ámbito (opcional):** El área del código que se ve afectada por el cambio (ej. `api`, `web`, `blockchain`, `secretaria`).
- **Descripción:** Una descripción concisa del cambio en tiempo presente imperativo (ej. "añadir", "corregir", "actualizar").

**Ejemplos:**

```
feat(web): implementar formulario de emision de certificados
fix(api): corregir error de autenticacion en endpoint de secretaria
docs(readme): actualizar seccion de instalacion
refactor(blockchain): simplificar logica de interaccion con contrato
```

Si el commit es más complejo, puedes añadir un cuerpo y pie de página al mensaje para explicar el "por qué" de la solución, los problemas que resuelve y cualquier referencia a issues de GitHub.

### 4.4. Guía para Pull Requests (PRs)

Antes de enviar tu Pull Request, asegúrate de:

1.  **Resolver el Issue:** Si tu PR cierra un issue, asegúrate de referenciarlo en la descripción del PR (ej. `Closes #123`).
2.  **Código Limpio:** Asegúrate de que tu código esté formateado y libre de warnings no intencionales.
3.  **Pruebas Pasadas:** Todas las pruebas existentes deben pasar y debes haber añadido pruebas para tu nuevo código/cambio.
4.  **Documentación Interna:** Actualiza los comentarios en el código si has modificado funciones, parámetros o la lógica central.
5.  **Revisión del Código:** Los PRs serán revisados por los autores del proyecto (Jorge Arguello y Víctor Toasa). Se requiere al menos **una aprobación** para fusionar el PR.
6.  **Conflictos de Fusión:** En caso de conflictos de fusión, el **responsable de la fusión** (generalmente uno de los autores del proyecto) se encargará de resolverlos.

### 4.5. Plantilla de Pull Request

Por favor, utiliza la siguiente plantilla al crear un nuevo Pull Request en GitHub:

Markdown

```
### Pull Request: [Tipo]: [Título conciso del PR]

**Tipo de Cambio:**
- [ ] `feat` (Nueva característica)
- [ ] `fix` (Corrección de bug)
- [ ] `docs` (Cambio en la documentación)
- [ ] `style` (Cambios de estilo de código)
- [ ] `refactor` (Refactorización de código)
- [ ] `test` (Añadir/corregir pruebas)
- [ ] `chore` (Tareas de mantenimiento, configuración)
- [ ] `perf` (Mejora de rendimiento)
- [ ] `build` (Cambios en el sistema de construcción)
- [ ] `ci` (Cambios en CI/CD)

**Descripción del Cambio:**
[Describe aquí los cambios realizados de manera detallada. Sé lo más explícito posible.]

**Relacionado con Issue(s):**
[Escribe aquí los números de los issues de GitHub que este PR resuelve. Ej: Closes #123, Fixes #456]

**¿Qué problema resuelve este PR?**
[Explica el problema que este Pull Request soluciona.]

**¿Cómo fue resuelto?**
[Describe la solución implementada. Si es relevante, menciona las clases/archivos clave modificados.]

**Pruebas:**
[Describe cómo se probó el cambio (ej. pruebas unitarias añadidas, pruebas de integración ejecutadas, pruebas manuales en el entorno de desarrollo).]
- [ ] Todas las pruebas unitarias pasan.
- [ ] Todas las pruebas de integración pasan.
- [ ] Las pruebas E2E (si aplica) han sido ejecutadas y pasan.

**Checklist:**
- [ ] Mi código sigue las directrices de estilo de este proyecto.
- [ ] Mis cambios no introducen nuevas advertencias de compilación.
- [ ] He añadido comentarios adecuados en el código donde sea necesario.
- [ ] He actualizado la documentación relevante (interna, README, etc.).
- [ ] Mis cambios no rompen ninguna funcionalidad existente.
- [ ] He probado mis cambios a fondo.
- [ ] He añadido pruebas para cubrir mis cambios (si aplica).
```

## 5\. Estilo de Código y Directrices de Documentación Interna

La consistencia es clave en Educhain. Aunque no se imponen herramientas automáticas específicas de formateo, se espera que el código sea legible y siga las convenciones generales de C# y .NET.

- **Comentarios en Código (C# XML Documentation Comments):**
    - Utiliza los comentarios de documentación XML (`<summary>`, `<param>`, `<returns>`, `<exception>`, `<remarks>`) para todas las clases, interfaces, métodos y propiedades públicas. Esto es crucial para generar documentación de la API y para la comprensión del código.
    - **Explicar Algoritmos Núcleo:** Es obligatorio añadir comentarios detallados para explicar la lógica de algoritmos complejos o decisiones de diseño críticas, especialmente aquellas que interactúan con la blockchain o manejan operaciones fundamentales del sistema (ej. hashing de certificados, interacción con contratos inteligentes, lógica de verificación). Explica el "por qué" y el "cómo" de estas secciones.
- **Nomenclatura:** Sigue las convenciones de nomenclatura estándar de C#:
    - **PascalCase** para clases, interfaces, métodos públicos, propiedades públicas y enumeraciones.
    - **camelCase** para variables locales y parámetros de métodos.
    - Utiliza nombres descriptivos que reflejen claramente el propósito del código, evitando abreviaciones ambiguas.
- **Organización del Código:** Mantén una estructura de carpetas y proyectos consistente dentro de cada microservicio, siguiendo un patrón lógico (ej. por capas, por características).

## 6\. Directrices de Pruebas

Para mantener la calidad y fiabilidad de Educhain, se espera que todas las contribuciones incluyan pruebas adecuadas.

- **Pruebas Unitarias:** Son las más importantes. Asegúrate de que cualquier nueva funcionalidad o corrección de bug esté acompañada de pruebas unitarias que cubran la lógica de negocio y los componentes individuales.
- **Pruebas de Integración:** También son cruciales. Se espera que las pruebas de integración validen la interacción entre los componentes de los microservicios, y especialmente la comunicación con la blockchain (utilizando entornos de desarrollo como Ganache o testnets). Se recomienda el uso de mocks cuando sea apropiado para simular dependencias externas complejas.
- **Cobertura:** Si bien no se exige un umbral de cobertura estricto, se anima a los desarrolladores a buscar una alta cobertura de sus cambios.

## 7\. Flujo de Trabajo para el Grupo de Testers

Nuestro pequeño grupo de testers, que también son desarrolladores, sigue un flujo de trabajo específico:

1.  **Detección y Reporte:** Cuando un tester encuentra un problema, abre un `Issue` en GitHub utilizando la plantilla de `Reporte de Bug` descrita en la sección 2.
2.  **Resolución en Rama:** Un desarrollador (o el mismo tester si asume el rol de desarrollador para la corrección) toma el issue y crea una nueva rama siguiendo las convenciones de nomenclatura de ramas (ej. `bugfix/#<issue-id>-descripcion`).
3.  **Implementación y Pruebas:** Se implementa la solución y se aseguran de que las pruebas unitarias y de integración pasen.
4.  **Pull Request:** Una vez resuelto y probado, se abre un `Pull Request` a la rama `main` del repositorio, refirienciando el issue que cierra (ej. `Closes #<issue-id>`). El PR sigue la plantilla de Pull Request descrita en la sección 4.5.
5.  **Revisión y Fusión:** Los autores del proyecto revisan el PR y, una vez aprobado, se fusiona.