Fundamentos de Internet 

##
 1. Del Cliente al Servidor
Respuesta: El cliente que solicita la informacion cuando buscamos un video en youtube a lo que se espera que el servidor responda con el video solicitado. Siendo nuestro navegador web el cliente solicitando el video. Entonces nuestra computadora  hacer un requesto a un servidor DNS que se va encarga de transformar la url de youtube.com al IP publica de la pagina web. Entonces con la web que obtenes atraves del DNS, nuestro navegador genera otro request directo a la IP que el DNS nos compartio,
El protocolo http entra cuando vamos a youtube y estamos haciendo un HTTP REQUESTS a los servidores de youtube.com
##
 2. Frontend y Backend en acción
Respuesta: El frontend se conecta con toda la interfaz grafica relacionado con la experiencia de los usuarions, el frontend se situaria
directamente con la visualizacion de menus, logos, seccions de web, interacciones de usuarios, notificaciones y mas donde se podria construir con HTML, JAVASCRIPT, CSS. Luego el backend, estaria construyendo todas las integraciones de APIs para incluir o conseguir informacion, tambien como la logica del requisito de guardar cita, conectar informacion de los pacientes, validacion de datos y mas. Puede utilizar cualquier tipo de idioma de programacion ya que el resultado siempre sera el mismo y el lenguaje de progamacion para el backend se encuentra armonizado.

Por lo tanto, si la pagina podria tener diferente tipos de visualizaciones dependiendo desde donde se este visualizando, donde el momento el momento se realice el HTTP request, el frontend hara la conexion indicada con el tipo de dispositivo y asi traducir y acomodar la informacion de sus APIs y exista la mejor interface visual acorde los datos de las APIs mediantes GETs, POSTs, PATCHs, DELETEs, etc...
##
 3. REST vs SOAP vs GraphQL

|
 Tipo de API

|
 Formato de datos usado 
|
 Nivel de flexibilidad 
|
 Dificultad de implementación 
|
 Uso actual (Alta / Media / Baja) 
|
|
-------------
|
------------------------
|
------------------------
|
-------------------------------
|
-----------------------------------
|
|
 REST        
|JSON, XML y otros mas
|Alta -Pero el cliente puede obtener diferencia al hacer el request de informacion por diferencia en errores
|Baja-Media
|Alta
|

 SOAP        
|XML
|Baja - Todos los APIs tienen que seguir una misma regla y estructura. Se esta discontinuando
|Alta
|Alta
|

 GraphQL     
|JSON
|Muy alta ya que el cliente se le permite solicitar datos especificos
|Media-Alta
|Alta
|

**
¿Cuál es más apropiada para una startup moderna? ¿Por qué?
**
REST es la opción más apropiada para una startup moderna, especialmente durante sus primeras etapas.

Esto se debe a que es fácil de implementar, flexible, escalable y compatible con la mayoría de los lenguajes de programación y tecnologías actuales. Además, utiliza principalmente JSON, un formato ligero que facilita el intercambio de información.
##
 4. Explorando APIs con Postman

###
 4.1 Selección de la API

-
 
**
Nombre de la API: JSONPlaceholder
**

-
 
**
Descripción: JSONPlaceholder es una API REST gratuita diseñada para realizar pruebas y practicar la comunicación entre aplicaciones y servidores. Proporciona datos simulados sobre usuarios, publicaciones, comentarios, álbumes y otras categorías.

Permite realizar solicitudes HTTP para consultar, crear, modificar y eliminar recursos simulados. Es ideal para aprender a utilizar Postman porque no requiere autenticación y sus respuestas utilizan el formato JSON

###
4.2 Configuración en Postman

Nombre de la colección: JSONPlaceholder API

API utilizada: JSONPlaceholder

URL base: https://jsonplaceholder.typicode.com

Solicitudes agregadas: GET / POST / PUT / DELETE

Solicitudes configuradas

GET - Obtener publicación: Permite consultar la información de una publicación existente mediante su identificador.

POST - Crear publicación: Permite enviar información en formato JSON para simular la creación de una publicación.

PUT - Actualizar publicación: Permite modificar los datos de una publicación existente utilizando su identificador.

DELETE - Eliminar publicación: Permite solicitar la eliminación de una publicación específica.

Configuración adicional:

No se requiere autenticación.

No se necesita un token de acceso.

Se utiliza JSON para enviar y recibir información.

Las solicitudes fueron organizadas y guardadas dentro de una colección en Postman.

Las respuestas obtenidas fueron almacenadas como ejemplos dentro de la colección.

4.3 Ejecución y análisis

Se ejecutaron cuatro solicitudes HTTP utilizando Postman. Los resultados obtenidos fueron los siguientes:

Solicitud

Método

Endpoint

Código de estado

Notas

Obtener publicación

GET

/posts/1

200 OK

