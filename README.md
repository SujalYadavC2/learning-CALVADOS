To run simulation I need to files `config.yaml` and `components.yaml`. I do not have to create these files manually, I can use `Config` and `Components` class from `calvados.cfg` package. I can load these classes like this:

```python
from calvados.cfg import Config, Components
```

I can define parameters that I need when I initialize these classes and the other parameters calvados will load their default value.

**Default Values**

`config.yaml`

```yaml
---
sysname : 'default_simulation'
topol : 'center'

fixed_lambda: 0
eps_lj : 0.2
cutoff_lj : 2.0
cutoff_yu : 4.0

steps : 100000000
wfreq : 100000
platform : 'CPU'
threads : 1
runtime : 0
restart : 'checkpoint'
frestart : 'restart.chk'
verbose : false

slab_eq : false
bilayer_eq : false
pressure_coupling : false
box_eq : false
pressure : [0,0,0]
boxscaling_xyz : [true,true,true]
k_eq : 0.02
steps_eq : 1000
ext_force : false
ext_force_expr : 'step(d2-18)*d2; d2=periodicdistance(x, y, z, 0, 0, z)^2'

friction_coeff: 0.01 
slab_width : 100
slab_outer : 40
random_number_seed : null
report_potential_energy : false
logfreq : 1000000
gpu_id: 0

custom_restraints : false
custom_restraint_type : 'harmonic'
fcustom_restraints : 'custom_restraints.txt'
```

`components.yaml`

```yaml
---
molecule_type : 'protein'
nmol : 1
charge_termini : 'both'
alpha: 0
ffasta : 'fastabib.fasta'
kb : 8033.0

ext_restraint : true
restraint : false
cutoff_restr : 0.9
pdb_folder : 'pdbs'
restraint_type : 'harmonic'
k_harmonic : 700.
fdomains : 'domains.yaml'
k_go : 10.
use_com : true
periodic: false

colabfold : 0
bfac_shift : 0.8
bfac_width : 50.
pae_shift : 0.4
pae_width : 8.

rna_kb1 : 8033.0
rna_kb2 : 8033.0
rna_ka : 7.24
rna_pa : 3.14
rna_nb_sigma : 0.4
rna_nb_scale : 15
rna_nb_cutoff : 0.6

n_ends : 1

ptm_name : 'example_ptm'
ptm_locations : []
```

In the manual it is written that as a minimum we need to input only the sequence, number and types on molecules, simulation box dimensions, and solution conditions.

But they do not say the parameters that is necessary to define to run simulation. For example for my first simulation I did not add `ionic` parameter in my `config.yaml`. This leads to an error. 

**Q. What paramerters are need to run simulation?**

To add the sequence of a protein we use `fasta` file. It can have more than one protein sequence.

for my simulation I just used one protein in the file.

**Q. How calvados know which protein to take?**

_Ans:_ What I think it gets estabished when we add protein.

```python
components.add(name='A1SLCD')
```

I changed the name in the add method to `FUSRGG3` and I did not had its sequence in the `fasta` file and I got an error when I tried to run simulation.

**Now I will look at the MDAnalysis packgae.**