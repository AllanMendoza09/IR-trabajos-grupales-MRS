#!/usr/bin/env python3
"""Pruebas con datos sintéticos en directorio temporal; no se guardan en el repositorio."""
import csv
import json
import tempfile
from pathlib import Path
from shutil import copy2
from analisis import SCHEMAS, validate_structure, process, DataError, spearman, average_ranks


def write_csv(path,header,rows):
    with path.open('w',encoding='utf-8',newline='') as f:
        w=csv.writer(f,lineterminator='\n'); w.writerow(header); w.writerows(rows)


def test():
    origin=Path(__file__).resolve().parents[1]/'datos'
    with tempfile.TemporaryDirectory(prefix='sim01_sintetico_') as raw:
        root=Path(raw)
        for f in SCHEMAS:
            copy2(origin/f,root/f)
        ids=[f'RF-{i:02d}' for i in range(1,13)]+[f'RNF-{i:02d}' for i in range(1,9)]
        # Valores sintéticos exclusivos del ensayo automático, no respuestas reales.
        priorities=['Must']*6+['Should']*8+['Could']*4+['Wont']*2
        write_csv(root/'moscow.csv',SCHEMAS['moscow.csv'],
                  [(id,priorities[n],1,'Justificación sintética de ensayo') for n,id in enumerate(ids)])
        k=[f'K{i:02d}' for i in range(1,9)]
        response=[]
        for p in [f'P{i:02d}' for i in range(1,6)]:
            for feature in k:
                response.append((p,feature,'Me gusta','No me gusta'))
        write_csv(root/'respuestas_kano.csv',SCHEMAS['respuestas_kano.csv'],response)
        votes=[]
        for part in ['P06','P07','P08']:
            for n,id in enumerate(ids):
                votes.append((part,id,100 if n==0 else 0))
        write_csv(root/'votos.csv',SCHEMAS['votos.csv'],votes)
        results=process(root,root/'outputs')
        assert results['requisitos']==20 and results['participantes_kano']==5
        assert (root/'outputs'/'comparacion.csv').exists()
        assert len(list(csv.DictReader((root/'outputs'/'orden_kano.csv').open(encoding='utf-8'))))==8
        assert results['proporcion_esfuerzo_must']==0.3
        # Check average tie ranks explicitly.
        ranks=average_ranks(['a','b','c'],{'a':9,'b':9,'c':1},False)
        assert ranks == {'a':1.5,'b':1.5,'c':3.0}
        assert abs(spearman({'a':1,'b':2,'c':3},{'a':1,'b':2,'c':3},['a','b','c'])-1)<1e-12
        # The project must reject invalid allocations and not write outputs.
        invalid=root/'votos.csv'
        invalid.write_text(invalid.read_text(encoding='utf-8').replace(',100\n',',99\n',1),encoding='utf-8')
        try:
            process(root,root/'outputs_bad')
        except DataError:
            assert not (root/'outputs_bad').exists()
        else:
            raise AssertionError('Se admitió una asignación de 99 puntos')
    print('AUTOPRUEBA APROBADA (datos sintéticos en memoria/directorio temporal y eliminados).')

if __name__=='__main__':
    test()
