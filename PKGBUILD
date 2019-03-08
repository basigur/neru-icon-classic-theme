# Maintainer: basigur

pkgname=neru-icon-classic-theme
pkgver=2.5.1
pkgrel=1
pkgdesc="Classic theme icons Neru"
arch=('any')
url="https://github.com/basigur/neru-icon-classic-theme"
license=('LGPL3')
depends=('gtk-update-icon-cache' 'librsvg' 'hicolor-icon-theme')
replaces=('neru-icon-classic-theme')
conflicts=()
source=("https://github.com/basigur/neru-icon-classic-theme/archive/v${pkgver}.tar.gz")
sha512sums=('E2617ABAE092643F99F54FBB1039B0CF8F5A73882D7974057D4DF01EDCD0C609F692ECDB31C53581F138E5BD8E59D8EDB605FBA9B4FB3B7891EB3A7E2893B602')

package() {
 cd ${pkgname}-${pkgver}
	install -d "$pkgdir/usr/share/icons"
	install -d "$pkgdir/usr/share/doc/${pkgname}"
	install -d "$pkgdir/usr/share/licenses/${pkgname}"

	gtk-update-icon-cache neru-classic-light
	gtk-update-icon-cache neru-classic-dark
	gtk-update-icon-cache neru-classic-light-green
	gtk-update-icon-cache neru-classic-dark-green
	gtk-update-icon-cache neru-classic-light-yellow
	gtk-update-icon-cache neru-classic-dark-yellow

cp -r {'neru-classic-light','neru-classic-dark','neru-classic-light-green','neru-classic-dark-green','neru-classic-light-yellow','neru-classic-dark-yellow'} "$pkgdir"/usr/share/icons/
	cp -r LICENSE "$pkgdir"/usr/share/licenses/"${pkgname}"/
	cp -r {README.md,AUTHORS} "$pkgdir"/usr/share/doc/"${pkgname}"/

}
