%.html : %.jinja2 templates/header.jinja2 templates/footer.jinja2
	python3 to_html.py --input $< --output $@

all: index.html links.html presentations.html publications.html

clean:
	rm -f *.html *~ .*~
	find . -name "*.html" -exec rm -f {} \;
	find . -name "*~" -exec rm -f {} \;
	find . -name ".*~" -exec rm -f {} \;

list := $(shell find . -name "*.html" -or -name "[a-z]*.png" -or -name "*.py") 
tar:
	find . -name "*.html" -exec chmod 604 {} \;
	find . -name "*.py" -exec chmod 700 {} \;
	tar --exclude=*.tgz --exclude=to_html.py -czf tm.tgz css js $(list)
	
.PHONY: all clean
