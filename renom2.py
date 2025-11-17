import os
import shutil

ruta_base = r"C:\Users\carls\Desktop\APP_AFECCIONES\CARM\CATASTRO_CARM\CASTILLA LA MANCHA\CATASTRO"

extensiones = [".shp", ".shx", ".dbf", ".prj", ".cpg", ".xml", ".sbx", ".sbn", ".qix", ".qpj"]

renombrados = 0
cpg_creados = 0

print("Renombrando TODOS los archivos al nombre del municipio + UTF-8...\n")

for root, dirs, files in os.walk(ruta_base):
    municipio = os.path.basename(root).strip()
    padre = os.path.basename(os.path.dirname(root))
    
    # Solo entramos en carpetas de municipios (dentro de las provincias)
    if padre in ["ALBACETE", "CIUDAD REAL", "CUENCA", "GUADALAJARA", "TOLEDO"]:
        if len(municipio) > 0 and municipio != "CATASTRO":
            
            # Buscamos el primer .shp que haya → ese será el "principal"
            shp_actual = None
            for f in files:
                if f.lower().endswith(".shp"):
                    shp_actual = f
                    break
            
            if shp_actual:  # hay shapefile en esta carpeta
                base_actual = os.path.splitext(shp_actual)[0]
                
                for ext in extensiones:
                    viejo = os.path.join(root, base_actual + ext)
                    nuevo = os.path.join(root, municipio + ext)
                    
                    if os.path.exists(viejo):
                        if os.path.exists(nuevo):
                            os.remove(nuevo)  # borramos si ya existía (por seguridad)
                        shutil.move(viejo, nuevo)
                        print(f"{municipio}{ext}")
                        renombrados += 1
                
                # Forzamos el .cpg con UTF-8 (aunque ya exista)
                cpg_path = os.path.join(root, municipio + ".cpg")
                with open(cpg_path, "w", encoding="utf-8") as f:
                    f.write("UTF-8")
                cpg_creados += 1

print("\n" + "="*50)
print("¡TODO LISTO!")
print(f"Municipios procesados: {cpg_creados}")
print(f"Archivos renombrados en total: {renombrados}")
print("Todos los shapefiles se llaman ahora como su municipio y tienen .cpg UTF-8")
input("\nPulsa Enter para cerrar...")