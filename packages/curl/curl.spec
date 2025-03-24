Name: %{_cross_os}curl
Version: 8.12.1
Release: 1%{dist}
Summary: A utility for getting files from remote servers (FTP, HTTP, and others)
License: curl
URL: https://curl.se

Source0: https://curl.se/download/curl-%{version}.tar.gz

%description
%{summary}

%prep
%autosetup -n curl-%{version} -p1

%build
autoreconf -fiv
%set_cross_build_flags
%configure \
    --prefix=%{_cross_prefix}       \
    --bindir=%{_cross_bindir}       \
    --sbindir=%{_cross_sbindir}     \
    --mandir=%{_cross_mandir}       \
    --libdir=%{_cross_libdir}       \
    --includedir=%{_cross_includedir} \
    --enable-optimize               \
    --disable-httpsrr               \
    --disable-dict                  \
    --disable-gopher                \
    --disable-imap                  \
    --disable-ldap                  \
    --disable-ldaps                 \
    --disable-mqtt                  \
    --disable-ntlm                  \
    --disable-pop3                  \
    --disable-rtsp                  \
    --disable-smb                   \
    --disable-smtp                  \
    --disable-telnet                \
    --disable-tftp                  \
    --disable-tls-srp               \
    --disable-websockets            \
    --disable-docs                  \
    --disable-largefile             \
    --disable-ftp                   \
    --disable-imap                  \
    --disable-libcurl-option        \
    --disable-openssl-auto-load-config  \
    --disable-mime                  \
    --disable-netrc                 \
    --enable-unix-sockets           \
    --without-brotli                \
    --without-libpsl                \
    --without-ssl                   \
    --without-zlib                  \
    --without-ca-bundle             \
    --without-ca-path               \
    --without-ca-fallback           \
    --without-zsh-functions-dir     \
    --without-fish-functions-dir    \
    --without-libuv                 \
    --without-msh3                  \
    --without-openssl-quic          \
    --without-nghttp2               \
    --without-zstd                  \
    --without-libssh

%force_disable_rpath
%make_build

%install
%make_install

%files
%{_cross_bindir}/curl
%{_cross_bindir}/curl-config
%{_cross_libdir}/libcurl.a
%{_cross_libdir}/libcurl.so
%{_cross_libdir}/libcurl.so.4
%{_cross_libdir}/libcurl.so.4.8.0
%{_cross_libdir}/libcurl.pc
/aarch64-bottlerocket-linux-gnu/sys-root/usr/share/licenses/curl/attribution.txt

%changelog
