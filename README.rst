===================
Repository Pattern 
===================



This is a sample project to demonstrate an implementation and benefits of the ``Repository`` pattern in python.


* Why use the repository pattern?

The beautfy of this pattern is enhanced when used together with DIP (dependency inversion principle), where it states
that we should not depend on implementations but rather abstractions.

We also get the benefit of being able to easily mock our "service layer" (database accesses), since we can create a Fake that follows the same interface
and use it to test components that depend on external sources (With some changes you can also create a repository for an external API).

This is shown in the integration tests, where we use the fake to test components that need the a repository.


* SPECIAL NOTE:

This is an example repository and I don't advice you to import it to your project and use it as package, rather you should take it as reference
and adapt it to your needs


* Running:

I recommend developing with VScode and docker container (DockerFile provided). You can install this project as a packag  `make install` or create a wheel
via `make dist`.



* Free software: MIT license


Features
--------

* Abstract classes for SQL and NoSQL repositories.
* Working example for SQL based repositories.
* Two SqlRepositories, ``PandasSqlRepository`` and ``SqlLite3Repository``.
* ``FakeSqlRepository`` used to show the benefits of its approach. alongside tests.
* ``MongoSqlRepository`` and ``FakeMongoRepository`` (no tests or example yet, and probably never will, but are kept there).


-------

This package was created with Cookiecutter_ and the `ZordoC/cookiecutter-simple-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/ZordoC/cookiecutter-simple-pypackage
