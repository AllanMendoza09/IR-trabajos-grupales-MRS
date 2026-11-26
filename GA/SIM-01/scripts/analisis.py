#!/usr/bin/env python3
"""Validación y análisis reproducible; no genera datos de participantes."""
import argparse
import csv
import json
import math
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'datos'
OUTPUT = DATA / 'calculos'
OPTIONS = ('Me gusta', 'Lo espero', 'Indiferente', 'Lo tolero', 'No me gusta')
GROUP_ORDER = {'Must': 0, 'Should': 1, 'Could': 2, 'Wont': 3}
KANO_TABLE = (
    ('Q','A','A','A','O'),
    ('R','I','I','I','M'),
    ('R','I','I','I','M'),
    ('R','I','I','I','M'),
    ('R','R','R','R','Q'),
)
KANO_TIEBREAK = {'M':0,'O':1,'A':2,'I':3,'R':4,'Q':5}
SCHEMAS = {
    'requisitos.csv': ['id','tipo','nombre','texto','verificacion'],
    'moscow.csv': ['requisito_id','prioridad','esfuerzo','justificacion'],
    'caracteristicas_kano.csv': ['caracteristica_id','requisito_id','caracteristica'],
    'instrumento_kano.csv': ['caracteristica_id','tipo_pregunta','pregunta','opciones'],
    'respuestas_kano.csv': ['participante_id','caracteristica_id','funcional','disfuncional'],
    'votos.csv': ['participante_id','requisito_id','puntos'],
    'decision.csv': ['requisito_id','decision','orden_final','justificacion'],
}

class DataError(ValueError):
    pass

def require(condition, explanation):
    if not condition:
        raise DataError(explanation)

def read_csv(name, root=DATA):
    path = root / name
    require(path.is_file(), f'Falta {path}')
    with path.open('r', encoding='utf-8-sig', newline='') as f:
        rd = csv.DictReader(f)
        require(rd.fieldnames == SCHEMAS[name],
                f'Encabezados incorrectos en {name}: {rd.fieldnames!r}')
        records = list(rd)
        require(all(None not in row for row in records),
                f'{name} tiene más columnas de las declaradas')
        return records

def validate_structure(root=DATA):
    data = {name:read_csv(name,root) for name in SCHEMAS}
    reqs=data['requisitos.csv']
    ids=[x['id'] for x in reqs]
    required=[f'RF-{i:02d}' for i in range(1,13)] + [f'RNF-{i:02d}' for i in range(1,9)]
    require(len(reqs)==20 and set(ids)==set(required) and len(ids)==len(set(ids)),
            'El catálogo debe contener exactamente RF-01..RF-12 y RNF-01..RNF-08')
    for row in reqs:
        require(row['tipo']==('RF' if row['id'].startswith('RF-') else 'RNF'),
                f'Tipo incoherente: {row["id"]}')
        require(all(row[k].strip() for k in ['nombre','texto','verificacion']),
                f'Requisito incompleto: {row["id"]}')
        require(row['texto'].startswith('El sistema deberá '),
                f'Falta verbo modal en {row["id"]}')
        require(' cuando ' in row['texto'] and ', con el fin de ' in row['texto'],
                f'Faltan condición o propósito en {row["id"]}')
    features=data['caracteristicas_kano.csv']
    codes=[k['caracteristica_id'] for k in features]
    require(len(features)==8 and set(codes)=={f'K{i:02d}' for i in range(1,9)},
            'Se requieren K01..K08')
    linked=[k['requisito_id'] for k in features]
    require(len(set(linked))==8 and set(linked).issubset(ids),
            'Cada característica Kano debe apuntar a un requisito distinto')
    instr=data['instrumento_kano.csv']
    require(len(instr)==16 and {(r['caracteristica_id'],r['tipo_pregunta']) for r in instr} ==
            {(k,t) for k in codes for t in ('funcional','disfuncional')},
            'El instrumento necesita las 16 preguntas, funcional y disfuncional')
    require(all(x['pregunta'].strip() and x['opciones'].strip() for x in instr),
            'Existen preguntas Kano sin contenido')
    return data

