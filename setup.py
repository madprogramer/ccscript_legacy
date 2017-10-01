#!/usr/bin/env/python

import os
import platform

from setuptools import setup
from setuptools.extension import Extension

source_files = [os.path.join("src", x) for x in os.listdir("src") if x.lower().endswith(".cpp")]

extra_compile_args = []
extra_link_args = []

if platform.system() == "Linux" or platform.system() == "Darwin":
      extra_compile_args = ["-std=c++1z"]
      extra_link_args = ["-lstdc++fs"]
      #print ("Args Fixed")
#print ("{} is the current system on this device".format( platform.system()) )
#print ("Setup is almost underway..." )
setup(name="ccscript",
      version="1.338",
      description="ccscript",
      url="http://starmen.net/pkhack/ccscript",
      print ("""We've got trouble:
      Source Files:{},
      extra_compile_args:{},
      extra_link_args:{}
      """.format(source_files,extra_compile_args,extra_link_args) )
      ext_modules=[
          Extension("ccscript",
                    source_files,
                    language="c++",
                    extra_compile_args=extra_compile_args,
                    extra_link_args=extra_link_args
                    )
      ])
