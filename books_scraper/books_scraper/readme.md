Para la realización del código de este ejercicio.

- En primer lugar, identifico las categorias inspeccionando la pagina y comprobando que los libros son
- 


  - Listo los nodos de las categorías que contiene la página "https://books.toscrape.com." para obtener todos los enlaces de cada categoría.
  - Con un bucle hago el recorrido por la lista.
  - Listo el texto de que acompaña a cada categoría.
  - Mediante un condicional, compruebo que la categoría es "Romance".
  - Obtengo el Link de la categoría "Romance".
  - Uno el link obtenido con la url principal.
  - Lanzo una petición con la nueva URL al método "parse_books".
  - Listo los libros ue encuentran en la URL en este caso la categoría "Romance".
  - Recorro cada uno de ellos mediante un bucle, donde mediante xpath accedo a los nodos y obtengo el título, precio, stock y url de 
    la imagen del libro.
   Como Stock es un boolean, compruebo mediante constrains() que la etiqueta <p> contiene la clase "instock" ya que esta clase verifica
    que hay stock del libro.
  - Creo una libreria "book_data" en la que guardo los datos obtenidos como es el título, el precio en el cual realizo un parseo para 
    convertirlo en float ya que lo que recibo es un string, en stock comprueba que tiene la clase "instock" anteriormente mencionada, 
    si es así devuelve "True" en caso contrario devuelve "False"
    y por último guardo la URL de cada imagen.
  - Finaliza el método lanzando la libreria "book_data".

En este caso la categoría "Romance" está contenida en dos páginas, mediante xpath realizo la busqueda del nodo que contien "next" y obtengo
la URL.
Lanzo una petición a la url de la página siguiente y realiza el método "parse_books".
    







