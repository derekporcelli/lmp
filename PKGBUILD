# Maintainer(s): Derek Porcelli derekp5831@gmail.com

pkgname=lmp
pkgver=1.0.2
pkgrel=1
pkgdesc="Lightweight media player"
arch=('x86_64')
url="https://github.com/derekporcelli/lmp"
license=('GPL')
depends=('python' 'mpv')
source=("lmp" "lmp.conf")
sha256sums=('18dff8d8f5d3a04c2e5adfe76c6d23f43369c7466beee371776a527ab9878375'
            '68764f6f46906d9e88bc95b5bccae8b220079031d8a887fbbde3e80f9ac7e65b')


package() {
    install -Dm755 "$srcdir/lmp" "$pkgdir/usr/bin/lmp"
    install -Dm644 "$srcdir/lmp.conf" "$pkgdir/etc/lmp/lmp.conf"
}
