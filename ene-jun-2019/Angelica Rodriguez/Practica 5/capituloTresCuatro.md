# Capítulo 3: Proceso de ejcución de prueba

### Modelo ERA/SRA
*Estabilización, Regresión y Aceptación*
Ciclo de estabilización donde ejecutamos el 100% de casos de prueba, si alcanzamos más del 80% de
efectividad, empezamos el ciclo de regresión donde probamos ese 20% de casos de prueba que tienen algún
defecto y que debemos generar el 100% de casos de prueba, si no lo logramos, regresamos al ciclo de
estabilización. Si alcanzamos el 100% pasamos a la etapa de aceptación, si hay algún defecto, regresamos
a la etapa de regresión. UAT es la última etapa. User Acceptance Test.

## PREREQUISITOS PARA LA EJECUCIÓN DE CASOS DE PRUEBA
### Casos de prueba
  - Deben estar creados en una matriz de prueba o en una herramienta de gestión de prueba.
  - Deben tener al menos la trazabilidad del escenario. Asociados a un script o procedimiento de prueba.
  - Deben indicarte en dónde están almacenados, ruta oficial del proyecto de prueba o ruta en la herramienta
  de gestión de prueba.
  - Los casos de prueba deben tener un VoBo de un experto en el negocio y con el script a detalle suficiente
  para la reusabilidad.

### Datos de prueba
  - Para ejecutar los casos de prueba se requieren datos estáticos y dinámicos.
  - Hay que generarlos. Cada CP requiere entradas.
  - Los datos estáticos los crea el diseñador de la prueba y los dinámicos el área de ambientes. Depende de
  tu organización.
  - Los datos tienen que estar visibles en tu AUT (Application Under Test) o en las bases de datos.
  - Los datos no pueden ser copias productivas, ejecuta Scrambling para protegerlos.

### Ventana funcional
El área de ambientes, es responsable de cuidad el choque o correlación de pruebas, es decir, que una
prueba no tome los datos de otra prueba o altere los resultados de esta.
Para esto, se implementa la administración de ventanas de prueba funcional, para evitar el choque.
Para una ventana funcional debes tener un checklist cumplido con lo siguiente
  - Casos de prueba listos
  - Datos generados
  - Plan de ejecución
  - Aplicativo AUT instalado

### Plan de ejecución.
*Es el plan a seguir por los ejecutores de prueba para determinar quién y cuándo inician y terminan su
prueba, revisar dependencias con otras pruebas, fechas y datos.*
  - Es común en equipos de 3 o más ejecutores de prueba.
  - Lo debe generar el líder de prueba.
  - Generalmente el plan de ejecución cambia cada ciclo de prueba.
  - Se puede elaorar en un documento de excel o en una herramienta de gestión de pruebas.
  - Es una secuencia de casos de prueba.
  - Responsables de ejecutar casos de prueba.
  - Repositorios de casos de prueba (TestWare)
  - Repositorios de evidencia.

### AUT (Aplicativo Bajo Prueba)
*Es el aplicativo o producto de software que vas a validar con los casos de pureba previamente diseñados
y asignados a ti como ejecutor de prueba.*
  - Tiene que estar instalado en tu ambiente de pruebas o QA.
  - Debe instalarlo el responsable de ambiente de pruebas.
  - Debes recibir la ruta para acceder a este aplicativo así como los usuarios y passwords respectivos.

## ROLES Y RESPONSABILIDADES
### Ejecutor de pruebas.
Ejecuta la prueba siguiendo el script de prueba, puede utilizar herramientas donde estén documentados los
casos de prueba y debe conocer del negocio de lo que va a probar.

### Ingeniero de pruebas.
Conoce el negocio, debe entender los flujos, escenarios y procesos de negocio para poder diseñar las
especificaciones y casos de prueba. Diseña procedimientos para la prueba manual.

### Líder de pruebas.
Conoce el negocio. Entiende el contexto general del proceso. Define el esfuerzo de horas y determina el
equipo de trabajo. Diseña estrategias y plan de pruebas. Monitorea el desempeño e indicadores de la
prueba. Puede suspender y reanudar la prueba en cualquier momento. Cierra la prueba y genera el
certificado de liberación a producción.

