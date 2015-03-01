CPP_FILE=acidTests.cpp
PY_FILE=acidTests.py
CPP_OUT=acidTests.out

test: ${CPP_FILE} ${PY_FILE}
	@python ${PY_FILE}
	@g++ -o ${CPP_OUT} ${CPP_FILE}
	@./${CPP_OUT}

clean:
	-rm ${PY_FILE}c ${CPP_OUT}