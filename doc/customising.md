# Customising

## Editing Existing Pages

To change a page, simply edit the markdown files in the `doc/` directory and run `phink build`.

## Adding New Pages

To add a new page of documentation:

 * Add a new Markdown file to the `doc/` directory.
 * In the `doc/index.rst` file, add the filename to the `toctree` section (without the `.md` extension).

## Sphinx Configuration

The `phlink init` command generates a sample `doc/conf.py` Sphinx configuration file.
You can customise this to your liking - see the [Sphinx documentation](https://www.sphinx-doc.org/en/master/usage/configuration.html) for full details.

