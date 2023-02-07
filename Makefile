filename = mono

## Generate and retrieve data
data : src/make_data.sh $(wildcard src/utils/data/*)
	sh src/make_data.sh

## Generate and retrieve figures
figures : src/make_figures.sh $(wildcard src/visual/*)
	sh src/make_figures.sh

## Compile producing only pdf file
compile : data figures $(wildcard text/*) $(wildcard figures/*)
	#TODO: see if make glossaries and index, reuse clean stage
	export BSTINPUTS=text
	pdflatex -output-directory=text text/$(filename).tex
	bibtex text/$(filename)
	# makeglossaries text/$(filename)
	# gmakeindex text/$(filename)
	pdflatex -output-directory=text text/$(filename).tex
	pdflatex -output-directory=text text/$(filename).tex
	@rm -f text/*.out text/*.aux text/*.alg text/*.acr text/*.dvi text/*.gls text/*.log text/*.bbl text/*.blg text/*.ntn text/*.not text/*.lof text/*.lot text/*.toc text/*.loa text/*.lsg text/*.nlo text/*.nls text/*.ilg text/*.ind text/*.ist text/*.glg text/*.glo text/*.xdy text/*.acn text/*.idx text/*.loq text/*.lol text/*~
	@rm -f
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	find . -name ".mypy_cache" -type d  -exec rm -r "{}" \;


.PHONY: clean
## Clean unnecessary files
clean :
	@rm -f text/*.out text/*.aux text/*.alg text/*.acr text/*.dvi text/*.gls text/*.log text/*.bbl text/*.blg text/*.ntn text/*.not text/*.lof text/*.lot text/*.toc text/*.loa text/*.lsg text/*.nlo text/*.nls text/*.ilg text/*.ind text/*.ist text/*.glg text/*.glo text/*.xdy text/*.acn text/*.idx text/*.loq text/*.lol text/*~
	@rm -f
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	find . -name ".mypy_cache" -type d  -exec rm -r "{}" \;

.PHONY: help
help :
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')
