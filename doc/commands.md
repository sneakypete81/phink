# Commands

**Note:** Always run **phink** commands from the root directory of your project.

## Init

```sh
    phink init
```

The `init` command creates a `doc/` directory in your project,
populating it with some sample documentation to get you started.

You should add the `doc/_build/` directory to your `.gitignore`
file, to ensure it isn't accidentally comitted.

## Build

```sh
    phink build
```

The `build` command generates your HTML documentation.
This is output to the `doc/_build/` directory.

## Serve

```sh
    phink serve
```

The `serve` command generates your HTML documentation, starts a local
webserver and provides a URL that you can use to view the documentation.

Any subsequent changes to the documentation source cause the HTML
documentation to be rebuilt and reloaded automatically.