def float_positive(x, field):
    try: n=float(x)
    except ValueError: raise DataError(f'Valor numérico inválido en {field}: {x}')
    require(math.isfinite(n) and n>0, f'{field} debe ser positivo y finito')
    return n

def check_moscow(records,ids):
    require(len(records)==20,'MoSCoW requiere 20 filas reales')
    require(len({r['requisito_id'] for r in records})==20 and
            {r['requisito_id'] for r in records}==set(ids),
            'MoSCoW no cubre 20 requisitos distintos')
    efforts={}
    for r in records:
        require(r['prioridad'] in GROUP_ORDER,f'Categoría MoSCoW inválida: {r}')
        require(r['justificacion'].strip(),f'Falta justificación en {r["requisito_id"]}')
        efforts[r['requisito_id']]=float_positive(r['esfuerzo'],r['requisito_id'])
    total=sum(efforts.values())
    must=sum(efforts[r['requisito_id']] for r in records if r['prioridad']=='Must')
    share=must/total
    require(share<=0.6+1e-12,
            f'El esfuerzo Must supera 60 %: {share*100:.2f} %')
    return share

def check_kano(records,codes):
    participants={r['participante_id'] for r in records}
    require(participants=={f'P{i:02d}' for i in range(1,6)},
            'Se requieren P01..P05, cinco personas distintas de Kano')
    require(len(records)==40,'Se requieren 8 respuestas dobles por cada participante Kano')
    keys=[(r['participante_id'],r['caracteristica_id']) for r in records]
    require(len(keys)==len(set(keys)),'Respuestas Kano duplicadas')
    require(set(keys)=={(p,k) for p in participants for k in codes},
            'Falta una respuesta doble Kano para algún participante o característica')
    groups=defaultdict(list)
    for r in records:
        f,d=r['funcional'],r['disfuncional']
        require(f in OPTIONS and d in OPTIONS,
                f'Opción Kano inválida en {r["participante_id"]}/{r["caracteristica_id"]}')
        groups[r['caracteristica_id']].append(KANO_TABLE[OPTIONS.index(f)][OPTIONS.index(d)])
    out=[]
    for k in sorted(codes):
        hist=Counter(groups[k]); count=max(hist.values()); tied=[x for x,n in hist.items() if n==count]
        dominant=sorted(tied,key=lambda x:KANO_TIEBREAK[x])[0]
        out.append({'caracteristica_id':k,'categoria':dominant,
                    'empate': 'Si' if len(tied)>1 else 'No',
                    **{c:hist.get(c,0) for c in 'AOMIRQ'}})
    return out

def check_votes(records,ids):
    parts={r['participante_id'] for r in records}
    require(parts=={'P06','P07','P08'},'Se requieren P06..P08, distintos de Kano')
    require(len(records)==60,'Se requieren 20 asignaciones por cada votante')
    keys=[(r['participante_id'],r['requisito_id']) for r in records]
    require(len(keys)==len(set(keys)), 'Hay duplicaciones en la votación')
    require(set(keys)=={(p,id) for p in parts for id in ids},
            'Cada votante debe asignar puntos a los 20 requisitos')
    sums=defaultdict(int); totals=defaultdict(int)
    for r in records:
        val=r['puntos']
        require(val.isdigit(),f'Puntuación no entera: {r}')
        pts=int(val)
        sums[r['participante_id']]+=pts
        totals[r['requisito_id']]+=pts
    require(all(sums[p]==100 for p in parts),f'Cada votante debe sumar 100: {dict(sums)}')
    require(sum(totals.values())==300,'Los votos deben totalizar 300')
    return totals

def average_ranks(ids,metrics,ascending=True):
    ordered=sorted(ids,key=lambda x:((metrics[x] if ascending else -metrics[x]),x))
    out={}; pos=0
    while pos<len(ordered):
        end=pos+1
        while end<len(ordered) and metrics[ordered[end]]==metrics[ordered[pos]]:
            end+=1
        rank=((pos+1)+end)/2.0
        for k in ordered[pos:end]: out[k]=rank
        pos=end
    return out

def spearman(r1,r2,ids):
    a=[r1[k] for k in ids]; b=[r2[k] for k in ids]
    am=sum(a)/len(a); bm=sum(b)/len(b)
    num=sum((x-am)*(y-bm) for x,y in zip(a,b))
    denom=math.sqrt(sum((x-am)**2 for x in a)*sum((y-bm)**2 for y in b))
    return num/denom if denom else None

