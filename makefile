build: src/hack.tal
	mkdir -p bin
	drifblim src/hack.tal bin/hack.rom

run: bin/hack.rom
	uxnemu bin/hack.rom

test: build
	zsh -c "time uxnemu bin/hack.rom"

clean:
	rm -rf bin
