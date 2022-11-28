import click
import pandas as pd
import importlib.util
import importlib
import sys

def validate_parameter(ctx, param, value):
    parameters = {}
    for p in value:
        kv = p.split("=")
        if len(kv)!=2:
            raise click.BadParameter("Format must be <key>=<value>")
        parameters[kv[0]]=kv[1]
    return parameters

@click.command()
@click.option("-l", "--live", "liveDataset", type=click.Path(exists=True), required=True, help="Path to csv file containing live dataset", prompt=True)
@click.option("-h", "--historical", "historicalDataset", type=click.Path(exists=True), required=True, help="Path to csv file containing historical dataset", prompt=True)
@click.option("-d", "--detector", "detectorPath", type=click.Path(exists=True), default="detector.py", show_default=True, help= "Path to python script containing the detector function", prompt=True)
@click.option("-p", "--parameter", "parameters", multiple=True, callback=validate_parameter)
def cli(liveDataset, historicalDataset, detectorPath, parameters):
    #Import detector module 
    spec = importlib.util.spec_from_file_location("detector", location = detectorPath)
    detectorMod = importlib.util.module_from_spec(spec)
    sys.modules["detector"] = detectorMod
    spec.loader.exec_module(detectorMod)
    
    #Load datasets
    liveDataset = pd.read_csv(liveDataset)
    historicalDataset = pd.read_csv(historicalDataset)

    #Execute detector
    level, raw = detectorMod.detector(liveDataset, historicalDataset, parameters)
    print("level: ", level)
    print("raw value: ", raw)
