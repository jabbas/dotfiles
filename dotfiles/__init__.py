# -*- coding: utf-8 -*-
# Author: Grzegorz Dziegielewski

# Example usage:
# dotfiles init

import os, sys
import confighelper

import logging
logger = logging.getLogger(__name__)

class NullHandler(logging.Handler):
    def emit(self, record):
        pass
logger.addHandler(NullHandler())

logging.basicConfig(
        format="[%(asctime)s] [%(levelname)-8s] %(name)s - %(message)s",
        level=logging.DEBUG
)

def makeDefaults(cfg):
    cfg.git_bin = 'git'
    cfg.git_dir = '~/.dotfiles'
    cfg.work_dir = '~/'

confighelper.makedefaults = makeDefaults
cfg = confighelper.get(__name__)

class Dotfiles(object):
    def __init__(self, cfg):
        object.__init__(self)
        self.git_bin = cfg.git_bin
        self.git_dir = os.path.expanduser(cfg.git_dir)
        self.work_dir = os.path.expanduser(cfg.work_dir)

        self.prepare_env()
        self.prepare_config()

    def setenv(self, key, value):
        if not os.getenv(key):
            os.putenv(key, value)

    def prepare_env(self):
        logger.debug("Setting GIT_DIR to '%s'" % self.git_dir)
        self.setenv('GIT_DIR', self.git_dir)
        logger.debug("Setting GIT_WORK_TREE to '%s'" % self.work_dir)
        self.setenv('GIT_WORK_TREE', self.work_dir)

    def prepare_config(self):
        # TODO it should be only launched if necessary
        logger.debug("Preparing config")
        self.launch('config', '--local', '--add status.showuntrackedfiles no')

    def launch(self, *argv):
        if not argv:
            argv=sys.argv[1:]

        cmd = "%s %s" % (self.git_bin, " ".join(argv))
        logger.debug("Launching '%s'" % cmd)
        os.system(cmd)


df = Dotfiles(cfg)
df.launch()
