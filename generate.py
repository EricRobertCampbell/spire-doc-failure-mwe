#!/usr/bin/env python3

from spire.doc import *
from spire.doc.common import *

def main():
    doc = Document()

    section = doc.AddSection()

    table = Table(doc, True)

    section.Tables.Add(table)

    doc.SaveToFile("table.docx", FileFormat.Docx2019)
    doc.Close()
    doc.Dispose()

if __name__ == "__main__":
    main()
