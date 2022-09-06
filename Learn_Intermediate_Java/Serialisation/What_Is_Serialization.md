# What Is Serialization?

Serialization describes the process of taking an object's state and transforming it into a 'stream of bytes'. A 'stream' is an abstract definition
of a sequence of data that is made available over time, and a 'stream of bytes' is a sequence of bytes that is made available over time.

To serialize an object, its fields and their types are stored in the form of bytes: these bytes are then able to be written to memory, a file, a database,
or sent over a network with all the information necessary to recreate the object.

## Deserialization

Deserialization does the opposite of serialization, and converts a 'stream of bytes' back into an object.

A few key points to note about serialization and deserialization are:

1. The 'stream of bytes' created by serialization only includes the member variables of an object and not its methods.

2. Deserialization creates a copy of the original object: this copy shares the same state but is an entirely new object in memory.