# Spire.Doc Table Error MWE

This is an MWE for a failure with Spire.Doc when adding a table, possibly related to WLS.

## Installation

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Error

To see the error, run

```bash
./generate.py
```

It should produce a simple word document with a table, but instead produces the error

```
Traceback (most recent call last):
  File "/home/eric/documents/spire-doc-failure-poc/./generate.py", line 20, in <module>
    main()
  File "/home/eric/documents/spire-doc-failure-poc/./generate.py", line 11, in main
    table = Table(doc, True)
  File "/home/eric/documents/spire-doc-failure-poc/venv/lib/python3.9/site-packages/plum/function.py", line 642, in __call__
    return self.f(self.instance, *args, **kw_args)
  File "/home/eric/documents/spire-doc-failure-poc/venv/lib/python3.9/site-packages/plum/function.py", line 592, in __call__
    return _convert(method(*args, **kw_args), return_type)
  File "/home/eric/documents/spire-doc-failure-poc/venv/lib/python3.9/site-packages/spire/doc/Table.py", line 37, in __init__
    intPtr = CallCFunction(GetDllLibDoc().Table_CreateTableDS,intPdoc,showBorder)
  File "/home/eric/documents/spire-doc-failure-poc/venv/lib/python3.9/site-packages/spire/doc/common/__init__.py", line 105, in CallCFunction
    result = func(*args, **kwargs)
RuntimeError: ffi_prep_cif_var failed
Exception ignored in: <function SpireObject.__del__ at 0x7f1d93c1dee0>
Traceback (most recent call last):
  File "/home/eric/documents/spire-doc-failure-poc/venv/lib/python3.9/site-packages/spire/doc/common/SpireObject.py", line 31, in __del__
    CallCFunction(dlllib.Spire_FreeHandle,self.Ptr)
  File "/home/eric/documents/spire-doc-failure-poc/venv/lib/python3.9/site-packages/spire/doc/common/SpireObject.py", line 27, in Ptr
    return self._ptr
AttributeError: 'Table' object has no attribute '_ptr'
```

This is an MWE for a suite of other errors in our main product, all of which contain the line `RuntimeError: ffi_prep_cif_var failed`.
