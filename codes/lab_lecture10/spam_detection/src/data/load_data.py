import yaml
import argparse
import pandas as pd


def read_params(config_path):
    """
    read parameters from the params.yaml file
    input: params.yaml location
    output: parameters as dictionary
    """
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


def load_data(data_path, model_var):
    """
    load csv dataset from given path
    input: csv path
    output:pandas dataframe
    """
    df = pd.read_table(data_path, header=None, names=model_var)
    return df


def load_raw_data(config_path):
    """
    load data from external location(data/external) to the raw folder(data/raw) with train and teting dataset
    input: config_path
    output: save train file in data/raw folder
    """
    config = read_params(config_path)
    external_data_path = config["external_data_config"]["external_data_csv"]
    raw_data_path = config["raw_data_config"]["raw_data_csv"]
    model_var = config["raw_data_config"]["model_var"]
    text  = config["raw_data_config"]["text"]
    target = config["raw_data_config"]["target"]
    label_encoding = config["raw_data_config"]["label_encoding"]

    df = load_data(external_data_path, model_var)
    df[text] = df[text].replace(',', " ")
    df[target] = df[target].map(label_encoding)
    df.to_csv(raw_data_path, index=False)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    load_raw_data(config_path=parsed_args.config)