### Streem proto decoder

Decoder for `pbmesh` and `pblayout` files from Streem backend.

```
# Install requiremensts
pip install -r requirements.txt

# Usage
Streem proto message decoder

usage: decoder.py [-h] [--input-mesh INPUT_PBMESH] [--output-mesh OUTPUT_OBJ] [--input-pblayout INPUT_PBLAYOUT]


optional arguments:
  -h, --help            show this help message and exit
  --input-mesh INPUT_PBMESH
                        Location of the input pbmesh file (defaults a pbmesh file in data folder)
  --output-mesh OUTPUT_OBJ
                        Location of the output obj file to export (defaults to test.obj in data folder)
  --input-pblayout INPUT_PBLAYOUT
                        Location of the input pblayout file (defaults to a pblayout file in data folder)
```

Example: decode the sample pbmesh and pblayout files in this folder
```
python3 decoder.py  

Exported mesh to data/test.obj
Vertices - [[-1.46313    -1.25905001  1.50556004]
 [-1.89444005 -1.26607001 -1.41409004]
 [ 1.03298998 -1.26568997 -1.87237   ]
 [ 1.50516999 -1.25838995  1.16159999]]
Layout area - 8.956459999084473
```

Please refer to [Proto definitions](./proto_defs.md) for schemas of the proto messages. Please note, this is only to read the schema for documentation purposes **only**.


