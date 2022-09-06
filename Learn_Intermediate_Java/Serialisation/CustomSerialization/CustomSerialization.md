# Custom Serialization

We can modiy the default processes of serialization, such as the 'readObject()' and 'writeObject()' methods (see the file Car.java in this folder to
see a demonstration).

Most of the time the default process of serialization is enough as long as all references implement 'Serializable': the implementation of 'readObject()'
and 'writeObject()' is especially useful when you have a reference field that does not or cannot implement 'Serializable'. You could also potentially handle
'static' field values if you needed to persist them, but this is not good practice as a 'static' field should belong to a class and not an object.