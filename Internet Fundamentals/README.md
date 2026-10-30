# Fundamentos de Internet

## 1. Del Cliente al Servidor

Cuando buscamos un video en YouTube, nuestro navegador web actúa como **cliente**, ya que solicita información a un servidor. El servidor procesa las solicitudes y devuelve los recursos necesarios para mostrar la página y reproducir el video.

El proceso ocurre de la siguiente manera:

1. **Solicitud y DNS:** Cuando escribimos `https://www.youtube.com` en el navegador, este necesita conocer la dirección IP del servidor. Para eso consulta el sistema DNS, que resuelve el **nombre de dominio** (`www.youtube.com` o `youtube.com`, según la solicitud) a una o más direcciones IP. El DNS no traduce la URL completa, sino el nombre de dominio o nombre de host.
2. **Conexión con el servidor:** Con la dirección IP obtenida, el navegador establece una conexión con el servidor correspondiente. También verifica la seguridad de la conexión mediante TLS cuando utiliza HTTPS.
3. **Solicitud HTTPS:** El navegador envía solicitudes HTTP a través de una conexión segura, por ejemplo, para obtener la página, sus imágenes, archivos JavaScript y los recursos necesarios para el video. YouTube utiliza **HTTPS**, cuya **S significa *Secure* (seguro)**. HTTPS usa TLS para cifrar los datos durante su transmisión, proteger su integridad y verificar la identidad del servidor mediante su certificado digital.
4. **Respuesta del servidor:** El servidor contesta cada solicitud con un **código de estado HTTP** y, cuando corresponde, con contenido. Por ejemplo, `200 OK` significa que la solicitud se procesó correctamente y `404 Not Found` que no se encontró el recurso solicitado.
5. **Visualización:** Finalmente, el navegador interpreta el HTML, CSS y JavaScript recibidos para mostrar la interfaz. En el caso de YouTube, el video puede recibirse en diferentes fragmentos mediante solicitudes adicionales, y el reproductor se encarga de mostrarlos.

Con esto comprendí que el DNS ayuda a encontrar el servidor, mientras que HTTPS permite realizar las solicitudes y recibir las respuestas de manera segura.

## 2. Frontend y Backend en acción

El **frontend** corresponde a la parte visual e interactiva de una aplicación web, es decir, lo que los usuarios ven y utilizan. Incluye menús, logotipos, secciones de la página, formularios, botones, notificaciones y otros elementos de la interfaz. Normalmente se desarrolla con **HTML, CSS y JavaScript**.

El **backend**, por otro lado, se encarga de la lógica de negocio, la validación de datos, la comunicación con las bases de datos y la exposición o integración de APIs. Por ejemplo, en una aplicación para gestionar citas médicas, el backend podría validar la disponibilidad de horarios, guardar las citas y consultar la información autorizada de los pacientes.

El backend puede desarrollarse con distintos **lenguajes de programación**, como Python, Java, JavaScript o C#. Esto no significa que todos produzcan automáticamente el mismo resultado. Lo importante es que el frontend y el backend se comuniquen mediante un **contrato de API**, normalmente usando HTTP o HTTPS y un formato común de intercambio de datos, como **JSON**. Si el backend mantiene los endpoints y el formato de respuesta acordados, el frontend puede trabajar con él sin necesitar saber en qué lenguaje fue programado.

En cuanto a las diferencias entre computadora, tableta y celular, normalmente el backend devuelve los mismos datos y el **frontend adapta su presentación** al tamaño de la pantalla mediante diseño *responsive*. Esto se puede lograr con CSS, por ejemplo, usando **media queries**, que permiten cambiar la disposición de los elementos según el ancho disponible.

Por lo tanto, **no es necesario modificar el backend únicamente para que una página se vea correctamente en un celular**. Esa adaptación suele resolverse en el frontend. El backend solo necesitaría cambios si hubiera requisitos diferentes de datos, funcionalidades o rendimiento para ciertos dispositivos.

Las APIs facilitan esta comunicación usando métodos HTTP como **GET** para consultar recursos, **POST** para enviar o crear, **PUT/PATCH** para actualizar y **DELETE** para eliminar.

## 3. REST vs SOAP vs GraphQL

| Tipo de API | Formato de datos usado | Nivel de flexibilidad | Dificultad de implementación | Uso actual (Alta / Media / Baja) |
|---|---|---|---|---|
| **REST** | Principalmente JSON; también puede utilizar XML u otros formatos | Alta. Permite trabajar con diferentes recursos y operaciones HTTP | Baja a media | Alta |
| **SOAP** | XML | Más estructurada, con reglas y contratos formales | Alta | Media, especialmente en sistemas empresariales |
| **GraphQL** | Habitualmente JSON en sus respuestas | Muy alta, ya que el cliente puede solicitar campos específicos | Media a alta | Alta en determinados tipos de aplicaciones |

