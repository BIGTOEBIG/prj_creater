import os
import string
import logging
import _env

import yaml
from pprint import pformat

CFG_FILE = os.path.realpath("prj_cfg.yaml")
TCL_DIR = os.path.realpath("tcl")
pin_plan_tcl_pattern_file = os.path.join(TCL_DIR, "pinplan.tcl")

formatter = logging.Formatter("%(name)s-%(levelname)s: %(message)s")
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
s_hdlr = logging.StreamHandler()
s_hdlr.setFormatter(formatter)
s_hdlr.setLevel(logging.INFO)
logger.addHandler(s_hdlr)

class Launcher:

    def __init__(self):
        with open(CFG_FILE, 'r') as fh:
            cfg = yaml.load(fh, Loader=yaml.FullLoader)
            cfg_str = pformat(cfg)
            print(cfg_str)
        self.cfg = cfg
        self.tcl_template_file = pin_plan_tcl_pattern_file
        with open(self.tcl_template_file, 'r') as fh:
            tcl_template = fh.read()
            tcl_content = string.Template(tcl_template).substitute(self.cfg)
            message = "\n".join([
                "Generated tcl content is >>>",
                "~" * 80,
                tcl_content,
                "~" * 80,
            ])
            logger.info(message.replace("\n", "\n\t|"))


if __name__ == "__main__":

    launcher = Launcher()
