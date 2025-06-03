import os
from calvados.cfg import Config, Components

cwd = os.getcwd()
sysname = 'sim'

config = Config(
    sysname = sysname,
    box = [50,50,50], #nm
    temp = 273,
    pH = 7.5,
    ionic = 0.19,

    wfreq = 1000,
    steps = 1010*1000,
    verbose = True,
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