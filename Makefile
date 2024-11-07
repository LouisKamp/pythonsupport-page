# Minimal makefile for Sphinx documentation
#
.PHONY: default
default: all

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = docs
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: all
all: clean html

LINKCHECKDIR  = build/linkcheck

.PHONY: spelling spell
spell: spelling
spelling:
	$(SPHINXBUILD) -b spelling "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)


.PHONY: checklinks linkcheck
checklinks: linkcheck
linkcheck:
	$(SPHINXBUILD) -b linkcheck "$(SOURCEDIR)" "$(LINKCHECKDIR)" $(SPHINXOPTS) $(O)
	@echo
	@echo "Check finished. Report is in $(LINKCHECKDIR)."

.PHONY: rendergifs
rendergifs:
	@cd ./docs/os/gifs && bash create.sh