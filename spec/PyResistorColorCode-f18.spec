%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:             PyResistorColorCode
Version:          0.1.0
Release:          1%{?dist}
Summary:          Python module providing some tools to manage IEC 60062 marking codes for resistors.

License:          GPLv3+
Group:            Applications/Engineering
URL:              http://github.com/FabriceSalvaire/PyResistorColorCode

Source0:           http://github.com/downloads/FabriceSalvaire/PyResistorColorCode/%{name}-%{version}.tar.gz

BuildArch:        noarch
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:    python-devel desktop-file-utils

Requires:         PyQt4 >= 4.9

%description
PyResistorColorCode is a Python module that provides some tools to
manage IEC 60062 marking codes for resistors.

The associated program resistor-decoder provides a graphical user
interface to help user to decode a resistor colour-coding using an
inference algorithm. This feature is an enhancement compared to a
program like gresistor which is only a colour-coding calculator.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

desktop-file-install --vendor fedora            \
    --add-category Engineering                  \
    --delete-original                           \
    --dir %{buildroot}%{_datadir}/applications/ \
    %{buildroot}%{_datadir}/applications/resistor-decoder.desktop

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/

%clean
rm -rf %{buildroot}

%post
ln -sf %{_datadir}/PyResistorColorCode/icons/resistor.svg %{_datadir}/icons/hicolor/scalable/apps/resistor-decoder.svg 
# The shell pattern "command || :" return always success
touch --no-create %{_datadir}/icons/hicolor || :
update-desktop-database &> /dev/null || :

%postun
rm %{_datadir}/icons/hicolor/scalable/apps/resistor-decoder.svg 
touch --no-create %{_datadir}/icons/hicolor || :
update-desktop-database &> /dev/null || :

%files
%defattr(-,root,root,-)
%{_bindir}/resistor-decoder
%{_datadir}/PyResistorColorCode/
%{_datadir}/applications/fedora-resistor-decoder.desktop
# datadir/icons/hicolor/scalable/apps/resistor-decoder.svg 
%{python_sitelib}/PyResistorColorCode/
%{python_sitelib}/%{name}-%{version}-py?.?.egg-info

%changelog
* Mon Nov  5 2012 Fabrice Salvaire <fabrice.salvaire@orange.fr> - 0.1.0-1
- Initial package.
# End SPEC
