LANG = python
APP = run.py

run:
	@$(LANG) $(APP) 

clean:
	@find . -name "*.pyc" -exec rm -f '{}' +
	@find . -name "*~" -exec rm -f '{}' +
	@echo "Done!"
