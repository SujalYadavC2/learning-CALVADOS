import os
from calvados.cfg import Config, Components

cwd = os.getcwd()
sysname = 'A1SLCD'

config = Config(
    sysname = sysname,
    box = [50,50,50], #nm
    temp = 273,
    pH = 7.5,
    ionic = 0.19,

    wfreq = 100,
    steps  = 1010*100   
)

path = f'{cwd}/{sysname}'

config.write(path, 'config.yaml')

components = Components(
    molecule_type = 'protein',
    nmol=1,
    charge_termini='both',
    fresidues = f'{cwd}/input/residues_CALVADOS2.csv',
    ffasta = f'{cwd}/input/idr.fasta',
)

components.add(name='A1SLCD')

components.write(path,'components.yaml')