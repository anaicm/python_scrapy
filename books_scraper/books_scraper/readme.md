Para la realizaci�n del c�digo de este ejercicio.

- En primer lugar, identifico las categorias inspeccionando la pagina y comprobando que los libros son
- 


  - Listo los nodos de las categor�as que contiene la p�gina "https://books.toscrape.com." para obtener todos los enlaces de cada categor�a.
  - Con un bucle hago el recorrido por la lista.
  - Listo el texto de que acompa�a a cada categor�a.
  - Mediante un condicional, compruebo que la categor�a es "Romance".
  - Obtengo el Link de la categor�a "Romance".
  - Uno el link obtenido con la url principal.
  - Lanzo una petici�n con la nueva URL al m�todo "parse_books".
  - Listo los libros ue encuentran en la URL en este caso la categor�a "Romance".
  - Recorro cada uno de ellos mediante un bucle, donde mediante xpath accedo a los nodos y obtengo el t�tulo, precio, stock y url de 
    la imagen del libro.
   Como Stock es un boolean, compruebo mediante constrains() que la etiqueta <p> contiene la clase "instock" ya que esta clase verifica
    que hay stock del libro.
  - Creo una libreria "book_data" en la que guardo los datos obtenidos como es el t�tulo, el precio en el cual realizo un parseo para 
    convertirlo en float ya que lo que recibo es un string, en stock comprueba que tiene la clase "instock" anteriormente mencionada, 
    si es as� devuelve "True" en caso contrario devuelve "False"
    y por �ltimo guardo la URL de cada imagen.
  - Finaliza el m�todo lanzando la libreria "book_data".

En este caso la categor�a "Romance" est� contenida en dos p�ginas, mediante xpath realizo la busqueda del nodo que contien "next" y obtengo
la URL.
Lanzo una petici�n a la url de la p�gina siguiente y realiza el m�todo "parse_books".
    