**¿Cuál es más apropiada para una startup moderna? ¿Por qué?**

REST es una opción muy apropiada para una startup moderna, especialmente durante sus primeras etapas. Esto se debe a que es relativamente fácil de implementar, flexible, escalable y compatible con la mayoría de los lenguajes de programación y tecnologías actuales. Además, utiliza frecuentemente JSON, un formato ligero que facilita el intercambio de información.

> **Aclaración:** SOAP no está descontinuado. Aunque REST es muy frecuente en aplicaciones web modernas, SOAP todavía se utiliza en algunos sistemas empresariales.

## 4. Explorando APIs con Postman

### 4.1 Selección de la API

- **Nombre de la API:** JSONPlaceholder.
- **Descripción:** JSONPlaceholder es una API REST gratuita diseñada para realizar pruebas y practicar la comunicación entre aplicaciones y servidores. Proporciona datos simulados sobre usuarios, publicaciones, comentarios, álbumes y otras categorías.

Permite realizar solicitudes HTTP para consultar, crear, modificar y eliminar recursos simulados. Es ideal para aprender a utilizar Postman porque no requiere autenticación y sus respuestas utilizan el formato JSON.

### 4.2 Configuración en Postman

- **Nombre de la colección:** JSONPlaceholder API.
- **API utilizada:** JSONPlaceholder.
- **URL base:** `https://jsonplaceholder.typicode.com`.
- **Variable de colección:** `base_url`.
- **Valor de la variable:** `https://jsonplaceholder.typicode.com`.
- **Solicitudes agregadas:** GET, POST, PUT y DELETE.

**Configuración de la variable `base_url`:**

1. Abrir la colección **JSONPlaceholder API** en Postman.
2. Ingresar en la pestaña **Variables** de la colección.
3. Crear la variable `base_url` y asignarle el valor `https://jsonplaceholder.typicode.com`.
4. Guardar los cambios y reemplazar la dirección repetida en cada request por `{{base_url}}`.

De esta manera, si cambia el dominio de la API, solo necesito actualizar el valor de la variable, en lugar de modificar cada solicitud. Utilicé una **variable de colección** porque se comparte entre los requests de esta práctica y no requiere una variable global.

**Solicitudes configuradas:**

| Nombre descriptivo del request | Método | URL en Postman | Objetivo |
|---|---|---|---|
| Obtener publicación | GET | `{{base_url}}/posts/1` | Consultar la publicación con ID 1. |
| Crear publicación | POST | `{{base_url}}/posts` | Simular la creación de una publicación. |
| Actualizar publicación | PUT | `{{base_url}}/posts/1` | Simular la actualización de la publicación con ID 1. |
| Eliminar publicación | DELETE | `{{base_url}}/posts/1` | Simular la eliminación de la publicación con ID 1. |

**Configuración adicional:**

- No se requiere autenticación ni un token de acceso.
- Se utiliza JSON para enviar y recibir información.
- En las solicitudes POST y PUT, se configura el encabezado `Content-Type: application/json`.
- Las solicitudes están agrupadas dentro de una colección, con nombres que indican la acción que realizan.
- En la práctica original se guardaron respuestas como ejemplos en Postman; al importar una colección nueva, esos ejemplos no se transfieren automáticamente a menos que estén incluidos en la exportación.

### 4.3 Ejecución y análisis

Durante la práctica se ejecutaron cuatro solicitudes HTTP utilizando Postman. Los resultados registrados fueron los siguientes:

| Solicitud | Método | Endpoint | Código de estado | Notas |
|---|---|---|---|---|
| Obtener publicación | GET | `/posts/1` | `200 OK` | Se obtuvo la información de la publicación con ID 1. |
| Crear publicación | POST | `/posts` | `201 Created` | Se simuló la creación de una publicación y se recibió el ID 101. |
| Actualizar publicación | PUT | `/posts/1` | `200 OK` | Se recibió la publicación con los datos modificados. |
| Eliminar publicación | DELETE | `/posts/1` | `200 OK` | Se recibió un objeto JSON vacío (`{}`) como resultado de la eliminación simulada. |

**Análisis de los resultados**

Todas las solicitudes registradas en la práctica original fueron ejecutadas exitosamente. Se comprobó que cada método HTTP cumple una función diferente y que los códigos de estado permiten identificar el resultado de las operaciones.

