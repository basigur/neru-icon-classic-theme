# Maintainer: basigur

pkgname=neru-classic-icon
_pkgname=neru-icon-classic-theme
pkgver=3.1
pkgrel=1
pkgdesc="Classic theme icons Neru fork"
arch=('any')
url="https://github.com/basigur/neru-icon-classic-theme"
license=('LGPL3')
depends=('gtk-update-icon-cache')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/basigur/neru-icon-classic-theme/archive/v${pkgver}.tar.gz")
sha512sums=('SKIP')

package() {
    cd "${_pkgname}-${pkgver}"
    install -d "$pkgdir/usr/share/icons"
    cp -r neru*classic/ "$pkgdir/usr/share/icons"
    install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    install -Dm644 README.md AUTHORS -t "${pkgdir}/usr/share/doc/${pkgname}/"
}