### Líder no funcional.
Conoce el negocio, a un nivel de abstracción muy alto. Tiene que entender sobre qué transacciones va a
ejecutar una prueba de desempeño, sobre qué pantallas o aplicativos. Define el esfuerzo de las horas, el
equipo de trabajo, las estrategias y plan de pruebas no funcionales. Monitorea el desempeño e indicadores
de la prueba no funcional. Puede suspender y reanudar la prueba no funcional. Consigue la aprobación de
PRE-PRODUCCIÓN. Cierra la prueba no funcional y genera su parte del certificado de liberación a producción.

### Ingeniero de desempeño.
  - Interpreta las necesidades cuantitativas de calidad del proyecto y plan de prueba no funcional.
  - Diseña los escenarios no funcionales.
  - Diseña y construye los scripts de prueba no funcional.
  - Ejecuta los escenarios diseñados.
  - Obtiene e interpreta las métricas.

### Líder de automatización.
Conoce el negocio. Conoce arquitecturas de automatización. Implementa frameworks. Define el esfuerzo de
horas. Define el equipo de trabajo. Diseña estrategias y plan de pruebas automatizadas. Monitorea el
desempeño e indicadores de la prueba automatizada. Puede suspender y reanudar la prueba automatizada.
Ofrece métricas y resultados de la prueba automatizada cuando el robot termina de hacer su trabajo.

### Ingeniero de automatización.
Conoce el negocio. Automatiza los procedimientos para a paso para ejecutar los casos de prueba. Diseña
y ejecuta scripts de automatización. Conoce de frameworks para entender cómo diseñar eficientemenre los
casos de prueba.

### Líder de ambiente.
  - Define la arquitectura de prueba.
  - Da seguimiento a las necesidades del área.
  - Monitorea el desempeño del área y ambiente de prueba.
  - Define la periodicidad de actualización de datos y scrambling.
  - Define el equipo, roles y responsabilidades.

### Dispatcher.
  - Recibe solicitudes de ambiente de prueba.
  - Las canaliza a los resolutores específicos.
  - Monitorea el desempeño de la solicitud y la atención a ésta.

### Ingeniero de datos o resolutor.
Recibe las solicitudes de ambiente de prueba asignadas por el dispatcher.
Las atiende, dando respuesta y atención. Sea de datos, usuarios, soporte, accesos, etc, para que el
ejecutor de prueba lo tenga disponible en su aplicativo o en su ambiente.

### Desarrollador de software.
Ingeniero que desarrolla el código relacionado al producto de software que estás probando. Es el
responsable de corregir los defectos. Conoce de reglas de negocio y estructuras internas del sistema.

### Matriz de escalamiento.
- Tester
	- Ingeniero de prueba
		- Líder de prueba
			- Test manager
				- Director QA
					- Dirección general
		- Líder de ambientes
		- Líder de PNP
		- Líder de automatización

# Capítulo 4: Herramientas para la ejecución
### Herramienta de gestión de pruebas
Herramienta utilizada para automatizar los procesos de prueba y que ayuda a gestionar todos los
procedimientos para asegurar la calidad como:
  - TestWare
  - Defectos
  - Indicadores
  - Requerimientos
*Sirve para generar, documentar requerimientos, escenarios, casos de prueba, procedimientos de prueba,
obtener indicadores de progreso, avance, número de defectos de una manera mucho más eficaz.*

