import pandas as pd
import json
import os

# --- CONFIGURACIÓN ---
EXCEL_FILE = "SEGUIMIENTO DE MATRICULA 2026_27.xlsx"
JSON_OUTPUT = "data_pro.json"

def procesar_gestion_titanium():
    print("🚀 TITANIUM 360: Iniciando motor de procesamiento...")
    
    if not os.path.exists(EXCEL_FILE):
        print(f"❌ Error: No se encuentra {EXCEL_FILE}")
        return

    # 1. Leer todas las hojas del Excel
    xls = pd.ExcelFile(EXCEL_FILE)
    data_consolidada = {"mat": [], "metadata": {"institucion": "TITANIUM 360", "year": "2026_27"}}
    
    for hoja in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=hoja)
        # Limpieza básica: renombrar columnas para estandarizar
        df.columns = [c.upper() for c in df.columns]
        
        # Convertir a formato dict para el JSON
        registros = df.to_dict(orient='records')
        data_consolidada["mat"].extend(registros)

    # 2. Guardar el archivo JSON para el Frontend
    with open(JSON_OUTPUT, 'w', encoding='utf-8') as f:
        json.dump(data_consolidada, f, indent=4, ensure_ascii=False)
    
    print(f"✅ Proceso completado. Archivo '{JSON_OUTPUT}' generado para el panel web.")
    print(f"📊 Total alumnos detectados: {len(data_consolidada['mat'])}")

if __name__ == "__main__":
    procesar_gestion_titanium()
