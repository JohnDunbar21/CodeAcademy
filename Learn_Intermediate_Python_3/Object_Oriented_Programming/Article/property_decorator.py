"""
When using the @property decorator, remeber 3 rules:

1. All three methods must use the same name (ex. weight).
2. The first method must be the getter and is identified using @property.
3. The decorators for the setter and deleter are defined by the name of the method @property
   is used with (ex; weight.setter, weight.deleter).
"""