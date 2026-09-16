# CatOS-Espruino Embed

This repository contains the minimal Espruino sources required to generate the
embeddable interpreter used by CatOS.

## Build

```bash
make BOARD=EMBED
```

The generated files are written to `bin/`:

- `espruino_embedded.c`
- `espruino_embedded.h`
- `espruino_embedded_utils.h`
- `jstypes.h`

CatOS Builder normally runs this build in Docker as part of `catos build` when
the project references the `catos-espruino` dependency.

The full multi-board Espruino SDK, hardware target libraries, documentation and
tests are intentionally excluded from this EMBED-only repository.