Las respuestas se recibieron en formato JSON. Además, se utilizó el encabezado `Content-Type: application/json` para indicar el formato de los datos enviados en las solicitudes POST y PUT.

Es importante mencionar que JSONPlaceholder es una API de pruebas, por lo que las operaciones de creación, actualización y eliminación son simuladas y **no modifican permanentemente** los datos del servidor.

### 4.4 Explicación técnica

#### 1. GET - Obtener publicación

- **Método HTTP:** GET.
- **URL en Postman:** `{{base_url}}/posts/1`.
- **Endpoint:** `/posts/1`.
- **Parámetros / Body:** No requiere un body. El número `1` identifica la publicación que se desea consultar.
- **Descripción de la respuesta:** El servidor devuelve un objeto JSON que contiene el identificador del usuario, el identificador de la publicación, el título y el contenido.

Ejemplo ilustrativo de respuesta JSON (contenido abreviado):

```json
{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "..."
}
```

- **Código de estado:** `200 OK`.

#### 2. POST - Crear publicación

- **Método HTTP:** POST.
- **URL en Postman:** `{{base_url}}/posts`.
- **Endpoint:** `/posts`.
- **Parámetros / Body:** Se envía el siguiente JSON:

```json
{
  "title": "Mi primera API",
  "body": "Estoy aprendiendo a utilizar Postman",
  "userId": 1
}
```

**Descripción de la respuesta:** El servidor recibe los datos, simula la creación de una publicación y devuelve un objeto JSON que incluye el identificador asignado.

Ejemplo de respuesta JSON:

```json
{
  "title": "Mi primera API",
  "body": "Estoy aprendiendo a utilizar Postman",
  "userId": 1,
  "id": 101
}
```

- **Código de estado:** `201 Created`.

#### 3. PUT - Actualizar publicación

- **Método HTTP:** PUT.
- **URL en Postman:** `{{base_url}}/posts/1`.
- **Endpoint:** `/posts/1`.
- **Parámetros / Body:** Se envía el siguiente JSON:

```json
{
  "id": 1,
  "title": "Publicación modificada",
  "body": "Estoy aprendiendo a actualizar datos con PUT en Postman",
  "userId": 1
}
```

**Descripción de la respuesta:** El servidor procesa la solicitud de actualización simulada y devuelve la información de la publicación con los valores modificados.

Ejemplo de respuesta JSON:

```json
{
  "id": 1,
  "title": "Publicación modificada",
  "body": "Estoy aprendiendo a actualizar datos con PUT en Postman",
  "userId": 1
}
```

- **Código de estado:** `200 OK`.

#### 4. DELETE - Eliminar publicación

- **Método HTTP:** DELETE.
- **URL en Postman:** `{{base_url}}/posts/1`.
- **Endpoint:** `/posts/1`.
- **Parámetros / Body:** No requiere parámetros adicionales ni un body. El identificador se encuentra en la URL.
- **Descripción de la respuesta:** El servidor simula la eliminación y devuelve un objeto JSON vacío, indicando que la solicitud fue exitosa.

Ejemplo de respuesta JSON:

```json
{}
```

- **Código de estado:** `200 OK`.

**¿Qué aprendiste del proceso?**

Durante esta práctica aprendí a utilizar Postman para enviar solicitudes HTTP y comunicarme con una API REST. Comprendí las diferencias entre los métodos GET, POST, PUT y DELETE, así como la importancia de utilizar correctamente los endpoints, los cuerpos de las solicitudes y los códigos de estado.

También aprendí a organizar solicitudes dentro de una colección, guardar respuestas y trabajar con información en formato JSON. Además, comprendí que utilizar una variable como `base_url` facilita el mantenimiento de las solicitudes, porque evita repetir la dirección del servidor.

### 4.5 Reflexión final

Esta actividad me permitió comprender mejor cómo funcionan las APIs y cómo facilitan la comunicación entre diferentes sistemas. Aprendí que las aplicaciones pueden solicitar, enviar, actualizar y eliminar información utilizando métodos HTTP específicos. También entendí la importancia de los códigos de respuesta para determinar si las operaciones se realizaron correctamente y cómo JSON permite intercambiar información de una manera estructurada.

Postman me ayudó a visualizar de forma práctica la comunicación entre cliente y servidor sin necesidad de escribir un programa completo. Al realizar cada solicitud, pude observar qué información se enviaba, cómo el servidor la procesaba y qué respuesta devolvía. Considero que esta herramienta es útil para el desarrollo de software porque permite probar APIs, identificar errores y comprender mejor su funcionamiento antes de integrarlas en una aplicación.
