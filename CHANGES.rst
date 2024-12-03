Changelog
=========

2.2.1 (unreleased)
------------------

- Nothing changed yet.


2.2.0 (2024-12-03)
------------------

- Add marker interface to objects that have at least one BlockField in their schema.
  [cekk]
- Add block_types indexer customization for contents with IBlocksFieldEnabled interface to allow index also these blocks.
  [cekk]
- Make package installable: on install, mark already created contents as IBlocksFieldEnabled and reindex them.
  [cekk]

2.1.0 (2024-08-09)
------------------
- Add serializers and deserializer for slate blocks.
  [cekk]
- Add indexer for slate blocks.
  [cekk]

2.0.0 (2023-07-03)
------------------

- Drop support for Plone 5.2 and collective.dexteritytextindexer; in Plone6
  we use core functions in plone.app.dexterity.textindexer
  [lucabel]

1.0.3 (2022-05-31)
------------------

- Fix required python version.
  [cekk]

1.0.2 (2022-05-25)
------------------

- add check if value is a dict in SearchableText indexer.
  [eikichi18]


1.0.1 (2021-03-25)
------------------

- Register standard blocks serializers/deserializer for IDexterityContent. Otherwise they don't work.
  [cekk]


1.0.0 (2021-02-24)
------------------

- Initial release.
  [cekk]
