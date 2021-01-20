============================
collective.volto.blocksfield
============================

Custom z3c.form field that allows to use Volto blocks.

This field can replace RichText fields in your custom content-types.

Features
--------

- store a json object with all blocks informations (data and order)
- restapi serializer/deserializer to manage internal links
- registered custom indexer for `collective.dexteritytextindexer` (if installed)

How to use
----------

Import it and use as a normal field::

    from collective.volto.blocksfield.field import BlocksField

    class IMySchema(Interface):

        my_field = BlocksField(
            title="A field with blocks",
        )


Installation
------------

Install collective.volto.blocksfield by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.volto.blocksfield


and then running ``bin/buildout``

You don't need to install it.

TODO
----

- Tests

Contribute
----------

- Issue Tracker: https://github.com/collective/collective.volto.blocksfield/issues
- Source Code: https://github.com/collective/collective.volto.blocksfield


License
-------

The project is licensed under the GPLv2.

Authors
-------

This product was developed by **RedTurtle Technology** team.

.. image:: https://avatars1.githubusercontent.com/u/1087171?s=100&v=4
   :alt: RedTurtle Technology Site
   :target: http://www.redturtle.it/
