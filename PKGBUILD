# Maintainer(s): Derek Porcelli derekp5831@gmail.com

pkgname=lmp
pkgver=1.0.7
pkgrel=1
pkgdesc="Lightweight media player"
arch=('x86_64')
url="https://github.com/derekporcelli/lmp"
license=('GPL')
depends=('python' 'mpv')
source=("lmp" "lmp.conf")
sha256sums=('2d1cb8bd073f14066aba9f1384177cfabf6e7b61d15e26d8f9eb01284a7f00a6'
            '68764f6f46906d9e88bc95b5bccae8b220079031d8a887fbbde3e80f9ac7e65b')
packager="Derek Porcelli derekp5831@gmail.com"

package() {
    install -Dm755 "$srcdir/lmp" "$pkgdir/usr/bin/lmp"
    install -Dm644 "$srcdir/lmp.conf" "$pkgdir/etc/lmp/lmp.conf"
}
