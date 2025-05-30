This Repo is for learning how to step up, run calculation and analysis the results.

# User Input

The user generally provide two input files:
- `conifg.yaml`
- `components.yaml`

The configuartion file describe global parameters such as 
- `box dimension`
- `temperature`
- `pH`

The component file defines
- type of molecules
- number of molecules
- molecule-specific properties

If there are some properties shared by all molecules, we can use a default section in the `components.yaml`