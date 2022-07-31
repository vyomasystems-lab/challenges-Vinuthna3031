# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

VERILOG_SOURCES = $(PWD)/multiplier_16bit_buggy.v              # provide your design path

TOPLEVEL :=multiplier_16bit_buggy          # design file
MODULE   :=test_16bit_multiplier    # test file

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 
