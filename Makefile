all: preview

preview:
	quarto preview

pdf:
	quarto render --to pdf

clean:
	rm -f *.tex *.html *.log *.aux

cleanall: clean
	rm -rf rangen_files intro_files index_files
