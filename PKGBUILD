# Maintainer: basigur

pkgname=neru-icon-classic-theme
pkgver=2.6
pkgrel=2
pkgdesc="Classic theme icons Neru"
arch=('any')
url="https://github.com/basigur/neru-icon-classic-theme"
license=('LGPL3')
depends=('gtk-update-icon-cache' 'librsvg' 'hicolor-icon-theme')
replaces=('neru-icon-classic-theme')
conflicts=()
source=("https://github.com/basigur/${pkgname}/archive/v${pkgver}.tar.gz")

sha512sums=('077914B2011A6F60A624D36ADBC6F0ECEB08A41749A0234228FD24DA894D74256813C0499CC830E792FEC497056F73F4980686C7E4DF36BD421A3F4F1796A2F8')

package() {
 cd ${pkgname}-${pkgver}

	install -d "$pkgdir/usr/share/icons"
	install -d "$pkgdir/usr/share/doc/${pkgname}"
	install -d "$pkgdir/usr/share/licenses/${pkgname}"

	ln -s filelight.svg neru-classic-light/32x32/apps/org.gnome.DiskUtility.svg
	ln -s ark.svg neru-classic-light/32x32/apps/org.gnome.ArchiveManager.svg
	ln -s preferences-system-privacy.svg neru-classic-light/32x32/apps/org.gnome.seahorse.Application.svg
	ln -s applications-fonts.svg neru-classic-light/32x32/apps/org.gnome.font-viewer.svg

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
