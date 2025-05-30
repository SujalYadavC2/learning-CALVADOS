from calvados import sim
from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('--path',nargs='?', default='.', const='.', type=str)
    parser.add_argument('--config',nargs='?', default='config.yaml', const='config.yaml', type=str)
    parser.add_argument('--components',nargs='?', default='components.yaml', const='components.yaml', type=str)

    args = parser.parse_args()

    path = args.path
    fconfig = args.config
    fcomponents = args.components

    sim.run(path=path,fconfig=fconfig,fcomponents=fcomponents)


from calvados.analysis import save_conf_prop

save_conf_prop(path="/home/sujaly/Desktop/github/learning-CALVAODS/Single-chain_IDR_simulations/A1-LCDstar/A1SLCD",name="A1SLCD",residues_file="/home/sujaly/Desktop/github/learning-CALVAODS/Single-chain_IDR_simulations/A1-LCDstar/input/residues_CALVADOS2.csv",output_path="data",start=10,is_idr=True,select='all')
