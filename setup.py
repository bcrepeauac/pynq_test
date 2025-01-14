from setuptools import setup, find_packages
#import neo_pynq
from distutils.dir_util import copy_tree
import os
import shutil

# global variables
board = os.environ['BOARD']
repo_board_folder = f'boards/{board}/pynq_test'
board_notebooks_dir = os.environ['PYNQ_JUPYTER_NOTEBOOKS']
hw_data_files = []
ovl_dest = 'pynq_test'


# check whether board is supported
def check_env():
    if not os.path.isdir(repo_board_folder):
        raise ValueError("Board {} is not supported.".format(board))
    if not os.path.isdir(board_notebooks_dir):
        raise ValueError("Directory {} does not exist.".format(board_notebooks_dir))


# copy overlays to python package
def copy_overlays():
    src_ol_dir = os.path.join(repo_board_folder, 'bitstream')
    dst_ol_dir = os.path.join(ovl_dest, 'bitstream')
    copy_tree(src_ol_dir, dst_ol_dir)
    hw_data_files.extend([os.path.join("..", dst_ol_dir, f) for f in os.listdir(dst_ol_dir)])
    print(f'Source: {src_ol_dir}')
    print(f'Destination: {dst_ol_dir}')


# copy notebooks to jupyter home
def copy_notebooks():
    src_nb_dir = os.path.join(repo_board_folder, 'notebook')
    dst_nb_dir = os.path.join(board_notebooks_dir, 'pynq_test')
    if os.path.exists(dst_nb_dir):
        shutil.rmtree(dst_nb_dir)
    copy_tree(src_nb_dir, dst_nb_dir)


check_env()
copy_overlays()
copy_notebooks()

setup(
	name= "pynq_test",
	version= "1.36",
	url= 'https://github.com/bcrepeauac/pynq_test.git',
	license = 'Apache Software License',
	author= "Brian Crepeau",
	author_email= "bcrepeau@amherst.edu",
	packages= find_packages(),
	package_data= {
	 '': hw_data_files,
	},
	description= "Test overlay for PYNQ Z1",
)
