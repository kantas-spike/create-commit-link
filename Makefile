DST_DIR=${HOME}/bin

install: create-commit-link.py
	mkdir -p ${DST_DIR}
	cp $< ${DST_DIR}
	chmod u+x ${DST_DIR}/$<
