# Maintainer(s): Derek Porcelli derekp5831@gmail.com

pkgname=lmp
pkgver=1.0.1
pkgrel=1
pkgdesc="Lightweight media player"
arch=('x86_64')
url="https://github.com/derekporcelli/lmp"
license=('GPL')
depends=('python' 'mpv')
source=("lmp" "lmp.conf")
sha256sums=('088edfb6e5bc0cf3d01f0a3e4d3fc938d8d2738943cff7be33f85db33ddb8670'
            '68764f6f46906d9e88bc95b5bccae8b220079031d8a887fbbde3e80f9ac7e65b')


package() {
    install -Dm755 "$srcdir/lmp" "$pkgdir/usr/bin/lmp"
    install -Dm644 "$srcdir/lmp.conf" "$pkgdir/etc/lmp/lmp.conf"
}
