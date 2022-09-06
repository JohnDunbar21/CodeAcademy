# Serializing Associated Fields

Not only can primitives such as 'int' or 'long' be serialized, but also references.

In order for reference types to be serializable, they must also implement the 'Serializable' interface, which the 'String' class does.
If the reference did not implement 'Serializable', then we would get a 'NotSerializableException' thrown. When the JVM encounters a reference
type, it will try to serialize the reference type first before trying to serialize the encapsulating object.

Most of the time, serializable classes will have a combination of reference and primitive types.