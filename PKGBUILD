# Maintainer: basigur

pkgname=neru-icon-classic-theme-git
_pkgname=neru-icon-classic-theme
pkgver=2.7
pkgrel=1
pkgdesc="Classic theme icons Neru"
arch=('any')
url="https://github.com/basigur/neru-icon-classic-theme"
license=('LGPL3')
depends=('gtk-update-icon-cache' 'librsvg' 'hicolor-icon-theme')
replaces=('neru-icon-classic-theme-git')
conflicts=('neru-icon-classic-theme')
source=("${_pkgname}::git+https://github.com/basigur/${_pkgname}")
sha512sums=('SKIP')


prepare() {
	cd "${_pkgname}"
	gtk-update-icon-cache neru-classic-light
	gtk-update-icon-cache neru-classic-dark
	gtk-update-icon-cache neru-classic-light-green
	gtk-update-icon-cache neru-classic-dark-green
	gtk-update-icon-cache neru-classic-light-yellow
	gtk-update-icon-cache neru-classic-dark-yellow
	gtk-update-icon-cache neru-classic-light-gray
	gtk-update-icon-cache neru-classic-dark-gray
	gtk-update-icon-cache neru-classic-light-red
	gtk-update-icon-cache neru-classic-dark-red
	gtk-update-icon-cache neru-classic-light-magenta
	gtk-update-icon-cache neru-classic-dark-magenta
	gtk-update-icon-cache neru-classic-light-black
	gtk-update-icon-cache neru-classic-dark-black
	gtk-update-icon-cache neru-classic-light-brown
	gtk-update-icon-cache neru-classic-dark-brown
	gtk-update-icon-cache neru-classic-light-cyan
	gtk-update-icon-cache neru-classic-dark-cyan
	gtk-update-icon-cache neru-classic-light-orange
	gtk-update-icon-cache neru-classic-dark-orange
	gtk-update-icon-cache neru-classic-light-pink
	gtk-update-icon-cache neru-classic-dark-pink

}


pkgver() {
  cd "${_pkgname}"
  echo "2.7~r$(git rev-list --count HEAD).$(git rev-parse --short HEAD)"

}


package() {
	cd "${_pkgname}"
	install -d "$pkgdir/usr/share/icons"
	install -d "$pkgdir/usr/share/doc/${_pkgname}"
	install -d "$pkgdir/usr/share/licenses/${_pkgname}"

	cp -r neru-classic-* "$pkgdir"/usr/share/icons/

	cp -r LICENSE "$pkgdir"/usr/share/licenses/"${_pkgname}"/
	cp -r {'README.md','AUTHORS','screenshot.svg','screenshot.png'} "$pkgdir"/usr/share/doc/"${_pkgname}"/

}

