str = "UEsDBBQABgAIAAAAIQC5S0K4agEAAKcFAAATAAgCW0NvbnRlbnRfVHlwZXNdLnhtbCCi"


import base64

b64_data = """UEsDBBQABgAIAAAAIQC5S0K4agEAAKcFAAATAAgCW0NvbnRlbnRfVHlwZXNd...
"""  # kompletter String hier einfügen
with open("Pruefziele_Orale_Medizin.xlsx", "wb") as f:
    f.write(base64.b64decode(b64_data))
print("Datei wurde gespeichert.")