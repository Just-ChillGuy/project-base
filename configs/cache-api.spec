Name:           cache-api
Version:        1.0
Release:        1%{?dist}
Summary:        Cache Proxy API

License:        MIT
BuildArch:      noarch

Requires:       python3, python3-flask, python3-redis, python3-requests, python3-pyyaml

%description
Cache Proxy API

%prep

%build

%install
mkdir -p %{buildroot}/opt/cache-api
mkdir -p %{buildroot}/etc/cache-api
mkdir -p %{buildroot}/usr/lib/systemd/system

cp %{_sourcedir}/cache-api.py %{buildroot}/opt/cache-api/cache-api.py
cp %{_sourcedir}/config.yaml %{buildroot}/etc/cache-api/config.yaml
cp %{_sourcedir}/cache-api.service %{buildroot}/usr/lib/systemd/system/cache-api.service

chmod 755 %{buildroot}/opt/cache-api/cache-api.py

%files
/opt/cache-api/cache-api.py
/etc/cache-api/config.yaml
/usr/lib/systemd/system/cache-api.service

%post
systemctl daemon-reload
systemctl enable cache-api
systemctl restart cache-api

%preun
systemctl stop cache-api
systemctl disable cache-api

%postun
systemctl daemon-reload
