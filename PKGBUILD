# Maintainer(s): Derek Porcelli derekp5831@gmail.com

pkgname=lmp
pkgver=1.0.4
pkgrel=1
pkgdesc="Lightweight media player"
arch=('x86_64')
url="https://github.com/derekporcelli/lmp"
license=('GPL')
depends=('python' 'mpv')
source=("lmp" "lmp.conf")
sha256sums=('a439b68e632bac86bcc25e96d467631e96b823e064162b090cedd59c4a9aaae4'
            '68764f6f46906d9e88bc95b5bccae8b220079031d8a887fbbde3e80f9ac7e65b')


package() {
    install -Dm755 "$srcdir/lmp" "$pkgdir/usr/bin/lmp"
    install -Dm644 "$srcdir/lmp.conf" "$pkgdir/etc/lmp/lmp.conf"
}