Se obtuvo correctamente la información de la publicación con ID 1.

Crear publicación

POST

/posts

201 Created

Se simuló la creación de una publicación y se recibió el ID 101.

Actualizar publicación

PUT

/posts/1

200 OK

Se recibió la publicación con los datos modificados.

Eliminar publicación

DELETE

/posts/1

200 OK

Se recibió un objeto JSON vacío {} como resultado de la eliminación simulada.

Análisis de los resultados

Todas las solicitudes fueron ejecutadas exitosamente.

Se comprobó que cada método HTTP cumple una función diferente y que los códigos de estado permiten identificar el resultado de las operaciones.

Las respuestas se recibieron en formato JSON. Además, se utilizó el encabezado Content-Type: application/json para indicar el formato de los datos enviados en las solicitudes POST y PUT.

Es importante mencionar que JSONPlaceholder es una API de pruebas, por lo que las operaciones de creación, actualización y eliminación son simuladas y no modifican permanentemente los datos del servidor.

4.4 Explicación técnica

1. GET - Obtener publicación

Método HTTP: GET

Endpoint:

https://jsonplaceholder.typicode.com/posts/1

Parámetros / Body:

No requiere un Body. El número 1 dentro de la URL identifica la publicación que se desea consultar.

Descripción de la respuesta:

El servidor devuelve un objeto JSON con la información de la publicación solicitada, incluyendo el identificador del usuario, el identificador de la publicación, el título y su contenido.

Ejemplo de respuesta JSON:

{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
}

Código de estado: 200 OK

2. POST - Crear publicación

Método HTTP: POST

Endpoint:

https://jsonplaceholder.typicode.com/posts

Parámetros / Body:

Se envió el siguiente JSON:

{
  "title": "Mi primera API",
  "body": "Estoy aprendiendo a utilizar Postman",
  "userId": 1
}

Descripción de la respuesta:

El servidor recibe los datos enviados, simula la creación de una nueva publicación y devuelve un objeto JSON que incluye el identificador asignado.

Ejemplo de respuesta JSON:

{
  "title": "Mi primera API",
  "body": "Estoy aprendiendo a utilizar Postman",
  "userId": 1,
  "id": 101
}

Código de estado: 201 Created

3. PUT - Actualizar publicación

Método HTTP: PUT

Endpoint:

https://jsonplaceholder.typicode.com/posts/1

Parámetros / Body:

Se envió el siguiente JSON:

{
  "id": 1,
  "title": "Publicación modificada",
  "body": "Estoy aprendiendo a actualizar datos con PUT en Postman",
  "userId": 1
}

Descripción de la respuesta:

El servidor procesa la solicitud de actualización y devuelve la información de la publicación con los valores modificados.

Ejemplo de respuesta JSON:

{
  "id": 1,
  "title": "Publicación modificada",
  "body": "Estoy aprendiendo a actualizar datos con PUT en Postman",
  "userId": 1
}

Código de estado: 200 OK

4. DELETE - Eliminar publicación

Método HTTP: DELETE

Endpoint:

https://jsonplaceholder.typicode.com/posts/1

Parámetros / Body:

No requiere parámetros adicionales ni un Body. El identificador de la publicación se encuentra en la URL.

Descripción de la respuesta:

El servidor procesa la solicitud de eliminación y devuelve un objeto JSON vacío, indicando que la operación simulada fue exitosa.

Ejemplo de respuesta JSON:

{}

Código de estado: 200 OK

¿Qué aprendiste del proceso?

Durante esta práctica aprendí a utilizar Postman para enviar solicitudes HTTP y comunicarme con una API REST. Comprendí las diferencias entre los métodos GET, POST, PUT y DELETE, así como la importancia de utilizar correctamente los endpoints, los cuerpos de las solicitudes y los códigos de estado.

También aprendí a organizar solicitudes dentro de una colección, guardar respuestas y trabajar con información en formato JSON. Además, comprendí que una respuesta exitosa no siempre significa que la información haya sido modificada permanentemente en el servidor.

4.5 Reflexión final

Esta actividad me permitió comprender mejor cómo funcionan las APIs y cómo facilitan la comunicación entre diferentes sistemas. Aprendí que las aplicaciones pueden solicitar, enviar, actualizar y eliminar información utilizando métodos HTTP específicos. También entendí la importancia de los códigos de respuesta para determinar si las operaciones se realizaron correctamente y cómo JSON permite intercambiar información de una manera estructurada.

Postman me ayudó a visualizar de forma práctica la comunicación entre cliente y servidor sin necesidad de escribir un programa completo. Al realizar cada solicitud, pude observar qué información se enviaba, cómo el servidor la procesaba y qué respuesta devolvía. Considero que esta herramienta es útil para el desarrollo de software porque permite probar APIs, identificar errores y comprender mejor su funcionamiento antes de integrarlas en una aplicación.