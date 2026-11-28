#!/usr/bin/env python3
"""Calcula votación, correlación MoSCoW-votación y tablas de comparación.

Se ejecuta con: python3 datos/calcular_resultados.py
Usa únicamente la biblioteca estándar. No modifica las fuentes de terceros.
"""
import csv
import json
import math
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
DATOS = RAIZ / 'datos'
SALIDA = DATOS / 'calculos'
TABLAS = RAIZ / 'tablas'
PRIORIDAD = {'Must': 0, 'Should': 1, 'Could': 2, 'Wont': 3, "Won't": 3}
IDS = [f'RF-{i:02d}' for i in range(1, 13)] + [f'RNF-{i:02d}' for i in range(1, 9)]
VOTANTES = ('P06', 'P07', 'P08')


def cargar(ruta, encabezado):
    with ruta.open(encoding='utf-8-sig', newline='') as f:
        lector = csv.DictReader(f)
        if lector.fieldnames != encabezado:
            raise ValueError(f'Encabezado incorrecto en {ruta.name}: {lector.fieldnames}')
        filas = list(lector)
        if any(None in fila or any(v is None for v in fila.values()) for fila in filas):
            raise ValueError(f'CSV con campos incorrectos: {ruta.name}')
    return filas


def rangos_medios(valores, descendente=False):
    orden = sorted(valores, key=lambda k: ((-valores[k]) if descendente else valores[k], k))
    resultado = {}
    i = 0
    while i < len(orden):
        j = i + 1
        while j < len(orden) and valores[orden[j]] == valores[orden[i]]:
            j += 1
        medio = (i + 1 + j) / 2
        for k in orden[i:j]:
            resultado[k] = medio
        i = j
    return resultado


def spearman(x, y):
    claves = list(x)
    a = sum(x.values()) / len(claves)
    b = sum(y[k] for k in claves) / len(claves)
    numerador = sum((x[k] - a) * (y[k] - b) for k in claves)
    vx = sum((x[k] - a) ** 2 for k in claves)
    vy = sum((y[k] - b) ** 2 for k in claves)
    if vx == 0 or vy == 0:
        raise ValueError('Spearman indefinido: al menos un orden tiene varianza nula')
    return numerador / math.sqrt(vx * vy)


def guardar_csv(ruta, encabezado, filas):
    with ruta.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=encabezado, lineterminator='\n')
        w.writeheader()
        w.writerows(filas)


def tabla(nombre, titulo, etiqueta, encabezados, filas, ancho):
    columnas = len(encabezados)
    lineas = [r'\begingroup', r'\small', r'\begin{longtable}{@{}' + ancho + r'@{}}',
              r'\caption{' + titulo + r'}\label{' + etiqueta + r'}\\',
              r'\toprule', ' & '.join(r'\textbf{' + h + '}' for h in encabezados) + r'\\',
              r'\midrule', r'\endfirsthead', r'\toprule',
              ' & '.join(r'\textbf{' + h + '}' for h in encabezados) + r'\\',
              r'\midrule', r'\endhead', r'\bottomrule', r'\endlastfoot']
    for valores in filas:
        if len(valores) != columnas:
            raise ValueError(f'Número de celdas incorrecto: {nombre}')
        lineas.append(' & '.join(str(valor).replace('&', r'\&').replace('%',r'\%') for valor in valores) + r'\\')
    lineas += [r'\end{longtable}', r'\endgroup']
    (TABLAS/nombre).write_text('\n'.join(lineas)+'\n', encoding='utf-8')


