# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

VERILOG_SOURCES = $(PWD)/buggy_multiplier_16bit.v              # provide your design path

TOPLEVEL :=buggy_multiplier_16bit          # design file
MODULE   :=test_16bit_multiplier    # test file

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 
