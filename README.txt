Los 2 ejercicios fueron escritos en python 3.7, solo se necesita instalarlo y correr cada uno en la terminal desde la carpeta raíz con el comando 
py (nombre archivo)


FirstProblem.py
Ejecutar programa, el preguntara por numero de operaciones, colocar un valor entero. Acto seguido el preguntara por las N operaciones con el texto 'indique operación'; este saldrá N veces donde se colocara en el formato establecido en el pdf (operación) (numero) 
ejemplo: 
7
r 1
a 1
a 2
a 1
r 1
r 2
r 1

SecondProblem.py
Ejecutar programa,  el preguntara por el numero de nodos, colocar un entero, seguido preguntara por los colores de los n nodos, lo cual corresponde a digitar los 5 enteros seguidos separados por un espacio, luego preguntara por las relaciones de los nodos las cuales estarán formadas por los dos nodos, padre e hijo seguidos de un espacio (nodo padre) (nodo hijo) 
ejemplo:
5
1 2 3 2 3
1 2
2 3
2 4
1 5


Nuta: el ejercicio solo lo tengo hasta la construcción del árbol con todas sus relaciones, el algoritmo de búsqueda para hacer la sumatoria de colores distintos entre dos nodos, así nodo por nodo no lo tengo


Cuales serian las cualidades para un código limpio?
usar siempre nombres con significado
usar unidades de código pequeñas
única responsabilidad
funciones con numero limitado de argumentos
no te repitas tu mismo
evitar comentarios
utilizar un formato único en tu código
abstraer datos, no usar getters y setters indiscriminadamente
objetos independientes
manejo excepciones
establecer fronteras sobre código que no controlamos
escribe test
utiliza patrones para problematicas frecuentes, alguien mas ya pudo haber tenido el problema y puede que haya un patron que te ayude


Cuales serian los estándares según tú para un buen proyecto?
A nivel de proyecto no solo pensar en código para cumplir a otra area, pensar mas en código para negocio, estar siempre pensando en concepto de empresa extendida y como este ayuda a cumplir los objetivos estratégicos y la misión de la empresa.
Los proyectos depende se personas, de equipos, de lideres, de motivación. Adoptar una metodología de proyecto como el pmbook es recomendable y hacer trabajo en lo posible con ágiles ya que el mercado así lo requiere, donde podemos entregar valor mas rápido al cliente en entrgas continuas siempre involucardolo.
Tener un buen equipo de trabajo, gente capacitada en su labor y a nivel de tecnologia siempre tener una arquitectura base y una to-be donde proyectemos nuestros esfuerzos de una manera organizada siguiendo una nuestra arquitectura como mas le convenga a la empresa siguiendo patrones que nos permitan hacer bien y de buena calidad las cosas y resolviendo nuestros problemas a nivel empresarial


Qué patrones conoce? y utiliza?
Muchos dependiendo el problema pero los que mas utilizo en la vida diaria tanto de diseño y arquitectura son
client server
N-layers
broker
forwarder receiver (muchos de integración)
logic centralization (muchos de SOA)
content negociation
decouple contract
publisher subscriber
dead letter
invalid message
guaranteed delivery
legacy wrapper
domain inventory
enterptise inventory
canonical schema
exception shelding
entre otros, estos son algunos pero repito dependiendo el problema se aplica el patrón
