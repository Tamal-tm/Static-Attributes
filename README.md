# Static-Attributes

This repository explains the object-oriented programming (OOP) concepts in Python related to class-level attributes and methods, as well as method access control using private and protected conventions.

Concepts Covered
1. Static (Class) Attributes

Belong to the class rather than any specific object.

Shared across all instances of the class.

Useful for values that should be consistent for every object created from the class.

2. Static Methods

Declared using the @staticmethod decorator.

Do not depend on a specific object (self) or the class itself (cls).

Work like normal functions but are logically grouped inside a class.

Often used for utility or helper functions related to the class’s responsibility.

3. Private Methods (__method)

Indicated by a double underscore prefix (__).

Cannot be accessed directly from outside the class.

Intended for internal use only.

Python applies name mangling to prevent accidental access.

4. Protected Methods (_method)

Indicated by a single underscore prefix (_).

A convention (not enforced by Python) to signal that the method is for internal use.

Can still be accessed, but developers are discouraged from doing so.
