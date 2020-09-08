from pathlib import Path
import yaml

META_NODES_FILE = Path(__file__).parent / "data-dict-meta-nodes.yml"
META_RELS_FILE = Path(__file__).parent / "data-dict-meta-rels.yml"

with META_NODES_FILE.open("r") as f:
    meta_nodes_dict = yaml.safe_load(f)

with META_RELS_FILE.open("r") as f:
    meta_rels_dict = yaml.safe_load(f)
