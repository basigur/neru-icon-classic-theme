# Maintainer: basigur

pkgname=neru-icon-theme
_pkgname=neru-icon-classic-theme
pkgver=2.8
pkgrel=1
pkgdesc="Classic theme icons Neru"
arch=('any')
url="https://github.com/basigur/neru-icon-classic-theme"
license=('LGPL3')
depends=('gtk-update-icon-cache')
replaces=('neru-icon-classic-theme')
conflicts=('neru-icon-classic-theme')
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/basigur/neru-icon-classic-theme/archive/v${pkgver}.tar.gz")
sha512sums=('SKIP')

package() {
	cd "${_pkgname}-${pkgver}"
	install -d "$pkgdir/usr/share/icons"
	cp -r neru-classic-* "$pkgdir/usr/share/icons"
	install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${_pkgname}/LICENSE"

    local _res
    for _res in README.md AUTHORS screenshot.svg screenshot.png
    do
	install -Dm644 "${_res}" "${pkgdir}/usr/share/doc/${_pkgname}/${_res}"
    done
}