def write_csv(path,fields,rows):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('w',newline='',encoding='utf-8') as fh:
        w=csv.DictWriter(fh,fieldnames=fields,lineterminator='\n'); w.writeheader();w.writerows(rows)

def process(root=DATA,output=OUTPUT):
    data=validate_structure(root)
    ids=sorted([r['id'] for r in data['requisitos.csv']])
    must_share=check_moscow(data['moscow.csv'],ids)
    kscore=check_kano(data['respuestas_kano.csv'],
                      [f['caracteristica_id'] for f in data['caracteristicas_kano.csv']])
    votes=check_votes(data['votos.csv'],ids)
    priorities={r['requisito_id']:r['prioridad'] for r in data['moscow.csv']}
    scores={x:GROUP_ORDER[priorities[x]] for x in ids}
    mr=average_ranks(ids,scores,True)
    vr=average_ranks(ids,votes,False)
    rho=spearman(mr,vr,ids)
    kmapping={r['caracteristica_id']:r['requisito_id'] for r in data['caracteristicas_kano.csv']}
    kano={kmapping[r['caracteristica_id']]:r for r in kscore}
    mo=[{'requisito_id':k,'prioridad':priorities[k],'rango_moscow':mr[k]} for k in sorted(ids,key=lambda x:(mr[x],x))]
    vo=[{'requisito_id':k,'puntos_totales':votes[k],'rango_votacion':vr[k]} for k in sorted(ids,key=lambda x:(vr[x],x))]
    kr=[{'caracteristica_id':r['caracteristica_id'],'requisito_id':kmapping[r['caracteristica_id']],
         'categoria':r['categoria'],'empate':r['empate'],
         **{c:r[c] for c in 'AOMIRQ'}} for r in kscore]
    both=[{'requisito_id':k,'moscow':priorities[k], 'rango_moscow':mr[k],
           'votos':votes[k],'rango_votacion':vr[k],
           'kano':kano[k]['categoria'] if k in kano else ''} for k in sorted(ids)]
    # No output is created until every participant dataset passes its checks.
    write_csv(output/'orden_moscow.csv',list(mo[0]),mo)
    write_csv(output/'orden_votacion.csv',list(vo[0]),vo)
    write_csv(output/'orden_kano.csv',list(kr[0]),kr)
    write_csv(output/'comparacion.csv',list(both[0]),both)
    summary={'requisitos':len(ids),'rf':12,'rnf':8,'participantes_kano':5,
             'participantes_votacion':3,'caracteristicas_kano':8,
             'puntos_por_votante':100,'proporcion_esfuerzo_must':round(must_share,6),
             'spearman_moscow_votacion':round(rho,8) if rho is not None else None,
             'metodo_rangos':'Promedio de posiciones empatadas; Spearman = Pearson sobre rangos',
             'limitacion_kano':'8 características; categoría ausente para los otros 12 requisitos',
             'clasificacion_kano':'En empates de máxima frecuencia: M > O > A > I > R > Q'}
    (output/'resumen.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return summary

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    group=ap.add_mutually_exclusive_group(required=True)
    group.add_argument('--verificar',action='store_true',help='Valida estructura e instrumentos sin exigir encuestas')
    group.add_argument('--procesar',action='store_true',help='Exige datos reales y calcula los tres órdenes')
    args=ap.parse_args()
    try:
        data=validate_structure()
        if args.verificar:
            print('ESTRUCTURA VÁLIDA: 20 requisitos (12 RF + 8 RNF), 8 características y 16 preguntas Kano.')
            print('Registros reales Kano:',len(data['respuestas_kano.csv']),
                  '| votación:',len(data['votos.csv']),
                  '| MoSCoW:',len(data['moscow.csv']))
            print('Esta comprobación no valida participación ni resultados de campo.')
        else:
            print(json.dumps(process(),ensure_ascii=False,indent=2))
    except DataError as e:
        ap.exit(2, f'VALIDACIÓN RECHAZADA: {e}\n')

if __name__=='__main__':
    main()
