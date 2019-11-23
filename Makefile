PREFIX = /usr

all:

install:
	mkdir -p $(DESTDIR)$(PREFIX)/share/icons
	cp -r neru-*-classic/ $(DESTDIR)$(PREFIX)/share/icons/

uninstall:
	$(RM) -r $(DESTDIR)$(PREFIX)/share/icons/neru-*-classic

post-install:
	@find $(DESTDIR)$(PREFIX)/share/icons -type d -name 'neru-*-classic' -exec gtk-update-icon-cache -qf {} \;

.PHONY: all install uninstall post-install