### Organización de herramientas de prueba.
Es muy importante definirla. Debemos revisar que la herramienta a adquirir tenga estos módulos, pueden
tener diferentes nombres pero el propósito de cada uno es el mismo.
  - **Requirements:** _administar los requerimientos y procesos de negocio._ Hay que tener cuidado en
  administrar los requermientos para tener la trazabilidad contra el testplan o testlab.
  - **Test plan:** _para hacer el diseo de las pruebas._ Administra los casos de prueba, puedes
  organizarlos en escenarios para mantener la trazabilidad al módulo de requerimientos con
  aplicativos o requerimientos.
  - **Test lab:** _ejecución de la prueba o pruebas de laboratorio._ Administra la ejecución de casos
  de prueba, construyes un plan de ejecución, asignas testers y ciclos de prueba.
  - **Defects:** _son todos los defectos, para poderlos administrar._ Administra los defectos detectados
  durante la prueba, configuras el ciclo de vida del defecto y plantillas, administrar el estatus
  del ciclo de vida del defecto.
  - **Dashboard:** _para obtener las métricas en tiempo real de lo que esté sucediendo en Defects o
  TestLab._ Administra los indicadores requeridos para la toma de decisiones en tiempo real y para
  los entregables de calidad. Métricas del progreso, efectividad y número de defectos para determinar
  cuando suspender la prueba, cuando reanudarla y cuando ya esta listo el producto para irse a producción

En una organización de herramientas de prueba es importante que el **testware** esté bien organizado y
bien configurado, los módulos a tomar en cuenta para administrar el testware son:
  - **Requerimientos:** de aquí se desprenden los casos de prueba o escenarios documentados en el testplan
	- **Test Plan:** se obtienen todos los casos de prueba que se van a bajar a la ejecución en el testlab
  - **TestLab:** Es importante que la trazabilidad del módulo de requerimientos, testplan y testlab
  esté bien gestionada.
*Administra la trazabilidad de la materia de prueba de software*

En la organización de herramientas de prueba la **reusabilidad** también es muy importante. Módulos a tomar
en cuenta:
  - **Requerimientos:** es muy fundamental que estén bien configurados con una trazabilidad importante
  para poder identificar los casos de prueba asociados a cierto requerimiento para que el ejecutor o
  diseñador puedan llegar a ellos sin ningún problema
  - **TestPlan:** . En el testplan los casos de prueba tienen que tener un detalle suficiente para que el
  ejecutor lo pueda ejecutar y reusar sin ningún problema ni investigación previa.
*Es importante monitorear el buen uso y enlace de estos módulos para garantizar una buena organización
amigable para facilitar la reusabilidad.*

En la organización de herraminetas de prueba las **métricas** son también muy importantes. Módulos:
  - **Testlab:** es donde se ejecutan los casos de prueba; en el cambio del estatus del caso de prueba
  va asociado a las métricas que vas obteniendo del ciclo de prueba de la efectividad, del progreso, de la
  calidad para que el líder pueda tomar decisiones si la efectividad va tomando un curso adecuado conforme
  al progreso de la prueba que vamos obteniendo, por eso es importante ir documentando los estatus de casos
  de prueba para tomar métricas funcionales.
  - **Defectos:** ir documentando el estatus del defecto ya sea abierto, cerrado, corregido sin error o
  cancelado.
*Es importante monitorear el buen uso de estos dos módulos para obtener siempre métricas reales.*

### Evidencias de pruebas
Existen diferentes tipos de herramientas que nos permiten grabar la evidencia de la prueba que estamos
realizando ya sea exitosa o fallida. Nos permiten grabar videos, tomar fotos de las pantallas o screenshots
y permiten traducirlas a formatos .jpg, .png, entre otras. Una de las herramientas que permiten hacer esto
es Greenshot.

### Administración de Defectos
Es importante registrar defectos, documentar evidencias, generar y mantener el ciclo de vida de un defecto,
los roles involucrados en la administración de defectos como el desarrollador y el tester y los indicadores
que colectamos de la gestión de los defectos. Todo esto es importante para mantener con vida un área de
tester para saber si la calidad de un producto ya está lista para irse a producción porque los defectos
encontrados son de seguridad baja.

### Administración del ambiente
Es muy importante mantener:
  - Datos, siempre vivos, disponibles bajo demanda
  - Diagramas de base de datos
  - Diagrama de servidores, dónde están los servidores, cómo se llaman
  - Diagrama de aplicativos por servidor, en qué aplicativo o en qué servidor tenemos qué aplicativo
  - Batch, hora de ejecución
