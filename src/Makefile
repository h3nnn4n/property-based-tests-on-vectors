CC=clang
override CFLAGS+=-dynamiclib -undefined dynamic_lookup

SOURCES=vector.c

DYLIB=vector.dylib

OBJECTS=$(SOURCES:.c=.o)

all: $(SOURCES) $(DYLIB)

$(DYLIB): $(OBJECTS)
	$(CC) $(CFLAGS) $(OBJECTS) -o $@

.c.o:
	$(CC) $(CFLAGS) $< -c -o $@

.PHONY: clean
clean:
	$(RM) $(OBJECTS) $(DYLIB)