from spire.doc import *
from spire.doc.common import *

def main():
    doc = Document()

    section = doc.AddSection()

    table = Table(doc, True)
    table.ResetCells(3,3)
    section.Tables.Add(table)
    # section.AddParagraph().AppendText("hello")
    doc.SaveToFile("table.docx", FileFormat.Docx2019)
    doc.Close()
    doc.Dispose()

if __name__ == "__main__":
    main()