def calcular():
    catalogo = cargar(DATOS/'requisitos.csv', ['id','tipo','nombre','texto','verificacion'])
    if len(catalogo) != 20 or {r['id'] for r in catalogo} != set(IDS):
        raise ValueError('Catálogo de requisitos distinto al vigente')
    nombres = {r['id']:r['nombre'] for r in catalogo}
    votos = cargar(DATOS/'votos.csv', ['participante_id','requisito_id','puntos'])
    if len(votos) != 60 or {(r['participante_id'],r['requisito_id']) for r in votos} != {(p,k) for p in VOTANTES for k in IDS}:
        raise ValueError('La votación requiere 60 registros únicos: 20 por cada votante P06-P08')
    totales = defaultdict(int)
    por_persona = defaultdict(int)
    for r in votos:
        valor = r['puntos']
        if not valor.isascii() or not valor.isdigit():
            raise ValueError(f'Puntuación no entera y no negativa: {r}')
        puntos = int(valor)
        totales[r['requisito_id']] += puntos
        por_persona[r['participante_id']] += puntos
    if any(por_persona[p] != 100 for p in VOTANTES) or sum(totales.values()) != 300:
        raise ValueError(f'Suma de votos inválida: {dict(por_persona)}')
    moscow = cargar(DATOS/'moscow.csv', ['id','categoria','esfuerzo','justificacion'])
    if len(moscow) != 20 or {r['id'] for r in moscow} != set(IDS):
        raise ValueError('MoSCoW requiere 20 requisitos sin duplicados')
    categoria = {}
    esfuerzo = {}
    for r in moscow:
        ident = r['id']
        if r['categoria'] not in PRIORIDAD or not r['justificacion'].strip():
            raise ValueError(f'MoSCoW inválido para {ident}')
        try:
            e = float(r['esfuerzo'])
        except ValueError:
            raise ValueError(f'Esfuerzo no numérico para {ident}')
        if not math.isfinite(e) or e <= 0:
            raise ValueError(f'Esfuerzo inválido para {ident}')
        categoria[ident] = r['categoria']
        esfuerzo[ident] = e
    esfuerzo_total = sum(esfuerzo.values())
    esfuerzo_must = sum(esfuerzo[k] for k in IDS if categoria[k] == 'Must')
    porcentaje = 100 * esfuerzo_must / esfuerzo_total
    if porcentaje > 60 + 1e-10:
        raise ValueError(f'Must supera 60 % de esfuerzo: {porcentaje:.4f} %')

    kano = cargar(DATOS/'kano_clasificacion.csv',
                  ['caracteristica','id_requisito','A','O','M','I','R','Q','categoria'])
    if len(kano) != 8 or {r['caracteristica'] for r in kano} != {f'K{i:02d}' for i in range(1,9)}:
        raise ValueError('Se requieren 8 clasificaciones Kano oficiales')
    kano_por_id = {}
    for fila in kano:
        if fila['id_requisito'] not in IDS or fila['categoria'] not in 'AOMIRQ':
            raise ValueError(f'Clasificación Kano inválida: {fila}')
        frecuencias = {x:int(fila[x]) for x in 'AOMIRQ'}
        if sum(frecuencias.values()) != 5 or any(x < 0 for x in frecuencias.values()):
            raise ValueError(f'Kano no contiene cinco respuestas: {fila}')
        if frecuencias[fila['categoria']] != max(frecuencias.values()):
            raise ValueError(f'Categoría Kano incompatible con las frecuencias: {fila}')
        kano_por_id[fila['id_requisito']] = fila['categoria']
    if len(kano_por_id) != 8:
        raise ValueError('Las ocho características Kano deben mapear a requisitos diferentes')

    rango_v = rangos_medios(totales,descendente=True)
    rango_m = rangos_medios({k:PRIORIDAD[categoria[k]] for k in IDS})
    rho = spearman(rango_m,rango_v)
    orden = sorted(IDS, key=lambda k:(-totales[k],k))
    SALIDA.mkdir(exist_ok=True)
    TABLAS.mkdir(exist_ok=True)
    guardar_csv(SALIDA/'orden_votacion.csv',['requisito_id','puntos_totales','rango_votacion'],[
        {'requisito_id':k,'puntos_totales':totales[k],'rango_votacion':rango_v[k]} for k in orden])
    guardar_csv(SALIDA/'orden_moscow.csv',['requisito_id','categoria','rango_moscow'],[
        {'requisito_id':k,'categoria':categoria[k],'rango_moscow':rango_m[k]} for k in IDS])
    guardar_csv(SALIDA/'comparacion.csv',['requisito_id','moscow','rango_moscow','votos','rango_votacion','kano'],[
        {'requisito_id':k,'moscow':categoria[k],'rango_moscow':rango_m[k],
         'votos':totales[k],'rango_votacion':rango_v[k],'kano':kano_por_id.get(k,'')} for k in IDS])
    resumen = {'participantes_votacion':{p:por_persona[p] for p in VOTANTES},
               'puntos_totales':sum(totales.values()),'n_requisitos':len(IDS),
               'n_caracteristicas_kano':len(kano),'esfuerzo_must':esfuerzo_must,
               'esfuerzo_total':esfuerzo_total,'porcentaje_must':porcentaje,
               'categorias_moscow':{c:sum(categoria[k]==c for k in IDS) for c in ('Must','Should','Could','Wont')},
               'spearman':rho}
    (SALIDA/'resumen.json').write_text(json.dumps(resumen,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    f = lambda x: str(x).replace('.',',')
    tabla('tabla_votacion.tex','Votación ponderada y rango medio', 'tab:resultados-votacion',
          ['ID','Requisito','Puntos','Rango'],[(k,nombres[k],totales[k],f(rango_v[k])) for k in orden],
          'p{0.13\\linewidth}p{0.53\\linewidth}rr')
    tabla('tabla_moscow_votacion.tex','Contraste entre MoSCoW y votación','tab:comparacion-moscow-votos',
          ['ID','MoSCoW','R. MoSCoW','Puntos','R. votos'],
          [(k,categoria[k],f(rango_m[k]),totales[k],f(rango_v[k])) for k in orden],
          'p{0.14\\linewidth}p{0.21\\linewidth}rrr')
    tabla('tabla_kano_votacion.tex','Características Kano frente a la votación', 'tab:comparacion-kano-votos',
          ['ID','Característica','Puntos','Rango','Kano'],
          [(r['id_requisito'],nombres[r['id_requisito']],totales[r['id_requisito']],
            f(rango_v[r['id_requisito']]),r['categoria']) for r in kano],
          'p{0.14\\linewidth}p{0.40\\linewidth}rrc')
    print(json.dumps(resumen,ensure_ascii=False,indent=2))
    return resumen


if __name__ == '__main__':
    calcular()
