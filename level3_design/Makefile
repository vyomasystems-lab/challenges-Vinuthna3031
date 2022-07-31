# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

VERILOG_SOURCES = $(PWD)/16bit_multiplier.v              # provide your design path

TOPLEVEL :=16bit_multiplier.v           # design file
MODULE   :=test_16bit_multiplier.py    # test file

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 
